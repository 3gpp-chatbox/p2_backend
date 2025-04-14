# schema_validation.py
from typing import Dict, List, Literal

from pydantic import BaseModel, Field, ValidationError


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


class GraphContent(BaseModel):
    """The actual graph content with nodes and edges"""

    nodes: List[Node] = Field(..., description="List of all states and events.")
    edges: List[Edge] = Field(..., description="List of all triggers and conditions.")


class Graph(BaseModel):
    """Graph structure containing all States, Events, Triggers, and Conditions"""

    graph: GraphContent = Field(
        ..., description="The graph content with nodes and edges."
    )


def validate_data(data: Dict) -> bool:
    """
    Validates the graph data against the defined schema.
    Returns True if valid, False if invalid.
    """
    try:
        # First validate the basic structure
        graph = Graph(**data)

        # Get all valid node IDs
        node_ids = {node.id for node in graph.graph.nodes}

        # Check if all edge references point to valid nodes
        for edge in graph.graph.edges:
            if edge.from_node not in node_ids:
                print(f"✗ Invalid edge: 'from' node {edge.from_node} does not exist")
                return False
            if edge.to not in node_ids:
                print(f"✗ Invalid edge: 'to' node {edge.to} does not exist")
                return False

        print("✓ Data schema validation successful.")
        return True
    except ValidationError as e:
        print(f"✗ Data schema validation failed.\nError details:\n{e}")
        return False
