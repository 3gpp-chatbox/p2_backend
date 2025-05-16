import sys
from pathlib import Path
from typing import Any, Optional
from uuid import UUID

from psycopg import AsyncConnection

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)


async def get_document_by_name(
    doc_name: str, db_conn: AsyncConnection
) -> dict[str, Any] | None:
    """Retrieve a document from the database by its name.

    Args:
        doc_name: The unique name of the document to retrieve.
        db_conn: Database connection instance.

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
        cur = await db_conn.execute(
            query=query,
            params=(doc_name,),
        )

        result = await cur.fetchone()

        doc = result if result else None
        if not doc:
            return None

        return doc

    except Exception as e:
        logger.error(
            f"Error in `get_document_by_name`: Exception encountered while retrieving document '{doc_name}'. Error: {e}",
            exc_info=True,
        )
        raise ValueError(f"Error retrieving document: {e}")


async def get_document_id_by_name(
    db_conn: AsyncConnection,
    document_name: str,
) -> Optional[UUID]:
    """
    Get document ID from the database by document name.

    Args:
        db: Database handler instance
        document_name: Name of the document

    Returns:
        UUID of the document if found, None otherwise
    """
    try:
        query = "SELECT id FROM document WHERE name = %s"
        parameters = (document_name,)

        cur = await db_conn.execute(
            query=query,
            params=parameters,
        )

        result = await cur.fetchone()

        if not result:
            logger.warning(f"Document with name '{document_name}' not found")
            return None

        return result["id"]
    except Exception as e:
        logger.error(f"Error retrieving document ID: {e}")
        return None
