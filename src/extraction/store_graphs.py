import sys
from pathlib import Path
from typing import Dict, Optional
from uuid import UUID
import json

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger

logger = get_logger(__name__)


def get_document_id_by_name(db: DatabaseHandler, document_name: str) -> Optional[UUID]:
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

        result = db.execute_query(query, parameters)
        if not result:
            logger.warning(f"Document with name '{document_name}' not found")
            return None

        return result[0]["id"]
    except Exception as e:
        logger.error(f"Error retrieving document ID: {e}")
        return None


def store_graph(
    name: str,
    document_name: str,
    graph_data: Dict,
    accuracy: float,
    db: DatabaseHandler,
    status: str = 'original',
    edited_graph: Optional[Dict] = None
) -> Optional[UUID]:
    """
    Store a graph in the database.

    Args:
        name: Name of the graph
        document_name: Name of the document this graph belongs to
        graph_data: Graph data as a dictionary
        accuracy: Accuracy score of the graph
        db: Database handler instance for database operations
        status: Status of the graph ('original' or 'edited'), defaults to 'original'
        edited_graph: Optional edited version of the graph. If provided, status will be set to 'edited'

    Returns:
        UUID of the stored graph if successful, None otherwise

    Raises:
        Exception: If database operation fails
    """
    try:
        # If edited_graph is provided, force status to 'edited'
        if edited_graph is not None:
            status = 'edited'
        # Validate status
        elif status not in ['original', 'edited']:
            logger.error(f"Invalid status: {status}. Must be 'original' or 'edited'")
            return None
            
        # Get document_id from document name
        document_id = get_document_id_by_name(db, document_name)
        if not document_id:
            logger.error(f"Cannot store graph: Document '{document_name}' not found")
            return None

        # Check if graph already exists for this document
        check_query = """
        SELECT id FROM graph 
        WHERE document_id = %s AND name = %s
        """
        check_params = (document_id, name)
        result = db.execute_query(check_query, check_params)

        if result:
            logger.warning(
                f"Graph '{name}' already exists for document '{document_name}'"
            )
            return result[0]["id"]

        # Convert Python dicts to JSON strings for PostgreSQL
        graph_json = json.dumps(graph_data)
        edited_json = json.dumps(edited_graph) if edited_graph is not None else None
        
        # Insert graph data into the database
        query = """
        INSERT INTO graph (
            name, 
            document_id, 
            original_graph, 
            edited_graph, 
            accuracy, 
            status,
            last_edit_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id
        """
        
        # Set last_edit_at to NOW() if edited_graph is provided, otherwise NULL
        last_edit_at = "NOW()" if edited_graph is not None else None
        
        parameters = (
            name, 
            document_id, 
            graph_json,      # Now a JSON string
            edited_json,     # Now a JSON string or None
            accuracy, 
            status,
            last_edit_at
        )

        with db.transaction():
            result = db.execute_query(query, parameters)
            if not result:
                raise Exception("Failed to store graph data")

            graph_id = result[0]["id"]
            logger.info(f"Stored graph '{name}' with ID: {graph_id}")
            return graph_id

    except Exception as e:
        logger.error(f"Error storing graph: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Initialize database handler
        db = DatabaseHandler()
        # dummy graph
        sample_graph = {
            "nodes": [
                {"id": "1", "label": "Node 1", "type": "entity"},
                {"id": "2", "label": "Node 2", "type": "action"},
            ],
            "edges": [
                {"source": "1", "target": "2", "label": "performs"},
            ],
        }

        # Store the graph
        document_name = "Sample Document 1"  # This should be an existing document name
        graph_id = store_graph(
            name="Sample Graph",
            document_name=document_name,
            graph_data=sample_graph,
            accuracy=0.95,
            db=db,
        )

        if graph_id:
            print(f"Stored graph with ID: {graph_id}")
        else:
            print(f"Failed to store graph for document: {document_name}")

    except Exception as e:
        logger.error(f"Error in example: {e}", exc_info=True)
