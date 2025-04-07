import json
import os
from typing import Any, Dict, List

from sbert_descriptions import (
    extract_edge_descriptions,
    extract_node_descriptions,
    find_best_edge_matches,
    find_best_matches,
    load_dataset,
)


def calculate_metrics(
    true_ids: List[str], predicted_ids: List[str]
) -> Dict[str, float]:
    """
    Calculates precision, recall, and F1 score based on intersection of IDs.
    """
    true_set = set(true_ids)
    predicted_set = set(predicted_ids)

    true_positives = len(true_set & predicted_set)
    false_positives = len(predicted_set - true_set)
    false_negatives = len(true_set - predicted_set)

    precision = (
        true_positives / (true_positives + false_positives)
        if (true_positives + false_positives) > 0
        else 0.0
    )
    recall = (
        true_positives / (true_positives + false_negatives)
        if (true_positives + false_negatives) > 0
        else 0.0
    )
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )

    return {"precision": precision, "recall": recall, "f1_score": f1}


def determine_validity_with_explanation(
    node_metrics: Dict[str, float],
    edge_metrics: Dict[str, float],
    unmatched_nodes: List[Any],
    unmatched_edges: List[Any],
    total_nodes: int,
    total_edges: int,
    max_unmatched_threshold: float = 0.05,
) -> Dict[str, Any]:
    node_precision = node_metrics["precision"]
    node_recall = node_metrics["recall"]
    node_f1 = node_metrics["f1_score"]

    edge_precision = edge_metrics["precision"]
    edge_recall = edge_metrics["recall"]
    edge_f1 = edge_metrics["f1_score"]

    unmatched_node_ratio = (
        len(unmatched_nodes) / total_nodes if total_nodes > 0 else 1.0
    )
    unmatched_edge_ratio = (
        len(unmatched_edges) / total_edges if total_edges > 0 else 1.0
    )

    metrics_valid = (
        node_precision >= 0.9
        and node_recall >= 0.9
        and node_f1 >= 0.9
        and edge_precision >= 0.9
        and edge_recall >= 0.9
        and edge_f1 >= 0.9
    )

    unmatched_valid = (
        unmatched_node_ratio <= max_unmatched_threshold
        and unmatched_edge_ratio <= max_unmatched_threshold
    )

    explanation = []

    if metrics_valid and not unmatched_valid:
        explanation.append("Metrics are high (>0.9) but unmatched ratios are elevated.")
        if unmatched_node_ratio > max_unmatched_threshold:
            explanation.append(f"Unmatched node ratio: {unmatched_node_ratio:.2%}")
        if unmatched_edge_ratio > max_unmatched_threshold:
            explanation.append(f"Unmatched edge ratio: {unmatched_edge_ratio:.2%}")
    elif not metrics_valid:
        explanation.append("One or more metrics are below the threshold of 0.9.")
        if unmatched_node_ratio > max_unmatched_threshold:
            explanation.append(f"Unmatched node ratio: {unmatched_node_ratio:.2%}")
        if unmatched_edge_ratio > max_unmatched_threshold:
            explanation.append(f"Unmatched edge ratio: {unmatched_edge_ratio:.2%}")
    else:
        explanation.append("All conditions met.")

    return {
        "validity": "valid" if metrics_valid and unmatched_valid else "invalid",
        "explanation": explanation,
    }


def compare_datasets_with_ground_truth_and_metrics(
    datasets: Dict[str, Any], fixed_threshold: float = 0.7
) -> Dict[str, Any]:
    try:
        nodes_v1 = extract_node_descriptions(datasets["v1"], "v1")
        edges_v1 = extract_edge_descriptions(datasets["v1"], "v1")
        total_nodes = len(nodes_v1)
        total_edges = len(edges_v1)

        results = {}

        for version in ["v2", "v3", "v4"]:
            print(f"Matching {version} to v1 (nodes)...")
            matched_nodes = find_best_matches(
                extract_node_descriptions(datasets[version], version),
                nodes_v1,
                fixed_threshold,
            )
            print(f"Matching {version} to v1 (edges)...")
            matched_edges = find_best_edge_matches(
                extract_edge_descriptions(datasets[version], version),
                edges_v1,
                fixed_threshold,
            )

            node_metrics = calculate_metrics(
                [node["id"] for node in nodes_v1],
                [match["id_2"] for match in matched_nodes["matches"]],
            )
            edge_metrics = calculate_metrics(
                [edge["id"] for edge in edges_v1],
                [match["id_2"] for match in matched_edges["matches"]],
            )

            results[version] = {
                "node_metrics": node_metrics,
                "edge_metrics": edge_metrics,
                "validity": determine_validity_with_explanation(
                    node_metrics,
                    edge_metrics,
                    matched_nodes["unmatched"],
                    matched_edges["unmatched"],
                    total_nodes,
                    total_edges,
                ),
            }

        return results
    except Exception as e:
        print(f"Error in comparison: {e}")
        return {}


def save_results_with_metrics(results: Dict[str, Any], output_path: str):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
        print(f"Results saved to {output_path}")
    except Exception as e:
        print(f"Error saving results: {e}")


if __name__ == "__main__":
    try:
        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        data_dir = os.path.join(base_dir, "data")
        output_dir = os.path.join(base_dir, "output")

        dataset_files = {
            "v1": os.path.join(data_dir, "version_1", "step3.json"),
            "v2": os.path.join(data_dir, "version_2", "v02-step3.json"),
            "v3": os.path.join(data_dir, "version_3", "step3-v3.json"),
            "v4": os.path.join(data_dir, "version_4", "step3-v4.json"),
        }

        for version, file_path in dataset_files.items():
            if not os.path.exists(file_path):
                raise FileNotFoundError(
                    f"Input file for {version} not found: {file_path}"
                )

        datasets = {key: load_dataset(file) for key, file in dataset_files.items()}
        results = compare_datasets_with_ground_truth_and_metrics(datasets)

        output_path = os.path.join(
            "src/accuracy/ground_truth_comparison_with_metrics.json"
        )
        save_results_with_metrics(results, output_path)

    except Exception as e:
        print(f"Error running script: {e}")
