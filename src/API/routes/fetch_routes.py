from fastapi import APIRouter, HTTPException
from typing import List
import sys
from pathlib import Path
from uuid import UUID
# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.API.models import ProcedureListItem, ProcedureGraph

router = APIRouter()

@router.get("procedureList", response_model=List[ProcedureListItem])
async def get_procedures():
    """
    Get list of all available procedures.
    
    Returns:
        List[ProcedureListItem]: List of procedures with basic information
    """
    try:
        # TODO: Replace with actual database query
        # Example SQL:
        # SELECT id, name, document_id, created_at 
        # FROM graph 
        # ORDER BY created_at DESC
        procedures = [
            {
                "id": "reg_proc",
                "name": "Registration Procedure"

            },
            {
                "id": "dereg_proc",
                "name": "Deregistration Procedure"
            }
        ]
        return procedures
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch procedures: {str(e)}"
        )

@router.get("procedures/{procedure_id}", response_model=ProcedureGraph)
async def get_procedure(procedure_id: UUID):
    """
    Get detailed information about a specific procedure.
    
    Args:
        procedure_id: UUID of the procedure
    
    Returns:
        ProcedureGraph: Complete procedure information including graph data
    """
    try:
        # TODO: Replace with actual database query
        # Example SQL:
        # SELECT id, name, document_id, graph, accuracy, created_at 
        # FROM graph 
        # WHERE id = procedure_id
        # Example response for Registration procedure
        if procedure_id == "reg_proc":
            return {
                "id": "reg_proc",
                "name": "Registration Procedure",
                "graph": {
                    "nodes": [
                        {
                            "id": "start",
                            "type": "state",
                            "description": "UE initiates registration"
                        }
                    ],
                    "edges": [
                        {
                            "from_node": "start",
                            "to": "auth",
                            "type": "trigger",
                            "description": "Send Registration Request"
                        }
                    ]
                },
                "accuracy": 0.95
            }
        
        raise HTTPException(
            status_code=404,
            detail=f"Procedure with id {procedure_id} not found"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch procedure details: {str(e)}"
        ) 


