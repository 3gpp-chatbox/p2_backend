import sys
from pathlib import Path
from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from src.retrieval.sections_content_retrieval import get_sections_content

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.API.pydantic_models import (
    EntityVersionItem,
    OneHistoryVersionItem,
    ProcedureItem,
    ProcedureListItem,
    Reference,
)
from src.db.db_ahandler import AsyncDatabaseHandler
from src.lib.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()


@router.get("/", response_model=List[ProcedureListItem])
async def get_procedure_names_and_entities():
    """
    Get distinct procedure names and entities.
    Used to populate the dropdown list on the frontend.
    """
    try:
        async with AsyncDatabaseHandler() as db:
            async with db.get_connection() as conn:
                query = """
                SELECT 
                    p.id as procedure_id, 
                    p.name as procedure_name, 
                    array_agg(DISTINCT g.entity) as entities
                FROM procedure p
                JOIN graph g ON p.id = g.procedure_id
                GROUP BY p.id, p.name
                ORDER BY p.name
                """
                cur = await conn.execute(query=query)
                results = await cur.fetchall()

                # --- START OF MODIFICATION ---
                available_procedures = []
                for row in results:
                    available_procedures.append(
                        ProcedureListItem(
                            procedure_id=row["procedure_id"],
                            procedure_name=row["procedure_name"],
                            entity=row[
                                "entities"
                            ],  # Pass the parsed list to the Pydantic model
                        )
                    )
                return available_procedures
                # --- END OF MODIFICATION ---

    except Exception as e:
        logger.error(f"Failed to fetch procedures: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch procedures")


@router.get("/{procedure_id}/{entity}", response_model=ProcedureItem)
async def get_latest_graph_by_procedure_id_and_entity(procedure_id: UUID, entity: str):
    """
    Get full latest graph data and metadata by procedure id and entity.
    """
    try:
        async with AsyncDatabaseHandler() as db:
            async with db.get_connection() as conn:
                query = """
                SELECT 
                    g.id as graph_id, g.entity, g.extracted_data, g.model_name, g.accuracy, g.version,
                    g.created_at, g.status, g.extraction_method, g.commit_title, g.commit_message, g.entity,
                    p.name as procedure_name,p.id as procedure_id, p.retrieved_top_sections, p.extracted_at,
                    d.id as document_id, d.name as document_name
                FROM graph g
                JOIN procedure p ON g.procedure_id = p.id
                JOIN document d ON p.document_id = d.id
                WHERE p.id = %s AND LOWER(g.entity) = LOWER(%s)
                ORDER BY g.version::int DESC
                Limit 1
                """

                cur = await conn.execute(
                    query=query,
                    params=(procedure_id, entity),
                )

                result = await cur.fetchone()
                if not result:
                    raise HTTPException(status_code=404, detail="Graph not found")

                document_name = result["document_name"]
                top_sections = result["retrieved_top_sections"]

                context_md = await get_sections_content(
                    db_conn=conn,
                    doc_name=document_name,
                    section_list=top_sections,
                )

                return ProcedureItem(
                    graph_id=result["graph_id"],
                    procedure_name=result["procedure_name"],
                    procedure_id=procedure_id,
                    document_id=result["document_id"],
                    document_name=result["document_name"],
                    graph=result["extracted_data"],
                    created_at=result["created_at"],
                    accuracy=result["accuracy"],
                    extracted_at=result["extracted_at"],
                    model_name=result["model_name"],
                    extraction_method=result["extraction_method"],
                    entity=result["entity"],
                    version=result["version"],
                    status=result["status"],
                    commit_title=result["commit_title"],
                    commit_message=result["commit_message"],
                    reference=Reference(context_markdown=context_md),
                )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to fetch graph: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch graph")


@router.get("/{procedure_id}/{entity}/history", response_model=List[EntityVersionItem])
async def get_graph_versions(procedure_id: UUID, entity: str):
    """
    Get brief info of all versions of a graph for a specific procedure name and entity type.
    """
    try:
        async with AsyncDatabaseHandler() as db:
            async with db.get_connection() as conn:
                query = """
                SELECT 
                g.id as graph_id, g.version, g.created_at,g.commit_title,g.commit_message,
                p.name as procedure_name
                FROM graph g
                JOIN procedure p ON g.procedure_id = p.id
                WHERE p.id = %s AND LOWER(g.entity) = LOWER(%s)
                ORDER BY g.version::int DESC
                """
                cur = await conn.execute(query=query, params=(procedure_id, entity))
                results = await cur.fetchall()

                version_history = [
                    EntityVersionItem(
                        graph_id=row["graph_id"],
                        version=row["version"],
                        created_at=row["created_at"],
                        commit_title=row["commit_title"],
                        commit_message=row["commit_message"],
                    )
                    for row in results
                ]

                if not version_history:
                    raise HTTPException(
                        status_code=404, detail="No version history found"
                    )

                return version_history
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to fetch graph version history: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch version history")


@router.get(
    "/{procedure_id}/{entity}/history/{graph_id}",
    response_model=OneHistoryVersionItem,
)
async def get_one_graph_version_detail(
    procedure_id: UUID,
    entity: str,
    graph_id: UUID,
):
    """
    Get one graph version detail for a specific procedure name and entity type.
    """
    try:
        async with AsyncDatabaseHandler() as db:
            async with db.get_connection() as conn:
                query = """
                SELECT 
                g.extracted_data
                FROM graph g
                WHERE g.procedure_id = %s AND g.entity = %s AND g.id = %s
                """
                cur = await conn.execute(
                    query=query, params=(procedure_id, entity, graph_id)
                )

                result = await cur.fetchone()

                if not result:
                    raise HTTPException(status_code=404, detail="Graph not found")

                graph = result["extracted_data"]

                return OneHistoryVersionItem(graph=graph)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to fetch graph: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch graph")
