# schema_validation.py
from pydantic import BaseModel, Field, ValidationError
from typing import List, Dict, Any, Literal

class Node(BaseModel):
    """Represents a State or Event in the process"""
    id: Any = Field(..., description="Unique identifier for the node (e.g., number, 'start', 'end').")
    type: Literal["state", "event"] = Field(..., description="Type of the node, either 'state' or 'event'.")
    description: str = Field(..., description="Brief explanation of the state or event.")

class Edge(BaseModel):
    """Represents a Trigger or Condition connecting Nodes"""
    from_node: Any = Field(..., alias="from", description="ID of the starting node.")
    to: Any = Field(..., description="ID of the target node.")
    type: str = Field(..., description="Type of the edge, either 'trigger' or 'condition'.")
    description: str = Field(..., description="Explanation of the trigger or condition.")

class Graph(BaseModel):
    """Graph structure containing all States, Events, Triggers, and Conditions"""
    nodes: List[Node] = Field(..., description="List of all states and events.")
    edges: List[Edge] = Field(..., description="List of all triggers and conditions.")

def validate_data(data: Dict) -> bool:
    """
    Validates the graph data against the defined schema.
    Returns True if valid, False if invalid.
    """
    try:
        # Validate entire Graph structure
        graph = Graph(**data)
        print("✓ Data validation successful.")
        return True
    except ValidationError as e:
        print(f"✗ Data validation failed.\nError details:\n{e}")
        return False
