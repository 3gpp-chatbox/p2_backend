import sys
from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, HTTPException

from src.API.pydantic_models import EditGraph

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.API.pydantic_models import ProcedureItem
from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()


@router.put("/{procedure_id}", response_model=ProcedureItem)
async def update_graph_with_edit(procedure_id: UUID, request: EditGraph):
    """
    Update a procedure graph with an edited version.

    Args:
        procedure_id: UUID of the procedure to update
        edit_request: Request containing the edited graph data

    Returns:
        ProcedureItem: Updated procedure information

    Raises:
        HTTPException: If the procedure is not found or update fails
    """
    try:
        with DatabaseHandler() as db:
            # First check if the procedure exists
            check_query = """
            SELECT id, document_id
            FROM graph
            WHERE id = %s
            """
            results = db.execute_query(check_query, (procedure_id,))

            if not results:
                raise HTTPException(
                    status_code=404,
                    detail=f"Procedure with id {procedure_id} not found",
                )

            # Get the current graph data
            current_graph = results[0]

            # Convert the edited_graph dict to JSON string
            edited_graph_json = request.edited_graph.model_dump_json()

            # Update the graph with the edited version
            update_query = """
            UPDATE graph
            SET edited_graph = %s,
                last_edit_at = NOW(),
                edited = true
            WHERE id = %s
            RETURNING id, name, document_id, original_graph, edited_graph,
                      accuracy, 
                      TO_CHAR(extracted_at, 'DD-MM-YYYY HH24:MI') as extracted_at,
                      CASE 
                          WHEN last_edit_at IS NULL THEN NULL 
                          ELSE TO_CHAR(last_edit_at, 'DD-MM-YYYY HH24:MI')
                      END as last_edit_at,
                      edited, model_name, extraction_method
            """
            update_params = (edited_graph_json, procedure_id)

            updated_results = db.execute_query(update_query, update_params)

            if not updated_results:
                raise HTTPException(
                    status_code=500, detail="Failed to update the graph"
                )

            # Get the document name for the response
            doc_query = """
            SELECT name
            FROM document
            WHERE id = %s
            """
            doc_results = db.execute_query(doc_query, (current_graph["document_id"],))
            document_name = (
                doc_results[0]["name"] if doc_results else "Unknown Document"
            )

            # Return the updated procedure
            row = updated_results[0]

            return ProcedureItem(
                id=row["id"],
                name=row["name"],
                document_id=row["document_id"],
                document_name=document_name,
                original_graph=row["original_graph"],
                edited_graph=row["edited_graph"],
                accuracy=row["accuracy"],
                extracted_at=row["extracted_at"],
                last_edit_at=row["last_edit_at"],
                edited=row["edited"],
                model_name=row["model_name"],
                extraction_method=row["extraction_method"],
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to update graph with edit: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to update graph with edit: {str(e)}"
        )
