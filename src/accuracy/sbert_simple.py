import json
import os
from typing import Any, Dict, List

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load JSON dataset
def load_dataset(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Extract node descriptions
def extract_node_descriptions(
    dataset: Dict[str, Any], dataset_name: str
) -> List[Dict[str, Any]]:
    nodes = []
    if dataset and "graph" in dataset and "nodes" in dataset["graph"]:
        for node in dataset["graph"]["nodes"]:
            description = node.get("description", "")
            metadata = ""
            if "type" in node:
                metadata += f" Type: {node['type']}"
            if "properties" in node:
                metadata += f" Properties: {node['properties']}"

            nodes.append(
                {
                    "id": node["id"],
                    "description": description + metadata,
                    "dataset": dataset_name,
                }
            )
    return nodes


# Extract edge descriptions
def extract_edge_descriptions(
    dataset: Dict[str, Any], dataset_name: str
) -> List[Dict[str, Any]]:
    edges = []
    if dataset and "graph" in dataset and "edges" in dataset["graph"]:
        for edge in dataset["graph"]["edges"]:
            description = edge.get("description", "")
            metadata = ""
            if "type" in edge:
                metadata += f" Type: {edge['type']}"
            if "properties" in edge:
                metadata += f" Properties: {edge['properties']}"

            edge_id = f"{edge['from']}->{edge['to']}"

            edges.append(
                {
                    "id": edge_id,
                    "description": description + metadata,
                    "dataset": dataset_name,
                }
            )
    return edges


# Compute SBERT embeddings
def compute_sbert_embeddings(descriptions: List[str]) -> np.ndarray:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(descriptions, convert_to_tensor=True)
    return embeddings.cpu().numpy()


# Find best matches
def find_best_matches(
    node_set_1: List[Dict[str, Any]],
    node_set_2: List[Dict[str, Any]],
    fixed_threshold: float = 0.5,
) -> Dict[str, Any]:
    descriptions_1 = [node["description"] for node in node_set_1]
    descriptions_2 = [node["description"] for node in node_set_2]

    embeddings_1 = compute_sbert_embeddings(descriptions_1)
    embeddings_2 = compute_sbert_embeddings(descriptions_2)

    similarity_matrix = cosine_similarity(embeddings_1, embeddings_2)

    matched_pairs = []
    unmatched_nodes = []

    for i, node_1 in enumerate(node_set_1):
        best_match_idx_1 = np.argmax(similarity_matrix[i])
        best_match_score_1 = float(similarity_matrix[i][best_match_idx_1])

        best_match_idx_2 = np.argmax(similarity_matrix[:, best_match_idx_1])
        if best_match_idx_2 == i and best_match_score_1 >= fixed_threshold:
            matched_pairs.append(
                {
                    "id_1": node_1["id"],
                    "description_1": node_1["description"],
                    "id_2": node_set_2[best_match_idx_1]["id"],
                    "description_2": node_set_2[best_match_idx_1]["description"],
                    "cosine_similarity": best_match_score_1,
                    "valid": True,
                }
            )
        else:
            unmatched_nodes.append(node_1)

    return {"matches": matched_pairs, "unmatched": unmatched_nodes}


def find_best_edge_matches(
    edge_set_1: List[Dict[str, Any]],
    edge_set_2: List[Dict[str, Any]],
    fixed_threshold: float = 0.7,
) -> Dict[str, Any]:
    descriptions_1 = [edge["description"] for edge in edge_set_1]
    descriptions_2 = [edge["description"] for edge in edge_set_2]

    embeddings_1 = compute_sbert_embeddings(descriptions_1)
    embeddings_2 = compute_sbert_embeddings(descriptions_2)

    similarity_matrix = cosine_similarity(embeddings_1, embeddings_2)

    matched_pairs = []
    unmatched_edges = []

    for i, edge_1 in enumerate(edge_set_1):
        best_match_idx_1 = np.argmax(similarity_matrix[i])
        best_match_score_1 = float(similarity_matrix[i][best_match_idx_1])

        best_match_idx_2 = np.argmax(similarity_matrix[:, best_match_idx_1])
        if best_match_idx_2 == i and best_match_score_1 >= fixed_threshold:
            matched_pairs.append(
                {
                    "id_1": edge_1["id"],
                    "description_1": edge_1["description"],
                    "id_2": edge_set_2[best_match_idx_1]["id"],
                    "description_2": edge_set_2[best_match_idx_1]["description"],
                    "cosine_similarity": best_match_score_1,
                    "valid": True,
                }
            )
        else:
            unmatched_edges.append(edge_1)

    return {"matches": matched_pairs, "unmatched": unmatched_edges}


def compare_two_datasets(
    dataset_1: Dict[str, Any], dataset_2: Dict[str, Any], fixed_threshold: float = 0.7
) -> Dict[str, Any]:
    nodes_1 = extract_node_descriptions(dataset_1, "Dataset 1")
    nodes_2 = extract_node_descriptions(dataset_2, "Dataset 2")

    edges_1 = extract_edge_descriptions(dataset_1, "Dataset 1")
    edges_2 = extract_edge_descriptions(dataset_2, "Dataset 2")

    v1_to_v2_nodes = find_best_matches(nodes_1, nodes_2, fixed_threshold)
    v1_to_v2_edges = find_best_edge_matches(edges_1, edges_2, fixed_threshold)

    node_matches = v1_to_v2_nodes["matches"]
    edge_matches = v1_to_v2_edges["matches"]

    unmatched_nodes = v1_to_v2_nodes["unmatched"]
    unmatched_edges = v1_to_v2_edges["unmatched"]

    validity = (
        "valid" if len(unmatched_nodes) + len(unmatched_edges) == 0 else "invalid"
    )

    total_node_matches = len(node_matches)
    total_edge_matches = len(edge_matches)
    total_unmatched_nodes = len(unmatched_nodes)
    total_unmatched_edges = len(unmatched_edges)
    total_nodes = total_node_matches + total_unmatched_nodes
    total_edges = total_edge_matches + total_unmatched_edges

    summary = {
        "validity_status": validity,
        "validation_reason": "There are unmatched nodes or edges"
        if validity == "invalid"
        else "All nodes and edges are matched",
        "node_stats": {
            "total": total_nodes,
            "matched": total_node_matches,
            "unmatched": total_unmatched_nodes,
            "match_percentage": (total_node_matches / total_nodes * 100)
            if total_nodes > 0
            else 0,
        },
        "edge_stats": {
            "total": total_edges,
            "matched": total_edge_matches,
            "unmatched": total_unmatched_edges,
            "match_percentage": (total_edge_matches / total_edges * 100)
            if total_edges > 0
            else 0,
        },
    }

    return {
        "summary": summary,
        "node_matches": node_matches,
        "edge_matches": edge_matches,
        "unmatched_nodes": unmatched_nodes,
        "unmatched_edges": unmatched_edges,
    }


# Save results with formatted output
def save_results(results: Dict[str, Any], output_path: str):
    summary = results["summary"]
    print("\n=== VALIDATION SUMMARY ===")
    print(f"Status: {summary['validity_status'].upper()}")
    print(f"Reason: {summary['validation_reason']}")

    print("\nNode Statistics:")
    print(f"Total Nodes: {summary['node_stats']['total']}")
    print(
        f"Matched Nodes: {summary['node_stats']['matched']} ({summary['node_stats']['match_percentage']:.2f}%)"
    )
    print(f"Unmatched Nodes: {summary['node_stats']['unmatched']}")

    print("\nEdge Statistics:")
    print(f"Total Edges: {summary['edge_stats']['total']}")
    print(
        f"Matched Edges: {summary['edge_stats']['matched']} ({summary['edge_stats']['match_percentage']:.2f}%)"
    )
    print(f"Unmatched Edges: {summary['edge_stats']['unmatched']}")
    print("=======================\n")

    # Save detailed results to file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Detailed results saved to {output_path}")


if __name__ == "__main__":
    # Use absolute paths
    data_dir = "data"
    dataset_files = {
        "v1": os.path.join(data_dir, "version_1/step3.json"),
        "v2": os.path.join(data_dir, "version_2/v02-step3.json"),
    }

    # Load the datasets
    datasets = {key: load_dataset(file) for key, file in dataset_files.items()}

    # Compare datasets
    results = compare_two_datasets(datasets["v1"], datasets["v2"])

    # Save the results
    save_results(results, "src/accuracy/sbert_simple.json")
