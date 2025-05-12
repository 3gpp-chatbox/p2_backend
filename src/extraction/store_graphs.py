import sys
from pathlib import Path
from typing import Optional
from uuid import UUID
import numpy as np
import os
from dotenv import load_dotenv
from src.schemas.procedure_graph import Graph
from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger
from src.retrieval.toc_retrieval import get_top_level_sections, find_procedure_section_lines

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

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
    entity: str,  # Now passed as a parameter
    top_level_sections: list,  # Now passed as a parameter
    commit_title: str ,
    commit_message: str,  # Optional, default value can be overridden
    version: str ,  # Optional, default value can be overridden
    status: str,
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
        entity: The entity (e.g., AMF or UE) to associate with the graph
        top_level_sections: List of top-level sections for the procedure
        commit_title: Title for the commit (optional, default is 'original graph')
        commit_message: Commit message for the graph (optional, default is 'procedure graph extracted')
        version: Version of the graph (optional, default is '1')
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

        # Convert graph data to JSON
        graph_json = graph_data.model_dump_json()

        # Convert top_level_sections to list if it's a numpy array
        if isinstance(top_level_sections, np.ndarray):
            top_level_sections = top_level_sections.tolist()

        with db.transaction():
            # Check if the procedure already exists
            check_procedure_query = """
            SELECT id FROM procedure
            WHERE name = %s AND document_id = %s
            """
            check_procedure_params = (name, document_id)
            existing_procedure_result = db.execute_query(check_procedure_query, check_procedure_params)

            procedure_id = None
            if existing_procedure_result:
                procedure_id = existing_procedure_result[0]["id"]
                logger.info(f"Found existing procedure '{name}' with ID: {procedure_id}")

                # Optional: Update retrieved_top_sections if they might change or be more complete
                # This depends on your logic. If top_level_sections can evolve, you might want to update it.
                # update_procedure_query = """
                # UPDATE procedure SET retrieved_top_sections = %s WHERE id = %s
                # """
                # db.execute_query(update_procedure_query, (top_level_sections, procedure_id), fetch=False) # fetch=False for UPDATE

            else:
                # If procedure does not exist, insert a new one
                logger.info(f"Procedure '{name}' not found, creating new entry.")
                procedure_insert_query = """
                INSERT INTO procedure (name, document_id, retrieved_top_sections, extracted_at)
                VALUES (%s, %s, %s, NOW())
                RETURNING id
                """
                procedure_insert_params = (name, document_id, top_level_sections)
                procedure_insert_result = db.execute_query(procedure_insert_query, procedure_insert_params)

                if not procedure_insert_result:
                    raise Exception("Failed to store procedure data")
                
                procedure_id = procedure_insert_result[0]["id"]
                logger.info(f"Created new procedure '{name}' with ID: {procedure_id}")

            # Ensure we have a procedure_id before inserting the graph
            if not procedure_id:
                raise Exception("Failed to obtain or create procedure ID")

            # Then insert into graph table, linking to the obtained/created procedure_id
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
            VALUES (%s, %s, %s, NOW(), %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """
            graph_params = (
                entity,
                graph_json,
                model,
                status,
                procedure_id, # <--- Using the existing or newly created procedure_id
                accuracy,
                extraction_method,
                commit_title,
                commit_message,
                version
            )
            
            graph_result = db.execute_query(graph_query, graph_params)
            if not graph_result:
                raise Exception("Failed to store graph data")

            graph_id = graph_result[0]["id"]
            logger.info(f"Stored graph for entity '{entity}' with ID: {graph_id} linked to procedure ID: {procedure_id}")
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

        # Dummy top-level section and entity
        top_level_section = ["Top Section 1", "Top Section 2"]
        entity = "AMF"

        # Store the graph
        document_name = "Sample Document 2"  # This should be an existing document name
        graph_id = store_graph(
            name="Sample Graph",
            document_name=document_name,
            graph_data=sample_graph,
            accuracy=0.95,
            model="Sample Model",
            extraction_method="Sample Method",
            entity=entity,
            top_level_section=top_level_section,
            commit_title="Sample Commit Title",
            commit_message="Sample Commit Message",
            version="1",
            db=db,
        )

        if graph_id:
            print(f"Stored graph with ID: {graph_id}")
        else:
            print(f"Failed to store graph for document: {document_name}")

    except Exception as e:
        logger.error(f"Error in example: {e}", exc_info=True)
