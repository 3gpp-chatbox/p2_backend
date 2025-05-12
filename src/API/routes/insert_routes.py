
import sys
from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, HTTPException

from src.API.pydantic_models import EditGraph,NewGraphInsert

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.API.pydantic_models import ProcedureItem
from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()


@router.post("/{procedure_id}", response_model=ProcedureItem)
async def insert_edited_graph(procedure_id: UUID, request: NewGraphInsert):
    """
    Insert a new graph version with user-edited extracted data.

    Args:
        procedure_id: UUID of the procedure
        request: Contains the edited `extracted_data` and commit info

    Returns:
        ProcedureItem: Newly inserted graph row
    """
    try:
        with DatabaseHandler() as db:
            # Get procedure and document info
            proc_query = """
            SELECT p.name, d.id AS document_id, d.name AS document_name
            FROM procedure p
            JOIN document d ON p.document_id = d.id
            WHERE p.id = %s
            """
            proc_result = db.execute_query(proc_query, (procedure_id,))
            if not proc_result:
                raise HTTPException(status_code=404, detail="Procedure not found")
            proc = proc_result[0]

            # Get latest graph for metadata reuse
            latest_query = """
            SELECT entity, model_name, accuracy, extraction_method, COALESCE(MAX(version::int), 0) as latest_version
            FROM graph
            WHERE procedure_id = %s
            GROUP BY entity, model_name, accuracy, extraction_method
            ORDER BY latest_version DESC
            LIMIT 1
            """
            latest_result = db.execute_query(latest_query, (procedure_id,))
            if not latest_result:
                raise HTTPException(status_code=400, detail="No existing graph to copy metadata from")

            latest = latest_result[0]
            next_version = str(int(latest["latest_version"]) + 1)

            # Serialize edited graph to JSON string
            edited_graph_json = request.edited_graph.model_dump_json()

            insert_query = """
            INSERT INTO graph (
                entity, extracted_data, model_name, accuracy,
                status, extraction_method, commit_title, commit_message,
                version, procedure_id
            ) VALUES (%s, %s::jsonb, %s, %s, 'verified', %s, %s, %s, %s, %s)
            RETURNING id, created_at
            """
            insert_params = (
                latest["entity"],
                edited_graph_json,
                latest["model_name"],
                latest["accuracy"],
                latest["extraction_method"],
                request.commit_title,
                request.commit_message,
                next_version,
                procedure_id
            )

            insert_result = db.execute_query(insert_query, insert_params)
            if not insert_result:
                raise HTTPException(status_code=500, detail="Failed to insert edited graph")

            new_graph = insert_result[0]

            return ProcedureItem(
                id=new_graph["id"],
                name=proc["name"],
                document_id=proc["document_id"],
                document_name=proc["document_name"],
                graph=request.edited_graph,
                accuracy=latest["accuracy"],
                extracted_at=new_graph["created_at"],
                extraction_method=latest["extraction_method"],  # reused, not overridden with 'modified'
                model_name=latest["model_name"],
                entity=latest["entity"],
                version=next_version,
                status="verified",
                commit_title=request.commit_title,
                commit_message=request.commit_message
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to insert edited graph: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to insert edited graph")
