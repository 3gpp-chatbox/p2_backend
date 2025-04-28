"""Document storage module for managing extracted document chunks.

This module provides functionality to store document chunks in a database
with hierarchical relationships using LTREE paths.
"""

import sys
from pathlib import Path
from typing import List

from dotenv import load_dotenv

from src.db.db_handler import DatabaseHandler
from src.retrieval.chunker import Chunk, extract_chunks

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))
from src.lib.logger import get_logger

logger = get_logger(__name__)


def store_extracted_sections(
    db_handler: DatabaseHandler, doc_name: str, toc: str, chunks: List[Chunk]
) -> None:
    """Store extracted document sections in the database.

    This function stores document sections with their hierarchical relationships:
    1. Creates a document record with name and table of contents
    2. Processes chunks to establish parent-child relationships
    3. Stores sections with LTREE paths for hierarchical querying

    Args:
        db_handler (DatabaseHandler): Database handler for performing database operations
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
        with db_handler.transaction():
            # Insert document and get its ID
            doc_insert_query = """
                INSERT INTO document (name, toc)
                VALUES (%s, %s)
                RETURNING id;
            """
            result = db_handler.execute_query(
                doc_insert_query, (doc_name, toc), fetch=True
            )
            doc_id = result[0]["id"] if result else None
            if not doc_id:
                raise ValueError("Failed to get document ID after insertion")
            logger.info(f"Created document record with ID: {doc_id}")

            # Process chunks to establish hierarchy
            section_stack = []  # Stack to track nested sections, stores tuples of (heading, level)

            for chunk in chunks:
                current_level = chunk["level"]

                # Remove sections from stack that are at same or deeper level
                while section_stack and section_stack[-1][1] >= current_level:
                    section_stack.pop()

                # Add current section to stack
                section_stack.append((chunk["heading"], current_level))

                # Build the path string from current stack
                # First encode each heading with encode_for_ltree
                encode_heading_query = "SELECT encode_for_ltree(%s) as encoded;"
                path_parts = []
                for section in section_stack:
                    result = db_handler.execute_query(
                        encode_heading_query, (section[0],), fetch=True
                    )
                    encoded = result[0]["encoded"]
                    path_parts.append(encoded)
                path = ".".join(path_parts)

                # Determine parent (if any)
                parent = None
                if current_level > 1 and len(section_stack) > 1:
                    # Parent will be the previous section in the stack
                    parent = section_stack[-2][0]

                # Insert section record
                section_insert_query = """
                    INSERT INTO section (document_id, heading, level, content, parent, path)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """
                db_handler.execute_query(
                    section_insert_query,
                    (
                        doc_id,
                        chunk["heading"],
                        chunk["level"],
                        chunk["content"],
                        parent,
                        path,
                    ),
                    fetch=False,
                )

            logger.info(f"Successfully stored {len(chunks)} sections")

    except Exception as e:
        logger.error(f"Error storing sections: {str(e)}")
        raise


if __name__ == "__main__":
    # Integrated example showcasing both chunking and storing functionality
    load_dotenv(override=True)  # Load environment variables from .env file
    try:
        # First, extract chunks from the markdown document
        file_path = Path("data/markdown/24501-filtered.md")
        result = extract_chunks(file_path)

        # Read TOC from the TOC file
        toc_path = Path("data/markdown/24501-toc.md")
        toc = toc_path.read_text(encoding="utf-8")

        # Initialize database handler and store chunks
        with DatabaseHandler() as db_handler:
            store_extracted_sections(
                db_handler, result["doc_name"], toc, result["chunks"]
            )

    except Exception as e:
        logger.error(f"Error in document processing pipeline: {e}")
