import sys
from pathlib import Path

from src.db.db_handler import DatabaseHandler

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)


def get_document_by_name(doc_name: str, db_handler: DatabaseHandler) -> str | None:
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
