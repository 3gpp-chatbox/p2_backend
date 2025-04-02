from pydantic import BaseModel, Field, ValidationError
from typing import List, Dict, Any, Literal
import json

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

def validate_data(data: Dict, filename: str) -> bool:
    """
    Validates the graph data against the defined schema.
    Returns True if valid, False if invalid.
    """
    try:
        # Validate entire Graph structure
        graph = Graph(**data)

        print(f"✓ {filename}: Graph validation successful.")
        return True
    except ValidationError as e:
        print(f"✗ {filename}: Graph validation failed.\nError details:\n{e}")
        return False

def load_dataset(file_path: str) -> Dict:
    """Loads a JSON dataset from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"✗ Error loading dataset {file_path}: {e}")
        return None

if __name__ == "__main__":
    # Define datasets to validate
    datasets = [
        "data/consolidated_step3/v01-step3.json",
        "data/consolidated_step3/v02-step3.json",
        "data/consolidated_step3/v03-step3.json",
        "data/consolidated_step3/v04-step3.json"
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
    print("\n=== Validation Summary ===")
    for path, is_valid in results:
        status = "✓ VALID" if is_valid else "✗ INVALID"
        print(f"{status}: {path}")
