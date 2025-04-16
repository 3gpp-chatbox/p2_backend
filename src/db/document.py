import sys
from pathlib import Path
from typing import Any

from src.db.db_handler import DatabaseHandler

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)


def get_document_by_name(
    doc_name: str, db_handler: DatabaseHandler
) -> dict[str, Any] | None:
    """Retrieve a document from the database by its name.

    Args:
        doc_name: The unique name of the document to retrieve.
        db_handler: Database connection handler instance.

    Returns:
        Dictionary containing document data if found, None if no document exists.

    Raises:
        ValueError: If an error occurs during database operation.

    Example:
        >>> handler = DatabaseHandler()
        >>> if doc := get_document_by_name("example_doc", handler):
        ...     print(f"Found document: {doc}")
        ... else:
        ...     print("Document not found")
    """
    try:
        # Check if the document exists in the database
        query = "SELECT * FROM document WHERE name = %s"
        result = db_handler.execute_query(
            query=query, parameters=(doc_name,), fetch=True
        )
        doc = result[0] if result else None
        if not doc:
            return None

        return doc

    except Exception as e:
        logger.error(
            f"Error in `get_document_by_name`: Exception encountered while retrieving document '{doc_name}'. Error: {e}",
            exc_info=True,
        )
        raise ValueError(f"Error retrieving document: {e}")
