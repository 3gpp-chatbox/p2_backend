import sys
from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, HTTPException

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.db.db_ahandler import AsyncDatabaseHandler
from src.lib.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.delete("/{procedure_id}/{entity}")
async def delete_procedure_graph(procedure_id: UUID, entity: str):
    """
    Delete all graphs for a specific procedure and entity combination.
    This will only delete the graphs, keeping the procedure and other entity graphs intact.
    
    Args:
        procedure_id (UUID): The UUID of the procedure
        entity (str): The entity type (e.g., 'UE', 'AMF')
        
    Returns:
        dict: A message indicating successful deletion
        
    Raises:
        HTTPException: If the procedure/entity combination doesn't exist or deletion fails
    """
    try:
        async with AsyncDatabaseHandler() as db:
            async with db.get_connection() as conn:
                # First check if procedure and entity combination exists
                query = """
                SELECT p.name as procedure_name, COUNT(g.id) as graph_count
                FROM procedure p
                JOIN graph g ON p.id = g.procedure_id
                WHERE p.id = %s AND LOWER(g.entity) = LOWER(%s)
                GROUP BY p.name
                """
                result = await conn.execute(query, (procedure_id, entity))
                procedure_info = await result.fetchone()
                
                if not procedure_info:
                    raise HTTPException(
                        status_code=404, 
                        detail=f"No graphs found for procedure {procedure_id} and entity {entity}"
                    )
                
                # Delete all graphs for this procedure and entity
                delete_query = """
                DELETE FROM graph 
                WHERE procedure_id = %s AND LOWER(entity) = LOWER(%s)
                """
                await conn.execute(delete_query, (procedure_id, entity))
                
                return {
                    "message": f"Successfully deleted {procedure_info['graph_count']} graphs for procedure '{procedure_info['procedure_name']}' ({entity} side)"
                }
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete procedure graphs: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete procedure graphs") 