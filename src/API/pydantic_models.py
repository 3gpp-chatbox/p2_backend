"""
Defines API response/request models.
"""

from typing import Any, Dict, Optional

from pydantic import UUID4, BaseModel

from src.schemas.procedure_graph import Graph


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
    document_name: str
    document_id: UUID4
    edited: bool
    original_graph: Graph
    edited_graph: Optional[Graph] = None
    accuracy: float
    extraction_method: str
    model_name: str
    extracted_at: str
    last_edit_at: Optional[str] = None


class EditedGraph(BaseModel):
    """model for edited graph.

    Attributes:
        edited_graph: The edited graph data in JSON format
    """

    edited_graph: Dict[str, Any]
