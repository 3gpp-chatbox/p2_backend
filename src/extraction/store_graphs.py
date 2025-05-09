import sys
from pathlib import Path
from typing import Optional
from uuid import UUID
import numpy as np

from src.schemas.procedure_graph import Graph

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger
from src.retrieval.toc_retrieval import get_top_level_sections, find_procedure_section_lines
import os
from dotenv import load_dotenv

logger = get_logger(__name__)

# Load environment variables
load_dotenv()

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
    graph_data: Graph,
    accuracy: float,
    model: str,
    extraction_method: str,
    db: DatabaseHandler,
) -> Optional[UUID]:
    """
    Store a graph in the database using the new schema with separate procedure and graph tables.

    Args:
        name: Name of the graph
        document_name: Name of the document this graph belongs to
        graph_data: Graph data as a dictionary
        accuracy: Accuracy score of the graph
        model: Name of the model used for extraction
        extraction_method: Method used for extraction
        db: Database handler instance for database operations

    Returns:
        UUID of the stored graph if successful, None otherwise

    Raises:
        Exception: If database operation fails
    """
    try:
        # Get document_id from document name
        document_id = get_document_id_by_name(db, document_name)
        if not document_id:
            logger.error(f"Cannot store graph: Document '{document_name}' not found")
            return None

        # Get document TOC to find relevant sections
        toc_query = "SELECT toc FROM document WHERE id = %s"
        toc_result = db.execute_query(toc_query, (document_id,))
        if not toc_result:
            logger.error(f"Cannot find TOC for document '{document_name}'")
            return None

        # Find relevant sections and get top-level section
        section_lines = find_procedure_section_lines(toc_result[0]["toc"].splitlines(), name)

        
        top_level_section = get_top_level_sections(section_lines)
        # If for some reason it's a NumPy array:
        if isinstance(top_level_section, np.ndarray):
          top_level_section = top_level_section.tolist()
        
        if len(top_level_section) == 0:
            logger.error(f"No sections found for procedure '{name}' in document '{document_name}'")
            return None

 

        # Get entity value from environment variable
        entity = os.getenv("ENTITY", "{}")

        # Convert graph data to JSON
        graph_json = graph_data.model_dump_json()

        with db.transaction():
            # First insert into procedure table
            procedure_query = """
            INSERT INTO procedure (name, document_id, retrieved_top_sections, extracted_at)
            VALUES (%s, %s, %s, NOW())
            RETURNING id
            """
            procedure_params = (name, document_id, top_level_section)
            procedure_result = db.execute_query(procedure_query, procedure_params)
            
            if not procedure_result:
                raise Exception("Failed to store procedure data")
            
            procedure_id = procedure_result[0]["id"]



            # Then insert into graph table
            graph_query = """
            INSERT INTO graph (
                entity,
                extracted_data,
                model_name,
                created_at,
                status,
                procedure_id,
                accuracy,
                extraction_method,
                commit_title,
                commit_message,
                version
            )
            VALUES (%s, %s, %s, NOW(), 'new', %s, %s, %s,'original graph','procedure graph extracted','1')
            RETURNING id
            """
            graph_params = (
                entity,
                graph_json,
                model,
                procedure_id,
                accuracy,
                extraction_method
            )
            
            graph_result = db.execute_query(graph_query, graph_params)
            if not graph_result:
                raise Exception("Failed to store graph data")

            graph_id = graph_result[0]["id"]
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
        document_name = "Sample Document 2"  # This should be an existing document name
        graph_id = store_graph(
            name="Sample Graph",
            document_name=document_name,
            graph_data=sample_graph,
            accuracy=0.95,
            model="Sample Model",
            extraction_method="Sample Method",
            db=db,
        )

        if graph_id:
            print(f"Stored graph with ID: {graph_id}")
        else:
            print(f"Failed to store graph for document: {document_name}")

    except Exception as e:
        logger.error(f"Error in example: {e}", exc_info=True)