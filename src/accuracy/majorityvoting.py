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


def compare_procedures(datasets: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Compares multiple versions of the procedure and performs majority voting."""
    results = {
        "nodes": [],
        "edges": []
    }

    # Get all node IDs across datasets and convert to strings
    node_ids = set()
    for dataset in datasets:
        if dataset and "graph" in dataset and "nodes" in dataset["graph"]:
            node_ids.update(str(node["id"]) for node in dataset["graph"]["nodes"])

    # Compare nodes
    for node_id in sorted(node_ids, key=lambda x: int(x) if str(x).isdigit() else x):
        node_data = {
            "id": node_id,
            "descriptions": [],
            "types": [],
            "properties": []
        }
        
        for dataset in datasets:
            if dataset and "graph" in dataset and "nodes" in dataset["graph"]:
                for node in dataset["graph"]["nodes"]:
                    # Convert node id to string for comparison
                    if str(node["id"]) == node_id:
                        node_data["descriptions"].append(node.get("description", ""))
                        node_data["types"].append(node.get("type", ""))
                        node_data["properties"].append(str(node.get("properties", {})))

        # Apply majority voting for each field
        description_majority = majority_vote(node_data["descriptions"])
        type_majority = majority_vote(node_data["types"])
        properties_majority = majority_vote(node_data["properties"])

        # Validate if the extracted data is valid (considering consistency)
        is_node_valid_description = is_valid(description_majority, node_data["descriptions"])
        is_node_valid_type = is_valid(type_majority, node_data["types"])
        is_node_valid_properties = is_valid(properties_majority, node_data["properties"])

        # Combine validity checks for description, type, and properties
        is_node_valid = is_node_valid_description and is_node_valid_type and is_node_valid_properties

        # Add results for this node
        results["nodes"].append({
            "id": node_id,
            "description_majority": description_majority,
            "type_majority": type_majority,
            "properties_majority": properties_majority,
            "valid": is_node_valid,
            "all_versions": node_data
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
