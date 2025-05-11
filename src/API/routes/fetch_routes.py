import sys
from pathlib import Path
from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from src.retrieval.sections_content_retrieval import get_sections_content

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.API.pydantic_models import ProcedureListItem, EntityVersionItem, ProcedureItem
from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()


@router.get("/reference/{procedure_id}")
def get_reference_context(procedure_id: str):
    try:
        with DatabaseHandler() as db_handler:
            query = """
                SELECT p.name AS procedure_name, d.name AS doc_name, p.retrieved_top_sections
                FROM procedure p
                JOIN document d ON p.document_id = d.id
                WHERE p.id = %s
            """
            result = db_handler.execute_query(query, parameters=(procedure_id,), fetch=True)

            if not result:
                raise HTTPException(status_code=404, detail="Procedure not found")

            row = result[0]
            doc_name = row["doc_name"]
            procedure_name = row["procedure_name"]
            top_sections = row["retrieved_top_sections"]

            context_md = get_sections_content(
                db_handler=db_handler,
                doc_name=doc_name,
                section_list=top_sections
            )

            return {"context_markdown": context_md}

    except Exception as e:
        logger.error(f"Error fetching reference context: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/procedures", response_model=List[ProcedureListItem])
async def get_procedure_names():
    """
    Get distinct procedure names.
    Used to populate the dropdown list on the frontend.
    """
    try:
        with DatabaseHandler() as db:
            query = "SELECT id, name FROM procedure ORDER BY name"
            results = db.execute_query(query)

            return [ProcedureListItem(id=row["id"], name=row["name"]) for row in results]

    except Exception as e:
        logger.error(f"Failed to fetch procedures: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch procedure names")


@router.get("/procedures/{procedure_id}", response_model=List[EntityVersionItem])
async def get_latest_graphs_for_entities(procedure_id: UUID):
    """
    Get the latest verified version of each entity type for a given procedure.
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT DISTINCT ON (g.entity)
                g.id, g.entity, g.version, g.accuracy, g.model_name, g.created_at
            FROM graph g
            JOIN procedure p ON g.procedure_id = p.id
            WHERE p.id = %s
            ORDER BY g.entity, g.version::int DESC
            """
            results = db.execute_query(query, (procedure_id,))

            return [
                EntityVersionItem(
                    graph_id=row["id"],
                    entity=row["entity"],
                    version=row["version"],
                    accuracy=row["accuracy"],
                    model_name=row["model_name"],
                    created_at=row["created_at"]
                )
                for row in results
            ]

    except Exception as e:
        logger.error(f"Failed to fetch latest entity graphs: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch entity graphs")


@router.get("/graph/{graph_id}", response_model=ProcedureItem)
async def get_graph_by_id(graph_id: UUID):
    """
    Get full graph data and metadata by graph ID.
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT 
                g.id, g.entity, g.extracted_data, g.model_name, g.accuracy, g.version,
                g.created_at, g.status, g.extraction_method, g.commit_title, g.commit_message,
                p.name as procedure_name,
                d.id as document_id, d.name as document_name
            FROM graph g
            JOIN procedure p ON g.procedure_id = p.id
            JOIN document d ON p.document_id = d.id
            WHERE g.id = %s
            """
            results = db.execute_query(query, (graph_id,))
            if not results:
                raise HTTPException(status_code=404, detail="Graph not found")

            row = results[0]
            return ProcedureItem(
                id=row["id"],
                name=row["procedure_name"],
                document_id=row["document_id"],
                document_name=row["document_name"],
                graph=row["extracted_data"],  # Only one graph now
                accuracy=row["accuracy"],
                extracted_at=row["created_at"],
                model_name=row["model_name"],
                extraction_method=row["extraction_method"],
                entity=row["entity"],
                version=row["version"],
                status=row["status"],
                commit_title=row["commit_title"],
                commit_message=row["commit_message"],
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to fetch graph: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch graph")


@router.get("/history/{procedure_id}/{entity}", response_model=List[EntityVersionItem])
async def get_graph_versions(procedure_id: UUID, entity: str):
    """
    Get all versions of a graph for a specific procedure name and entity type.
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT 
                g.id, g.version, g.accuracy, g.model_name, g.created_at,g.commit_title,g.commit_message 
            FROM graph g
            JOIN procedure p ON g.procedure_id = p.id
            WHERE p.id = %s AND g.entity = %s
            ORDER BY g.version::int DESC
            """
            results = db.execute_query(query, (procedure_id, entity))

            return [
                EntityVersionItem(
                    graph_id=row["id"],
                    entity=entity,
                    version=row["version"],
                    accuracy=row["accuracy"],
                    model_name=row["model_name"],
                    created_at=row["created_at"],
                    commit_title=row["commit_title"],
                    commit_message=row["commit_message"],
                )
                for row in results
            ]

    except Exception as e:
        logger.error(f"Failed to fetch graph version history: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch version history")
