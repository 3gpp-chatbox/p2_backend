import sys
from pathlib import Path

from psycopg import AsyncConnection
from pydantic.types import UUID4

from src.db.document import get_document_by_id
from src.retrieval.sections_content_retrieval import get_sections_content
from src.retrieval.toc_retrieval import (
    find_procedure_section_lines,
    get_top_level_sections,
)
from src.schemas.types.context import DocumentContext

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)


async def get_context(
    doc_id: UUID4, procedure_name: str, db_conn: AsyncConnection
) -> DocumentContext:
    """Retrieves context and top-level sections for a specific procedure from a document.

    Args:
        doc_id (UUID4): ID of the document to search in.
        procedure_name (str): Name of the procedure to find sections for.
        db_handler (DatabaseHandler): Database connection handler instance.

    Returns:
        DocumentContext: A Pydantic model containing:
            - context (str): The retrieved content of the sections.
            - top_level_sections (List[str]): List of top-level sections found for the procedure.

    Raises:
        ValueError: If the document is not found, no matching sections are found,
            or no top-level sections are found for the procedure.
    """
    try:
        # Get document
        doc = await get_document_by_id(doc_id=doc_id, db_conn=db_conn)

        if not doc:
            logger.error(f"Document with ID '{doc_id}' not found in the database.")
            raise ValueError(f"Document with ID '{doc_id}' not found in the database.")

        # Get relevant sections
        section_lines = find_procedure_section_lines(
            toc_lines=doc.toc.splitlines(), procedure_name=procedure_name
        )

        logger.info(
            f"Found {len(section_lines)} section candidates for '{procedure_name}' in document '{doc_id}'."
        )

        if not section_lines:
            logger.error(
                f"No section lines found for '{procedure_name}' in document '{doc_id}'."
            )
            raise ValueError(
                f"Required section lines found for '{procedure_name}' not found in document '{doc_id}'."
            )

        top_level_sections = get_top_level_sections(section_lines=section_lines)

        if top_level_sections.size == 0:
            logger.error(
                f"No top level sections found for '{procedure_name}' in document '{doc_id}'."
            )
            raise ValueError(
                f"Required top level sections for '{procedure_name}' not found in document '{doc_id}'."
            )

        logger.info(
            f"Found {top_level_sections} top-level sections for '{procedure_name}' in document '{doc_id}'."
        )

        context = await get_sections_content(
            # Get sections content
            db_conn=db_conn,
            doc_id=doc.id,
            section_list=top_level_sections.tolist(),
        )

        return DocumentContext(
            context=context, top_level_sections=top_level_sections.tolist()
        )

    except Exception as e:
        logger.error(
            f"Error in `get_context`: Exception encountered while processing document '{doc_id}'. Error: {e}",
            exc_info=True,
        )
        raise ValueError(f"Error retrieving context: {e}")


if __name__ == "__main__":
    import asyncio

    from src.db.db_ahandler import AsyncDatabaseHandler

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    async def main() -> None:
        """Main function to demonstrate the usage of get_context."""
        # Sample parameters for demonstration

        doc_name = "3GPP TS 24.501"
        procedure_name = "Initial Registration"

        try:
            async with AsyncDatabaseHandler() as db_handler:
                async with db_handler.get_connection() as conn:
                    context_data = await get_context(
                        doc_name=doc_name,
                        procedure_name=procedure_name,
                        db_conn=conn,
                    )

                    print("Retrieved DocumentContext:")
                    print(context_data.context)
                    print("Top Level Sections:")
                    print(context_data.top_level_sections)
        except Exception as e:
            print(f"Error occurred: {e}")

    asyncio.run(main())
