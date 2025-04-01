import json
from collections import Counter
from typing import List, Dict, Any

def load_dataset(file_path: str) -> Dict[str, Any]:
    """Loads a JSON dataset from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def majority_vote(values: List[Any]) -> Any:
    """Performs majority voting on a list of values."""
    if len(values) == 0:
        return None  # Handle empty list case
    counter = Counter(values)
    most_common, count = counter.most_common(1)[0]
    return most_common

def is_valid(value: Any, all_versions: List[Any]) -> bool:
    """Check if the value is valid (non-empty and consistent across all versions)."""
    # If the value is empty, it's invalid
    if not bool(value):
        return False
    
    # Check if the value is consistent across all versions (e.g., descriptions, types, properties)
    return all(v == value for v in all_versions)

def natural_sort_key(node_id):
    """Helper function to sort node IDs naturally, handling both strings and numbers."""
    if str(node_id).isdigit():
        return (0, int(node_id))  # Numbers come first
    elif node_id == "start":
        return (-1, node_id)  # Start comes before numbers
    elif node_id == "finish":
        return (2, node_id)  # Finish comes after numbers
    else:
        return (1, str(node_id))  # Other strings come between numbers and finish

def compare_procedures(datasets: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Compares multiple versions of the procedure and performs majority voting."""
    results = {
        "nodes": [],
        "edges": []
    }

    # Extract all node IDs across datasets
    node_ids = set()
    for dataset in datasets:
        if dataset and "graph" in dataset and "nodes" in dataset["graph"]:
            node_ids.update(str(node["id"]) for node in dataset["graph"]["nodes"])

    # Process nodes using majority voting
    for node_id in sorted(node_ids, key=natural_sort_key):
        node_data = {
            "id": node_id,
            "descriptions": [],
            "types": [],
            "properties": []
        }

        for dataset in datasets:
            if dataset and "graph" in dataset and "nodes" in dataset["graph"]:
                for node in dataset["graph"]["nodes"]:
                    if str(node["id"]) == node_id:
                        node_data["descriptions"].append(node.get("description", ""))
                        node_data["types"].append(node.get("type", ""))
                        node_data["properties"].append(str(node.get("properties", {})))

        # Apply majority voting
        description_majority = majority_vote(node_data["descriptions"])
        type_majority = majority_vote(node_data["types"])
        properties_majority = majority_vote(node_data["properties"])

        # Validate data consistency
        is_node_valid = (
            is_valid(description_majority, node_data["descriptions"]) and
            is_valid(type_majority, node_data["types"]) and
            is_valid(properties_majority, node_data["properties"])
        )

        results["nodes"].append({
            "id": node_id,
            "description_majority": description_majority,
            "type_majority": type_majority,
            "properties_majority": properties_majority,
            "valid": is_node_valid,
            "all_versions": node_data
        })

    # Extract all unique edges across datasets
    edge_signatures = set()  # Store edges uniquely based on (source, target, type)
    
    for dataset in datasets:
        if dataset and "graph" in dataset and "edges" in dataset["graph"]:
            for edge in dataset["graph"]["edges"]:
                from_node = str(edge["from"])
                to_node = str(edge["to"])
                edge_type = edge.get("type", "unknown")
                edge_signatures.add((from_node, to_node, edge_type))

    # Process edges using majority voting
    for from_node, to_node, edge_type in sorted(edge_signatures):
        edge_data = {
            "from": [],
            "to": [],
            "type": [],
            "properties": []
        }

        for dataset in datasets:
            if dataset and "graph" in dataset and "edges" in dataset["graph"]:
                for edge in dataset["graph"]["edges"]:
                    if str(edge["from"]) == from_node and str(edge["to"]) == to_node:
                        edge_data["from"].append(edge["from"])
                        edge_data["to"].append(edge["to"])
                        edge_data["type"].append(edge.get("type", "unknown"))
                        edge_data["properties"].append(str(edge.get("properties", {})))

        # Apply majority voting for edges
        from_majority = majority_vote(edge_data["from"])
        to_majority = majority_vote(edge_data["to"])
        type_majority = majority_vote(edge_data["type"])
        properties_majority = majority_vote(edge_data["properties"])

        # Validate edge consistency
        is_edge_valid = (
            is_valid(from_majority, edge_data["from"]) and
            is_valid(to_majority, edge_data["to"]) and
            is_valid(type_majority, edge_data["type"]) and
            is_valid(properties_majority, edge_data["properties"])
        )

        results["edges"].append({
            "from": from_majority,
            "to": to_majority,
            "type": type_majority,
            "properties": properties_majority,
            "valid": is_edge_valid,
            "all_versions": edge_data
        })

    return results


def save_results(results: Dict[str, Any], output_path: str):
    """Saves the comparison results to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    # Load datasets (v1p1, v2p1, v3p1)
    v1p3_file = "../../data/version_1/step3.json"
    v2p3_file = "../../data/version_2/step3-v2.json"
    v3p3_file = "../../data/version_3/step3-v3.json"
    
    print("Loading datasets...")
    v1p3 = load_dataset(v1p3_file)
    v2p3 = load_dataset(v2p3_file)
    v3p3 = load_dataset(v3p3_file)

    print("Comparing procedures using majority voting...")
    comparison_results = compare_procedures([v1p3, v2p3, v3p3])
    
    output_file = "../../src/accuracy/majority_comparison_results.json"
    save_results(comparison_results, output_file)
