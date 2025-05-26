from uuid import UUID

import numpy as np
from psycopg import AsyncConnection
from pydantic.types import UUID4

from src.lib.logger import logger
from src.schemas.procedure_graph import Graph


async def store_graph(
    name: str,
    document_id: UUID4,
    graph_data: Graph,
    accuracy: float,
    model: str,
    extraction_method: str,
    entity: str,
    top_level_sections: list,
    commit_title: str,
    commit_message: str,
    version: str,
    status: str,
    db_conn: AsyncConnection,
) -> UUID:
    """
    Store a graph in the database using the new schema with separate procedure and graph tables.

    Args:
        name: Name of the graph
        document_id: ID of the document this graph belongs to
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
        # Convert graph data to JSON
        graph_json = graph_data.model_dump_json()

        # Convert top_level_sections to list if it's a numpy array
        if isinstance(top_level_sections, np.ndarray):
            top_level_sections = top_level_sections.tolist()

        async with db_conn.transaction():
            # Check if the procedure already exists
            check_procedure_query = """
            SELECT id FROM procedure
            WHERE LOWER(name) = LOWER(%s) AND document_id = %s
            """
            check_procedure_params = (name, document_id)

            cur = await db_conn.execute(
                query=check_procedure_query,
                params=check_procedure_params,
            )

            existing_procedure_result = await cur.fetchone()

            procedure_id = None
            if existing_procedure_result:
                procedure_id = existing_procedure_result["id"]
                logger.info(
                    f"Found existing procedure '{name}' with ID: {procedure_id}"
                )

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
                INSERT INTO procedure (name, document_id, retrieved_top_sections)
                VALUES (%s, %s, %s)
                RETURNING id
                """
                procedure_insert_params = (name, document_id, top_level_sections)

                cur = await db_conn.execute(
                    query=procedure_insert_query,
                    params=procedure_insert_params,
                )

                procedure_insert_result = await cur.fetchone()

                if not procedure_insert_result:
                    raise Exception("Failed to store procedure data")

                procedure_id = procedure_insert_result["id"]
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
                status,
                procedure_id,
                accuracy,
                extraction_method,
                commit_title,
                commit_message,
                version
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """
            graph_params = (
                entity,
                graph_json,
                model,
                status,
                procedure_id,  # <--- Using the existing or newly created procedure_id
                accuracy,
                extraction_method,
                commit_title,
                commit_message,
                version,
            )

            cur = await db_conn.execute(
                query=graph_query,
                params=graph_params,
            )

            graph_result = await cur.fetchone()

            if not graph_result:
                raise Exception("Failed to store graph data")

            graph_id = graph_result["id"]

            logger.info(
                f"Stored graph for entity '{entity}' with ID: {graph_id} linked to procedure ID: {procedure_id}"
            )
            return graph_id

    except Exception as e:
        logger.error(f"Error storing graph: {e}")
        raise


# Example usage
if __name__ == "__main__":
    import asyncio

    from src.db.db_ahandler import AsyncDatabaseHandler

    async def main() -> None:
        try:
            async with AsyncDatabaseHandler() as db:
                async with db.get_connection as conn:
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
                    document_name = (
                        "Sample Document 2"  # This should be an existing document name
                    )
                    graph_id = store_graph(
                        name="Sample Graph",
                        document_name=document_name,
                        graph_data=sample_graph,
                        accuracy=0.95,
                        model="Sample Model",
                        extraction_method="main",
                        entity=entity,
                        top_level_section=top_level_section,
                        commit_title="Sample Commit Title",
                        commit_message="Sample Commit Message",
                        version="1",
                        db_conn=conn,
                    )

                    if graph_id:
                        print(f"Stored graph with ID: {graph_id}")
                    else:
                        print(f"Failed to store graph for document: {document_name}")

        except Exception as e:
            logger.error(f"Error in example: {e}", exc_info=True)

    asyncio.run(main())
