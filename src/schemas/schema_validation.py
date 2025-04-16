from typing import Dict

from pydantic import ValidationError

from src.schemas.procedure_graph import Graph


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
