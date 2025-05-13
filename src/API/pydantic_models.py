"""
Defines API response/request models.
"""
from datetime import datetime
from typing import Optional,List
from pydantic import UUID4, BaseModel
from src.schemas.procedure_graph import Graph


class ProcedureListItem(BaseModel):
    """Basic procedure information for list view.

    Attributes:
        id: UUID of the procedure
        name: Name of the procedure
    """
    procedure_id: UUID4
    procedure_name: str
    entity:List


class Reference(BaseModel):
    context_markdown: str

class ProcedureItem(BaseModel):
    """Procedure graph with metadata and accuracy.

    Attributes:
        id: UUID of the graph
        name: Name of the procedure
        document_id: UUID of the source document
        document_name: Name of the source document
        graph: JSON representation of the procedure graph
        accuracy: Confidence score of the procedure
        extracted_at: Timestamp of extraction
        extraction_method: Method used to extract the graph
        model_name: Name of the model used
        entity: Type of network entity (e.g., UE, AMF)
        version: Version of the graph
        status: Status of the graph (e.g., new, verified)

    """
    graph_id: UUID4
    procedure_name: str
    procedure_id: UUID4
    document_id: UUID4
    document_name: str
    graph: Graph
    accuracy: float
    extracted_at: datetime
    extraction_method: str
    model_name: str
    entity: str
    version: str
    status: str
    commit_title: str
    commit_message: str
    reference: Reference



class EntityVersionItem(BaseModel):
    """Represents a version of a graph for a specific network entity.

    Attributes:
        graph_id: UUID of the graph
        entity: Type of the entity (e.g., UE, AMF)
        version: Version string of the graph
        accuracy: Accuracy of the graph extraction
        model_name: Name of the model used
        created_at: Timestamp when the graph was created
        commit_title: Title of the associated commit
        commit_message: Description of the associated commit
    """
    graph_id: UUID4
    version: str
    created_at: datetime
    commit_title: Optional[str] = None
    commit_message: Optional[str] = None

class Graph(Graph):
    pass


class NewGraphInsert(BaseModel):
    edited_graph: Graph
    commit_title: str
    commit_message: str

class NewProcedureItemInfo(BaseModel):
    graph_id: UUID4
    procedure_name: str
    procedure_id: UUID4
    document_id: UUID4
    document_name: str
    graph: Graph
    accuracy: float
    extracted_at: datetime
    extraction_method: str
    model_name: str
    entity: str
    version: str
    status: str
    commit_title: str
    commit_message: str




class OneHistoryVersionItem(BaseModel):
    graph: Graph