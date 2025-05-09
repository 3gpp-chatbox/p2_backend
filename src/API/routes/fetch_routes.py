import sys
from pathlib import Path
from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.API.pydantic_models import ProcedureItem, ProcedureListItem
from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()


@router.get("/", response_model=List[ProcedureListItem])
async def get_procedures():
    """
    Get list of all available procedures.

    Returns:
        List[ProcedureListItem]: List of procedures with basic information
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT id, name 
            FROM graph 
            ORDER BY extracted_at DESC
            """
            results = db.execute_query(query)

            if not results:
                return []

            procedures = [
                ProcedureListItem(id=row["id"], name=row["name"]) for row in results
            ]
            return procedures

    except Exception as e:
        logger.error(f"Failed to fetch procedures: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to fetch procedures: {str(e)}"
        )


@router.get("/{procedure_id}", response_model=ProcedureItem)
async def get_procedure(procedure_id: UUID):
    """
    Get detailed information about a specific procedure.

    Args:
        procedure_id: UUID of the procedure

    Returns:
        ProcedureGraph: Complete procedure information including graph data
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT g.id, g.name, g.document_id, d.name as document_name, g.original_graph, g.edited_graph, 
                   g.accuracy, 
                   TO_CHAR(g.extracted_at, 'DD-MM-YYYY HH24:MI') as extracted_at,
                   CASE 
                       WHEN g.last_edit_at IS NULL THEN NULL 
                       ELSE TO_CHAR(g.last_edit_at, 'DD-MM-YYYY HH24:MI')
                   END as last_edit_at,
                   g.edited, g.model_name, g.extraction_method 
            FROM graph g
            JOIN document d ON g.document_id = d.id
            WHERE g.id = %s
            """

            results = db.execute_query(query, (procedure_id,))

            if not results:
                raise HTTPException(
                    status_code=404,
                    detail=f"Procedure with id {procedure_id} not found",
                )

            row = results[0]
            return ProcedureItem(
                id=row["id"],
                name=row["name"],
                document_id=row["document_id"],
                document_name=row["document_name"],
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
        logger.error(f"Failed to fetch procedure details: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to fetch procedure details: {str(e)}"
        )
