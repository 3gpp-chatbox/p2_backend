"""Markdown document chunking module.

This module provides functionality to extract chunks from markdown documents.
Each chunk contains a heading, its content, and the heading level.
"""

import sys
from pathlib import Path
from typing import List, TypedDict

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

logger = get_logger(__name__)


class Chunk(TypedDict):
    """Dictionary type for document chunks."""

    heading: str
    content: str
    level: int


class ExtractedDocument(TypedDict):
    """Dictionary type for extracted document data."""

    doc_name: str
    chunks: List[Chunk]


def extract_chunks(file_path: str | Path) -> ExtractedDocument:
    """Extract chunks from a markdown file.

    This function processes a markdown file and extracts sections based on headings.
    Each section includes its heading text, content, and heading level.

    Args:
        file_path (str | Path): Path to the markdown file.
            Can be either a string path or a Path object.

    Returns:
        ExtractedDocument: A dictionary containing:
            - doc_name (str): Name of the document extracted from file path
            - chunks (List[Chunk]): List of dictionaries containing:
                - heading (str): The cleaned heading text
                - content (str): The aggregated text below the heading
                - level (int): The computed heading level

    Raises:
        FileNotFoundError: If the input file doesn't exist
        ValueError: If the markdown content is malformed
        IOError: If there are issues reading the file

    """
    # Convert to Path object if string is provided
    path = Path(file_path)
    logger.info(f"Processing markdown file: {path}")

    # Verify file exists
    if not path.exists():
        logger.error(f"File not found: {path}")
        raise FileNotFoundError(f"File not found: {path}")

    # Verify file is a file (not a directory)
    if not path.is_file():
        logger.error(f"Path is not a file: {path}")
        raise ValueError(f"Path is not a file: {path}")

    try:
        # Read file content
        content = path.read_text(encoding="utf-8")
        logger.info(f"Successfully read file content, size: {len(content)} characters")

        # Extract document name from file path (format: {doc_name}-{doc_description}.md)
        doc_name = path.stem.split("-")[0]
        logger.info(f"Extracted document name: {doc_name}")

        # Split content into lines for processing
        lines = content.split("\n")
        chunks = []
        current_chunk = None
        current_content = []

        # Process each line
        for line in lines:
            # Check if line is a heading
            if line.startswith("#"):
                # If we have a previous chunk, save it
                if current_chunk is not None:
                    current_chunk["content"] = "\n".join(current_content).strip()
                    chunks.append(current_chunk)

                # Process new heading
                heading_match = line.strip()
                level = len(heading_match) - len(heading_match.lstrip("#"))
                heading_text = heading_match[level:].strip()

                # Create new chunk
                current_chunk: Chunk = {
                    "heading": heading_text,
                    "level": level,
                    "content": "",
                }
                current_content = []
            elif current_chunk is not None:
                current_content.append(line)

        # Add the last chunk if exists
        if current_chunk is not None:
            current_chunk["content"] = "\n".join(current_content).strip()
            chunks.append(current_chunk)

        logger.info(f"Extracted {len(chunks)} chunks")

        return {"doc_name": doc_name, "chunks": chunks}

    except IOError as e:
        logger.error(f"Failed to read file {path}: {str(e)}")
        raise IOError(f"Failed to read file {path}: {str(e)}")


if __name__ == "__main__":
    # Example usage of the document chunker
    try:
        # Extract chunks from the filtered document
        file_path = Path("data/markdown/24501-filtered.md")
        result = extract_chunks(file_path)
        # Print first two chunks without formatting
        if result["chunks"]:
            print("\nFirst two chunks:")
            for chunk in result["chunks"][:2]:
                print(chunk)

    except Exception as e:
        logger.error(f"Error processing document: {e}")
