import sys
from pathlib import Path

from psycopg import AsyncConnection

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

logger = get_logger(__name__)


async def get_sections_content(
    db_conn: AsyncConnection, doc_name: str, section_list: list[str]
) -> str:
    """Fetch and format section contents from a document based on section identifiers.
    Args:
        db_conn (AsyncConnection): Database connection instance.
        doc_name (str): Name of the document to fetch sections from.
        section_list (list[str]): List of section identifiers to fetch.

    Returns:
        str: Markdown formatted string containing the fetched sections

    Raises:
        ValueError: If document is not found or sections cannot be retrieved.
        Exception: For any other database or processing errors.
    """
    if not doc_name:
        raise ValueError("Missing required argument: doc_name")
    if not section_list:
        raise ValueError("Missing required argument: section_list")
    if not all(isinstance(section, str) for section in section_list):
        raise ValueError("All section identifiers must be strings")

    try:
        async with db_conn.cursor() as cur:
            # Retrieve document ID by its name to verify document exists
            doc_fetch_query = """
            SELECT 
                id,
                name 
            FROM document 
            WHERE name = %s
            """

            # Step 1. Check if document exists
            await cur.execute(
                query=doc_fetch_query,
                params=(doc_name,),
            )

            result = await cur.fetchone()

            doc_id = result["id"] if result else None
            if not doc_id:
                raise ValueError(f"Document '{doc_name}' not found in the database.")

            # Step 2: Fetch the path for every section in the section_list
            # Find all sections whose headings match the given patterns
            # Uses ILIKE for case-insensitive matching and checks if section heading starts with pattern
            path_fetch_query = """
            SELECT 
                heading,
                path
            FROM section 
            WHERE document_id = %s
                AND EXISTS (
                    SELECT 1 
                    FROM unnest(%s::text[]) AS pattern
                    WHERE section.heading ILIKE pattern || ' %%'
                )
            """

            await cur.execute(
                query=path_fetch_query,
                params=(doc_id, section_list),
            )

            sections = await cur.fetchall()

            if not sections:
                raise ValueError(
                    f"No sections found for document '{doc_name}' with the given parameter: {section_list}"
                )

            logger.info(
                f"Found {len(sections)} matching sections for document '{doc_name}'"
            )

            sections_path = [section["path"] for section in sections]
            sections_heading = [section["heading"] for section in sections]

            logger.debug(
                f"Matched sections for document '{doc_name}': {', '.join(sections_heading)}"
            )

            # Step 3: Fetch the contents for every section hirearchaly in the sections_path
            # Fetch content for all sections hierarchically using ltree path operator
            # path <@ ANY (%s) finds all sections whose path is descendant of any given path
            content_fetch_query = """
            SELECT 
                heading,
                level,
                content
            FROM section
            WHERE document_id = %s
                AND path <@ ANY (%s)
            ORDER BY path
            """

            await cur.execute(
                query=content_fetch_query,
                params=(doc_id, sections_path),
            )

            sections_content = await cur.fetchall()

            if not sections_content:
                raise ValueError(
                    f"Failed to perform hierarchical search for document '{doc_name}' with the given parameter: {section_list}"
                )

            logger.debug(
                f"Retrieved {len(sections_content)} sections (including subsections) "
                f"for document '{doc_name}' under paths: {', '.join(sections_path)}"
            )

            # Step 4 generate markdown
            markdown = _generate_markdown(doc_name, sections_content)

            return markdown

    except Exception as e:
        logger.error("Error in `fetch_sections_content`", exc_info=True)
        raise Exception(
            f"fetch_sections_content: Failed to retrieve sections: {str(e)}"
        ) from e


def _generate_markdown(
    doc_name: str, sections_content: list[dict[str, str | int]]
) -> str:
    """Generate markdown formatted string from document sections.

    Args:
        doc_name (str): Name of the document.
        sections_content (list[dict[str, str | int]]): List of dictionaries containing section data.
            Each dictionary should have 'heading', 'level', and 'content' keys.

    Returns:
        str: Markdown formatted string containing the document content.
    """
    try:
        md_lines = []

        md_lines.append(f"# {doc_name}")
        md_lines.append("")  # Add a blank line after the title

        for section in sections_content:
            heading = section["heading"]
            level = section["level"]
            content = section["content"]

            # Create md heading
            md_heading = "#" * level + " " + heading

            md_lines.append(md_heading)
            md_lines.append("")  # Add a blank line after the heading

            if content.strip():
                md_lines.append(content)
                md_lines.append("")  # Add a blank line after the content

        return "\n".join(md_lines).strip()

    except Exception as e:
        logger.error("Error in `_generate_markdown`", exc_info=True)
        raise Exception(
            f"`_generate_markdown`: Failed to generate markdown: {str(e)}"
        ) from e


if __name__ == "__main__":
    # Example usage

    import asyncio

    from src.db.db_ahandler import AsyncDatabaseHandler

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    async def main() -> None:
        try:
            async with AsyncDatabaseHandler() as db_handler:
                async with db_handler.get_connection() as conn:
                    doc_name = "3GPP TS 24.501"
                    section_list = ["4.2", "5.2"]

                    sections_content = await get_sections_content(
                        db_conn=conn,
                        doc_name=doc_name,
                        section_list=section_list,
                    )

                    # save file (Optional: for manual review)
                    output_file = Path("data/markdown/extracted_section.md")
                    output_file.parent.mkdir(
                        parents=True, exist_ok=True
                    )  # Create parent directories if they don't exist
                    output_file.write_text(sections_content, encoding="utf-8")

        except Exception as e:
            logger.error(f"Error: {e}", exc_info=True)

    asyncio.run(main())
