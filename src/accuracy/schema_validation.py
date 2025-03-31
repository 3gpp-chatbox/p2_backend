from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import json

class NodeProperties(BaseModel):
    """Schema for node properties"""
    state_change: Optional[str] = None
    entity: Optional[str] = None
    messages: Optional[List[str]] = None
    message_sent: Optional[str] = None
    state_required: Optional[str] = None
    state_change: Optional[str] = None
    condition: Optional[str] = None
    side_effects: Optional[str] = None
    trigger: Optional[str] = None
    timeout: Optional[str] = None
    outcomes: Optional[List[Dict[str, Any]]] = None

class Node(BaseModel):
    """Schema for validating nodes"""
    id: Any  # Can be numeric or "start"/"finish"
    type: str  # "start", "process", "decision", "timer", etc.
    description: str
    properties: NodeProperties

class EdgeProperties(BaseModel):
    """Schema for edge properties"""
    trigger: Optional[str] = None
    conditions: Optional[str] = None
    outcome: Optional[List[Dict[str, Any]]] = None

class Edge(BaseModel):
    """Schema for validating edges"""
    from_node: Any = Field(alias="from")
    to: Any
    type: str  # "sequential", "conditional", "retry"
    properties: Dict[str, Any]

class Graph(BaseModel):
    """Schema for the entire graph structure"""
    graph: Dict[str, List[Any]]  # Contains "nodes" and "edges" lists

def validate_data(data: Dict) -> bool:
    """
    Validates the graph data against the defined schema.
    Returns True if valid, False if invalid.
    """
    try:
        # First validate the overall structure
        graph = Graph(**data)
        
        # Then validate each node individually
        for node in data["graph"]["nodes"]:
            Node(**node)
            
        # Validate edges if they exist
        if "edges" in data["graph"]:
            for edge in data["graph"]["edges"]:
                Edge(**edge)
                
        print("✓ Graph structure validation successful")
        return True
    except Exception as e:
        print(f"✗ Graph validation failed: {str(e)}")
        return False

def load_dataset(file_path: str) -> Dict:
    """Loads a JSON dataset from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading dataset: {str(e)}")
        return None

if __name__ == "__main__":
    # Load dataset
    print("Loading dataset...")
    dataset = load_dataset("../../data/version_1/step3.json")
    
    if dataset:
        print("Validating dataset...")
        is_valid = validate_data(dataset)
        print(f"Validation result: {'✓ Valid' if is_valid else '✗ Invalid'}")
    else:
        print("Failed to load dataset")