from pydantic import BaseModel, UUID4
from typing import Dict, Any
from datetime import datetime

class ProcedureListItem(BaseModel):
    """Basic procedure information for list view.
    
    Attributes:
        id: UUID of the procedure
        name: Name of the procedure
        document_id: Reference to the source document
        created_at: Timestamp of creation
    """
    id: UUID4
    name: str
    document_id: UUID4
    created_at: datetime

class ProcedureGraph(BaseModel):  # Note: Fixed the class name to follow PascalCase convention
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
    graph: Dict[str, Any]  # For JSONB data
    accuracy: float
    created_at: datetime
    


