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

def validate_data(data: Dict, filename: str) -> bool:
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
                
        print(f"✓ {filename}: Graph structure validation successful")
        return True
    except Exception as e:
        print(f"✗ {filename}: Graph validation failed - {str(e)}")
        return False

def load_dataset(file_path: str) -> Dict:
    """Loads a JSON dataset from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading dataset {file_path}: {str(e)}")
        return None

if __name__ == "__main__":
    # Define datasets to validate
    datasets = [
        "../../data/consolidated_step3/v01-step3.json",
        "../../data/consolidated_step3/v02-step3.json",
        "../../data/consolidated_step3/v03-step3.json",
        "../../data/consolidated_step3/v04-step3.json"
    ]
    
    print("\n=== Starting Dataset Validation ===\n")
    
    # Track validation results
    results = []
    
    # Validate each dataset
    for dataset_path in datasets:
        print(f"Processing: {dataset_path}")
        dataset = load_dataset(dataset_path)
        
        if dataset:
            is_valid = validate_data(dataset, dataset_path.split('/')[-1])
            results.append((dataset_path, is_valid))
        else:
            results.append((dataset_path, False))
        print()  # Add blank line between datasets
    
    # Print summary
    print("=== Validation Summary ===")
    for path, is_valid in results:
        status = "✓ VALID" if is_valid else "✗ INVALID"
        print(f"{status}: {path}")