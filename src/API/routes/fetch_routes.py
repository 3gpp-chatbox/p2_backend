import sys
from pathlib import Path
from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from src.retrieval.sections_content_retrieval import get_sections_content

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.API.pydantic_models import ProcedureListItem, EntityVersionItem, ProcedureItem,Reference,OneHistoryVersionItem
from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger
import re

logger = get_logger(__name__)
router = APIRouter()


@router.get("/", response_model=List[ProcedureListItem])
async def get_procedure_names_and_entities():
    """
    Get distinct procedure names and entities.
    Used to populate the dropdown list on the frontend.
    """
    try:
        with DatabaseHandler() as db:
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
            results = db.execute_query(query, fetch=True) 

            # --- START OF MODIFICATION ---
            processed_items = []
            for row in results:
                entity_raw_string = row["entities"] # This will be the string like '{UE,AMF}'

                parsed_entities = []
                if entity_raw_string and entity_raw_string.startswith('{') and entity_raw_string.endswith('}'):
                    content = entity_raw_string[1:-1] # Remove outer braces
                    if content: # Check if there's any content inside the braces
                        # Use regex to split by comma, handling potential quotes within elements
                        parsed_entities = [
                            item.strip().strip('"') for item in re.findall(r'(?:[^,"]|"(?:[^"])*")+', content)
                        ]
                
                processed_items.append(
                    ProcedureListItem(
                        procedure_id=row["procedure_id"], 
                        procedure_name=row["procedure_name"], 
                        entity=parsed_entities # Pass the parsed list to the Pydantic model
                    )
                )
            return processed_items
            # --- END OF MODIFICATION ---

    except Exception as e:
        logger.error(f"Failed to fetch procedures: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch procedure names")


@router.get("/{procedure_Id}/{entity}", response_model=ProcedureItem)
async def get_latest_graph_by_procedure_id_and_entity(procedure_id: UUID, entity: str):
    """
    Get full latest graph data and metadata by procedure id and entity.
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT 
                g.id as graph_id, g.entity, g.extracted_data, g.model_name, g.accuracy, g.version,
                g.created_at, g.status, g.extraction_method, g.commit_title, g.commit_message,
                p.name as procedure_name,p.id as procedure_id, p.retrieved_top_sections,
                d.id as document_id, d.name as document_name
            FROM graph g
            JOIN procedure p ON g.procedure_id = p.id
            JOIN document d ON p.document_id = d.id
            WHERE p.id = %s AND g.entity = %s
            ORDER BY g.version::int DESC
            Limit 1
            """
            results = db.execute_query(query, (procedure_id, entity))
            if not results:
                raise HTTPException(status_code=404, detail="Graph not found")
            
            

            row = results[0]
            document_name=row["document_name"]
            top_sections = row["retrieved_top_sections"]
            context_md = get_sections_content(
                db_handler=db,
                doc_name=document_name,
                section_list=top_sections
            )


            return ProcedureItem(
                graph_id=row["graph_id"],
                procedure_name=row["procedure_name"],
                procedure_id=procedure_id,
                document_id=row["document_id"],
                document_name=row["document_name"],
                graph=row["extracted_data"],  # Only one graph now
                accuracy=row["accuracy"],
                extracted_at=row["created_at"],
                model_name=row["model_name"],
                extraction_method=row["extraction_method"],
                entity=entity,
                version=row["version"],
                status=row["status"],
                commit_title=row["commit_title"],
                commit_message=row["commit_message"],
                reference={"context_markdown": context_md}
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
        with DatabaseHandler() as db:
            query = """
            SELECT 
            g.id as graph_id, g.version, g.created_at,g.commit_title,g.commit_message,
            p.name as procedure_name
            FROM graph g
            JOIN procedure p ON g.procedure_id = p.id
            WHERE p.id = %s AND g.entity = %s
            ORDER BY g.version::int DESC
            """
            results = db.execute_query(query, (procedure_id, entity))

            return [
                EntityVersionItem(
                    graph_id=row["graph_id"],
                    version=row["version"],
                    created_at=row["created_at"],
                    commit_title=row["commit_title"],
                    commit_message=row["commit_message"],
                )
                for row in results
            ]

    except Exception as e:
        logger.error(f"Failed to fetch graph version history: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch version history")


@router.get("/{procedure_id}/{entity}/history/{graph_id}", response_model=List[OneHistoryVersionItem])
async def get_one_graph_version_detail(procedure_id: UUID, entity: str, graph_id: UUID,):
    """
    Get one graph version detail for a specific procedure name and entity type.
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT 
            g.extracted_data
            FROM graph g
            WHERE g.procedure_id = %s AND g.entity = %s AND g.id = %s
            """
            results = db.execute_query(query, (procedure_id, entity, graph_id))

            return [
                OneHistoryVersionItem(
                    graph=row["extracted_data"]
                )
                for row in results
            ]

    except Exception as e:
        logger.error(f"Failed to fetch graph version history: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch version history")
