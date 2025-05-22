"""Document storage module for managing extracted document chunks.

This module provides functionality to store document chunks in a database
with hierarchical relationships using LTREE paths. Document sections are stored
with paths that represent their hierarchical structure, where each section's
heading is hex-encoded to ensure LTREE compatibility (since LTREE paths only
support alphanumeric characters and underscores).

For example, a document structure like:
    Chapter 1
        Section 1.1
            Subsection 1.1.1
Would be stored with paths like:
    4368617074657231 (hex for "Chapter1")
    4368617074657231.53656374696f6e312e31 (hex for "Chapter1.Section1.1")
    4368617074657231.53656374696f6e312e31.537562736563746f6e312e312e31

This encoding strategy allows for efficient hierarchical queries while preserving
the original document structure, regardless of special characters in headings.
"""

import asyncio
import sys
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from psycopg import AsyncConnection

from src.db.db_ahandler import AsyncDatabaseHandler
from src.retrieval.chunker import Chunk, extract_chunks

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))
from src.lib.logger import get_logger

logger = get_logger(__name__)


async def store_extracted_sections(
    db_conn: AsyncConnection,
    doc_spec: str,
    doc_version: str,
    doc_release: int,
    doc_toc: str,
    chunks: List[Chunk],
) -> None:
    """Store extracted document sections in the database.

    This function stores document sections with their hierarchical relationships:
    1. Creates a document record with name and table of contents
    2. Processes chunks to establish parent-child relationships
    3. Stores sections with LTREE paths for hierarchical querying

    Each section's path in the LTREE structure is built by:
    1. Converting each ancestor section's heading to hex encoding
    2. Joining the hex-encoded headings with dots
    This ensures LTREE compatibility while preserving the exact heading text,
    as LTREE paths are restricted to alphanumeric chars and underscores.
    The hex encoding allows for:
    - Special character preservation
    - Case sensitivity
    - Efficient hierarchical queries using LTREE operators

    Args:
        db_conn (AsyncConnection): Database connection for performing database operations
        doc_name (str): Name of the document
        toc (str): Table of Contents in text format
        chunks (List[Chunk]): List of parsed sections, each containing:
            - heading (str): Section heading
            - content (str): Section content
            - level (int): Heading level

    Raises:
        ValueError: If input parameters are invalid
        psycopg.Error: If database operations fail
    """
    if not chunks:
        logger.warning("No chunks provided for storage")
        return

    try:
        async with db_conn.transaction():
            async with db_conn.cursor() as cur:
                # Insert document and get its ID
                doc_insert_query = """
                    INSERT INTO document (spec, toc, release, version)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """

                await cur.execute(
                    doc_insert_query, (doc_spec, doc_toc, doc_release, doc_version)
                )

                result = await cur.fetchone()
                doc_id = result["id"] if result else None

                # Check if document ID was retrieved
                if not doc_id:
                    raise ValueError("Failed to get document ID after insertion")
                logger.info(f"Created document record with ID: {doc_id}")

                # Process chunks to establish hierarchy
                section_stack = []  # Stack to track nested sections, stores tuples of (heading, level)

                sections_data = []  # List to store section data for batch insertion
                for chunk in chunks:
                    current_level = chunk["level"]

                    # Remove sections from stack that are at same or deeper level
                    while section_stack and section_stack[-1][1] >= current_level:
                        section_stack.pop()

                    # Add current section to stack
                    section_stack.append((chunk["heading"], current_level))

                    # Build the path string from current stack
                    # First encode each heading to hex
                    path_parts = []
                    for section in section_stack:
                        encoded = section[0].encode("utf-8").hex()
                        path_parts.append(encoded)
                    path = ".".join(path_parts)

                    # Determine parent (if any)
                    parent = None
                    if current_level > 1 and len(section_stack) > 1:
                        # Parent will be the previous section in the stack
                        parent = section_stack[-2][0]

                    sections_data.append(
                        (
                            doc_id,
                            chunk["heading"],
                            chunk["level"],
                            chunk["content"],
                            parent,
                            path,
                        ),
                    )
                # Insert section record
                section_insert_query = """
                    INSERT INTO section (document_id, heading, level, content, parent, path)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """

                await cur.executemany(section_insert_query, sections_data)

            logger.info(f"Successfully stored {len(chunks)} sections")

    except Exception as e:
        logger.error(f"Error storing sections: {str(e)}")
        raise


if __name__ == "__main__":
    load_dotenv(override=True)  # Load environment variables from .env file

    async def main():
        try:
            # First, extract chunks from the markdown document
            file_path = Path("data/markdown/24501-filtered.md")
            result = extract_chunks(file_path)

            # Read TOC from the TOC file
            toc_path = Path("data/markdown/24501-toc.md")
            toc = toc_path.read_text(encoding="utf-8")

            # Initialize database handler and store chunks
            async with AsyncDatabaseHandler() as db_handler:
                await store_extracted_sections(
                    db_handler, result["doc_name"], toc, result["chunks"]
                )

        except Exception as e:
            logger.error(f"Error in document processing pipeline: {e}")

    asyncio.run(main())
