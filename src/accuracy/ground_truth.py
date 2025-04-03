from sklearn.metrics import precision_score, recall_score, f1_score
from typing import List, Dict, Any
import json
import os
from sbert_descriptions import (
    extract_node_descriptions,
    extract_edge_descriptions,
    find_best_matches,
    find_best_edge_matches,
    load_dataset
)


# Function to calculate Precision, Recall, F1 Score for node matches
def calculate_metrics(true_matches: List[str], predicted_matches: List[str]) -> Dict[str, float]:
    if not predicted_matches:  # Handle empty predictions
        return {"precision": 0.0, "recall": 0.0, "f1_score": 0.0}
        
    true_labels = [1 if match in true_matches else 0 for match in predicted_matches]
    predicted_labels = [1] * len(predicted_matches)  # All predictions are considered matches
    
    try:
        precision = precision_score(true_labels, predicted_labels)
        recall = recall_score(true_labels, predicted_labels)
        f1 = f1_score(true_labels, predicted_labels)
    except Exception as e:
        print(f"Warning: Error calculating metrics: {e}")
        return {"precision": 0.0, "recall": 0.0, "f1_score": 0.0}

    return {"precision": precision, "recall": recall, "f1_score": f1}

# Function to determine validity based on metrics and unmatched nodes/edges with explanation
def determine_validity_with_explanation(node_metrics: Dict[str, float], edge_metrics: Dict[str, float], 
                                         unmatched_nodes: List[Any], unmatched_edges: List[Any], 
                                         total_nodes: int, total_edges: int,
                                         max_unmatched_threshold: float = 0.05) -> Dict[str, Any]:
    # Get metrics
    node_precision = node_metrics["precision"]
    node_recall = node_metrics["recall"]
    node_f1 = node_metrics["f1_score"]
    
    edge_precision = edge_metrics["precision"]
    edge_recall = edge_metrics["recall"]
    edge_f1 = edge_metrics["f1_score"]

    # Calculate unmatched ratios
    unmatched_node_ratio = len(unmatched_nodes) / total_nodes if total_nodes > 0 else 1.0
    unmatched_edge_ratio = len(unmatched_edges) / total_edges if total_edges > 0 else 1.0

    # Check if all metrics meet thresholds
    metrics_valid = (
        node_precision >= 0.9 and node_recall >= 0.9 and node_f1 >= 0.9 and
        edge_precision >= 0.9 and edge_recall >= 0.9 and edge_f1 >= 0.9
    )

    # Check if unmatched ratios are below threshold
    unmatched_valid = (
        unmatched_node_ratio <= max_unmatched_threshold and 
        unmatched_edge_ratio <= max_unmatched_threshold
    )

    # Create explanation
    explanation = []
    if not metrics_valid:
        explanation.append("One or more metrics (precision, recall, F1 score) are below the threshold of 0.9.")
    
    if not unmatched_valid:
        if unmatched_node_ratio > max_unmatched_threshold:
            explanation.append(f"Unmatched nodes exceed the threshold: {unmatched_node_ratio:.2f} > {max_unmatched_threshold}")
        if unmatched_edge_ratio > max_unmatched_threshold:
            explanation.append(f"Unmatched edges exceed the threshold: {unmatched_edge_ratio:.2f} > {max_unmatched_threshold}")

    return {
        "validity": "valid" if metrics_valid and unmatched_valid else "invalid",
        "explanation": explanation if explanation else ["All conditions met."]
    }

# Compare datasets with v1 as ground truth and calculate Precision, Recall, F1
def compare_datasets_with_ground_truth_and_metrics(datasets: Dict[str, Any], fixed_threshold: float = 0.7) -> Dict[str, Any]:
    try:
        nodes_v1 = extract_node_descriptions(datasets["v1"], "v1")
        edges_v1 = extract_edge_descriptions(datasets["v1"], "v1")
        
        # Extract nodes and edges from other versions
        nodes_v2 = extract_node_descriptions(datasets["v2"], "v2")
        nodes_v3 = extract_node_descriptions(datasets["v3"], "v3")
        nodes_v4 = extract_node_descriptions(datasets["v4"], "v4")
        
        edges_v2 = extract_edge_descriptions(datasets["v2"], "v2")
        edges_v3 = extract_edge_descriptions(datasets["v3"], "v3")
        edges_v4 = extract_edge_descriptions(datasets["v4"], "v4")

        # Store total counts
        total_nodes = len(nodes_v1)
        total_edges = len(edges_v1)

        results = {}

        # Compare v2 to v1 (nodes and edges)
        print("Matching v2 to v1 (nodes)...")
        v2_to_v1_nodes = find_best_matches(nodes_v2, nodes_v1, fixed_threshold)
        print("Matching v2 to v1 (edges)...")
        v2_to_v1_edges = find_best_edge_matches(edges_v2, edges_v1, fixed_threshold)

        # Calculate metrics for nodes and edges for v2
        node_metrics_v2 = calculate_metrics(
            [node["id"] for node in nodes_v1],
            [match["id_2"] for match in v2_to_v1_nodes["matches"]]
        )
        edge_metrics_v2 = calculate_metrics(
            [edge["id"] for edge in edges_v1],
            [match["id_2"] for match in v2_to_v1_edges["matches"]]
        )

        # Compare v3 to v1 (nodes and edges)
        print("Matching v3 to v1 (nodes)...")
        v3_to_v1_nodes = find_best_matches(nodes_v3, nodes_v1, fixed_threshold)
        print("Matching v3 to v1 (edges)...")
        v3_to_v1_edges = find_best_edge_matches(edges_v3, edges_v1, fixed_threshold)

        # Calculate metrics for nodes and edges for v3
        node_metrics_v3 = calculate_metrics(
            [node["id"] for node in nodes_v1],
            [match["id_2"] for match in v3_to_v1_nodes["matches"]]
        )
        edge_metrics_v3 = calculate_metrics(
            [edge["id"] for edge in edges_v1],
            [match["id_2"] for match in v3_to_v1_edges["matches"]]
        )

        # Compare v4 to v1 (nodes and edges)
        print("Matching v4 to v1 (nodes)...")
        v4_to_v1_nodes = find_best_matches(nodes_v4, nodes_v1, fixed_threshold)
        print("Matching v4 to v1 (edges)...")
        v4_to_v1_edges = find_best_edge_matches(edges_v4, edges_v1, fixed_threshold)

        # Calculate metrics for nodes and edges for v4
        node_metrics_v4 = calculate_metrics(
            [node["id"] for node in nodes_v1],
            [match["id_2"] for match in v4_to_v1_nodes["matches"]]
        )
        edge_metrics_v4 = calculate_metrics(
            [edge["id"] for edge in edges_v1],
            [match["id_2"] for match in v4_to_v1_edges["matches"]]
        )

        # Collect all metrics with new validity logic and explanation
        results["v2"] = {
            "node_metrics": node_metrics_v2,
            "edge_metrics": edge_metrics_v2,
            "validity": determine_validity_with_explanation(
                node_metrics_v2, edge_metrics_v2,
                v2_to_v1_nodes["unmatched"], v2_to_v1_edges["unmatched"],
                total_nodes, total_edges
            )
        }
        results["v3"] = {
            "node_metrics": node_metrics_v3,
            "edge_metrics": edge_metrics_v3,
            "validity": determine_validity_with_explanation(
                node_metrics_v3, edge_metrics_v3,
                v3_to_v1_nodes["unmatched"], v3_to_v1_edges["unmatched"],
                total_nodes, total_edges
            )
        }
        results["v4"] = {
            "node_metrics": node_metrics_v4,
            "edge_metrics": edge_metrics_v4,
            "validity": determine_validity_with_explanation(
                node_metrics_v4, edge_metrics_v4,
                v4_to_v1_nodes["unmatched"], v4_to_v1_edges["unmatched"],
                total_nodes, total_edges
            )
        }

        return results
    except Exception as e:
        print(f"Error in comparison: {e}")
        return {}

# Save the results
def save_results_with_metrics(results: Dict[str, Any], output_path: str):
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
        print(f"Results saved to {output_path}")
    except Exception as e:
        print(f"Error saving results: {e}")

if __name__ == "__main__":
    try:
        # Use absolute paths for reliability
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, "data")
        output_dir = os.path.join(base_dir, "output")
        
        dataset_files = {
            "v1": os.path.join(data_dir, "version_1", "step3.json"),
            "v2": os.path.join(data_dir, "version_2", "v02-step3.json"),
            "v3": os.path.join(data_dir, "version_3", "step3-v3.json"),
            "v4": os.path.join(data_dir, "version_4", "step3-v4.json"),
        }

        # Verify all input files exist
        for version, file_path in dataset_files.items():
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Input file for {version} not found: {file_path}")

        datasets = {key: load_dataset(file) for key, file in dataset_files.items()}

        # Compare datasets and calculate metrics
        results = compare_datasets_with_ground_truth_and_metrics(datasets)

        # Save results with metrics
        output_path = os.path.join("src/accuracy/ground_truth_comparison_with_metrics.json")
        save_results_with_metrics(results, output_path)
        
    except Exception as e:
        print(f"Error running script: {e}")
