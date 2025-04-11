'''
Defines API response/request models.
'''
from pydantic import BaseModel, UUID4
from typing import Dict, Any, Optional
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
        document_id: UUID of the source document
        document_name: Name of the source document
        original_graph: JSON representation of the original procedure graph
        edited_graph: Optional JSON representation of the edited procedure graph
        accuracy: Confidence score of the procedure
        extracted_at: Timestamp of extraction
        last_edit_at: Optional timestamp of last edit
        status: Status of the graph ('original' or 'edited')
    """
    id: UUID4
    name: str
    document_id: UUID4
    document_name: str
    original_graph: Dict[str, Any]
    edited_graph: Optional[Dict[str, Any]] = None
    accuracy: float
    extracted_at: datetime
    last_edit_at: Optional[datetime] = None
    status: str
    
class EditedGraph(BaseModel):
    """model for edited graph.
    
    Attributes:
        graph_id: UUID of the edited graph
        edited_graph: The edited graph data in JSON format
    """
    graph_id: UUID4
    edited_graph: Dict[str, Any]

