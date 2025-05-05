# schema_validation.py
from typing import List, Literal

from pydantic import BaseModel, ConfigDict, Field


class Node(BaseModel):
    """Represents a State or Event in the process"""

    id: str = Field(
        ...,
        description="Unique identifier for the node (e.g., number, 'start', 'end').",
    )
    type: Literal["state", "event"] = Field(
        ..., description="Type of the node, either 'state' or 'event'."
    )
    description: str = Field(..., description="Explanation of the state or event.")

    # model_config = ConfigDict(extra="forbid")


class Edge(BaseModel):
    """Represents a Trigger or Condition connecting Nodes"""

    from_node: str = Field(..., alias="from", description="ID of the starting node.")
    to: str = Field(..., description="ID of the target node.")
    type: str = Field(
        ..., description="Type of the edge, either 'trigger' or 'condition'."
    )
    description: str = Field(
        ..., description="Explanation of the trigger or condition."
    )

    model_config = ConfigDict(serialize_by_alias=True)


class Graph(BaseModel):
    """The actual graph content with nodes and edges"""

    nodes: List[Node] = Field(..., description="List of all states and events.")
    edges: List[Edge] = Field(..., description="List of all triggers and conditions.")

    # model_config = ConfigDict(extra="forbid")
