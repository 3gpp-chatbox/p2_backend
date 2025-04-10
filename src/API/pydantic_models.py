'''
Defines API response/request models.
'''
from pydantic import BaseModel, UUID4
from typing import Dict, Any
from datetime import datetime

class ProcedureListItem(BaseModel):
    """Basic procedure information for list view.
    
    Attributes:
        id: UUID of the procedure
        name: Name of the procedure
    """
    id: UUID4
    name: str

class ProcedureItem(BaseModel):  
    """Procedure graph with accuracy.
    
    Attributes:
        id: UUID of the procedure
        name: Name of the procedure
        document_id: Reference to the source document
        graph: JSON representation of the procedure graph
        accuracy: Confidence score of the procedure
        created_at: Timestamp of creation
    """
    id: UUID4
    name: str
    document_id: UUID4
    graph: Dict[str, Any]  
    accuracy: float
    created_at: datetime
    


