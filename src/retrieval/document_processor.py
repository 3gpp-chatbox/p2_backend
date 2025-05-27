"""
Document Processing Pipeline

This module implements the main document processing pipeline for converting DOCX files
to markdown format and storing them in a database. The pipeline performs the following steps:

1. Loads environment variables for document path configuration
2. Converts DOCX files to markdown format
3. Extracts content chunks from the markdown
4. Stores the processed chunks in the database

Usage:
    Ensure the DOCUMENT_PATH environment variable is set to the path of your DOCX file.
    Then run the script:

    ```bash
    python -m src.retrieval.main
    ```

Requirements:
    - Environment Variables:
        DOCUMENT_PATH: Path to the DOCX file to be processed

Notes:
    - The script expects a valid DOCX file at the specified path
    - The process will create markdown files in the configured output directory
    - Processed chunks are stored in the database for later retrieval

Raises:
    ValueError: If environment variables are missing or if processing fails
    FileNotFoundError: If the specified document path doesn't exist
    RuntimeError: If an unexpected error occurs during processing
"""

import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from src.db.db_ahandler import AsyncDatabaseHandler
from src.lib.logger import logger, setup_logger
from src.retrieval.chunker import extract_chunks_from_content
from src.retrieval.pre_processor import docx_to_markdown
from src.retrieval.store_chunks import store_extracted_sections


async def main() -> None:
    """Process a DOCX document through the conversion and storage pipeline.

    This function orchestrates the document processing pipeline:
    1. Loads and validates environment variables
    2. Converts DOCX to markdown format
    3. Extracts content chunks
    4. Stores processed data in the database

    Returns:
        None

    Raises:
        ValueError: If any of these conditions occur:
            - DOCUMENT_PATH environment variable is missing
            - Markdown conversion fails to produce content, TOC, or document name
            - No chunks could be extracted from the content
            - Any other processing error occurs
        RuntimeError: If an unexpected error occurs during processing
        FileNotFoundError: If the document specified in DOCUMENT_PATH doesn't exist
    """
    load_dotenv(override=True)
    setup_logger()  # Initialize logging configuration
    try:
        # Get document path from environment variables
        DOCUMENT_PATH = os.getenv("DOCUMENT_PATH")
        if not DOCUMENT_PATH:
            raise ValueError("Missing environment variable: DOCUMENT_PATH")

        # Convert string path to Path object for better path handling
        doc_path = Path(DOCUMENT_PATH)
        if not doc_path.is_file():
            raise FileNotFoundError(f"Document not found or is not a file: {doc_path}")

        # Convert DOCX to Markdown format and extract document structure
        markdown_output = docx_to_markdown(file_path=doc_path, save_markdown=True)

        md_content = markdown_output.content
        toc = markdown_output.toc
        spec = markdown_output.spec
        version = markdown_output.version
        release = markdown_output.release

        # Validate that all required components were extracted successfully
        if not md_content or not toc or not spec:
            raise ValueError(
                "Markdown conversion failed: Missing content, toc, or spec."
            )

        # Split markdown content into manageable chunks for processing
        chunks = extract_chunks_from_content(content=md_content)

        if not chunks:
            raise ValueError("No chunks extracted from the markdown content.")

        # Store processed chunks and document structure in the database
        async with AsyncDatabaseHandler() as db_handler:
            async with db_handler.get_connection() as conn:
                await store_extracted_sections(
                    db_conn=conn,
                    doc_spec=spec,
                    doc_toc=toc,
                    doc_version=version,
                    doc_release=release,
                    chunks=chunks,
                )
    except Exception as e:
        logger.error(f"Unexpected document processing error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    # Set the event loop policy for Windows to support async PostgreSQL
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # count how long it took to run the script
    import time

    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    logger.info(
        f"Main document_processor function executed in {end_time - start_time} seconds"
    )
