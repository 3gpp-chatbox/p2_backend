import json
import os
from typing import Any, Dict, List

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def load_dataset(file_path: str) -> Dict[str, Any]:
    """Loads a JSON dataset from the specified file path.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        Dict[str, Any]: Parsed JSON content as a dictionary.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_node_descriptions(
    dataset: Dict[str, Any], dataset_name: str
) -> List[Dict[str, Any]]:
    """Extracts and formats node descriptions from the dataset.

    Args:
        dataset (Dict[str, Any]): The JSON dataset containing graph nodes.
        dataset_name (str): Name/identifier for the dataset.

    Returns:
        List[Dict[str, Any]]: List of dictionaries with node ID, full description, and dataset name.
    """
    nodes = []
    if dataset and "graph" in dataset and "nodes" in dataset["graph"]:
        for node in dataset["graph"]["nodes"]:
            node_id = node.get("id", "")
            node_type = node.get("type", "")
            description = node.get("description", "")
            properties = json.dumps(node.get("properties", {}), ensure_ascii=False)

            full_text = f"ID: {node_id}. Type: {node_type}. Description: {description}. Properties: {properties}"

            nodes.append(
                {
                    "id": node_id,
                    "description": full_text,
                    "dataset": dataset_name,
                }
            )
    return nodes


def extract_edge_descriptions(
    dataset: Dict[str, Any], dataset_name: str
) -> List[Dict[str, Any]]:
    """Extracts and formats edge descriptions from the dataset.

    Args:
        dataset (Dict[str, Any]): The JSON dataset containing graph edges.
        dataset_name (str): Name/identifier for the dataset.

    Returns:
        List[Dict[str, Any]]: List of dictionaries with edge ID, full description, and dataset name.
    """
    edges = []
    if dataset and "graph" in dataset and "edges" in dataset["graph"]:
        for edge in dataset["graph"]["edges"]:
            from_node = edge.get("from", "")
            to_node = edge.get("to", "")
            edge_type = edge.get("type", "")
            description = edge.get("description", "")

            edge_id = f"{from_node}->{to_node}"
            full_text = f"From: {from_node}. To: {to_node}. Type: {edge_type}. Description: {description}."

            edges.append(
                {
                    "id": edge_id,
                    "description": full_text,
                    "dataset": dataset_name,
                }
            )
    return edges


def compute_sbert_embeddings(
    descriptions: List[str], model: SentenceTransformer
) -> np.ndarray:
    """Computes SBERT embeddings for a list of text descriptions.

    Args:
        descriptions (List[str]): List of string descriptions to embed.

    Returns:
        np.ndarray: Array of SBERT embeddings.
    """
    embeddings = model.encode(descriptions, convert_to_tensor=True)
    return embeddings.cpu().numpy()


def find_best_matches(
    set_1: List[Dict[str, Any]],
    set_2: List[Dict[str, Any]],
    fixed_threshold: float = 0.8,
) -> Dict[str, Any]:
    """Finds the best semantic matches between two sets of graph items using SBERT and cosine similarity.

    Args:
        set_1 (List[Dict[str, Any]]): First list of graph items (nodes or edges).
        set_2 (List[Dict[str, Any]]): Second list of graph items.
        fixed_threshold (float): Minimum cosine similarity to consider a match as valid. Defaults to 0.8.

    Returns:
        Dict[str, Any]: Dictionary containing matched pairs and unmatched items.
    """
    descriptions_1 = [item["description"] for item in set_1]
    descriptions_2 = [item["description"] for item in set_2]

    # Define model outside the function to avoid reloading it every time
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings_1 = compute_sbert_embeddings(descriptions_1, model=model)
    embeddings_2 = compute_sbert_embeddings(descriptions_2, model=model)

    similarity_matrix = cosine_similarity(embeddings_1, embeddings_2)

    matched_pairs = []
    unmatched = []

    for i, item_1 in enumerate(set_1):
        best_match_idx_1 = np.argmax(similarity_matrix[i])
        best_match_score_1 = float(similarity_matrix[i][best_match_idx_1])

        best_match_idx_2 = np.argmax(similarity_matrix[:, best_match_idx_1])
        if best_match_idx_2 == i and best_match_score_1 >= fixed_threshold:
            matched_pairs.append(
                {
                    "id_1": item_1["id"],
                    "description_1": item_1["description"],
                    "id_2": set_2[best_match_idx_1]["id"],
                    "description_2": set_2[best_match_idx_1]["description"],
                    "cosine_similarity": best_match_score_1,
                    "valid": True,
                }
            )
        else:
            unmatched.append(item_1)

    return {"matches": matched_pairs, "unmatched": unmatched}


def compare_two_datasets(
    dataset_1: Dict[str, Any],
    dataset_2: Dict[str, Any],
    dataset_1_name: str,
    dataset_2_name: str,
    fixed_threshold: float = 0.8,
) -> Dict[str, Any]:
    """Compares two datasets by matching their nodes and edges based on semantic similarity.

    Args:
        dataset_1 (Dict[str, Any]): First dataset.
        dataset_2 (Dict[str, Any]): Second dataset.
        dataset_1_name (str): Name of the first dataset.
        dataset_2_name (str): Name of the second dataset.
        fixed_threshold (float): Minimum similarity score to consider a match valid.

    Returns:
        Dict[str, Any]: Dictionary containing summary statistics, matches, and unmatched items.
    """
    nodes_1 = extract_node_descriptions(dataset_1, dataset_1_name)
    nodes_2 = extract_node_descriptions(dataset_2, dataset_2_name)

    edges_1 = extract_edge_descriptions(dataset_1, dataset_1_name)
    edges_2 = extract_edge_descriptions(dataset_2, dataset_2_name)

    node_results = find_best_matches(nodes_1, nodes_2, fixed_threshold)
    edge_results = find_best_matches(edges_1, edges_2, fixed_threshold)

    node_matches = node_results["matches"]
    edge_matches = edge_results["matches"]
    unmatched_nodes = node_results["unmatched"]
    unmatched_edges = edge_results["unmatched"]

    total_node_matches = len(node_matches)
    total_edge_matches = len(edge_matches)
    total_unmatched_nodes = len(unmatched_nodes)
    total_unmatched_edges = len(unmatched_edges)
    total_nodes = total_node_matches + total_unmatched_nodes
    total_edges = total_edge_matches + total_unmatched_edges

    node_match_percent = (
        (total_node_matches / total_nodes * 100) if total_nodes > 0 else 0
    )
    edge_match_percent = (
        (total_edge_matches / total_edges * 100) if total_edges > 0 else 0
    )

    overall_similarity = (
        ((total_node_matches + total_edge_matches) / (total_nodes + total_edges) * 100)
        if (total_nodes + total_edges) > 0
        else 0
    )

    validity = (
        "valid"
        if node_match_percent >= 80 and edge_match_percent >= 80
        else "invalid (min 80%)"
    )

    summary = {
        "validity_status": validity,
        "validation_reason": "At least 80% of nodes and edges matched"
        if validity == "valid"
        else "There are less than 80% matched nodes or edges",
        "dataset_comparing": f"Comparing {dataset_1_name} and {dataset_2_name}",
        "node_stats": {
            "total": total_nodes,
            "matched": total_node_matches,
            "unmatched": total_unmatched_nodes,
            "match_percentage": node_match_percent,
        },
        "edge_stats": {
            "total": total_edges,
            "matched": total_edge_matches,
            "unmatched": total_unmatched_edges,
            "match_percentage": edge_match_percent,
        },
        "overall_match_percentage": overall_similarity,
    }

    return {
        "summary": summary,
        "node_matches": node_matches,
        "edge_matches": edge_matches,
        "unmatched_nodes": unmatched_nodes,
        "unmatched_edges": unmatched_edges,
    }


def save_results(results: Dict[str, Any], output_path: str):
    """Prints a summary of validation results and saves the full results to a JSON file.

    Args:
        results (Dict[str, Any]): Result dictionary from the dataset comparison.
        output_path (str): Path to save the results JSON file.
    """
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

    print("\nOverall Similarity:")
    print(f"Overall Match Percentage: {summary['overall_match_percentage']:.2f}%")

    print("=======================\n")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Detailed results saved to {output_path}")


if __name__ == "__main__":
    data_dir = "data"
    dataset_files = {
        "v1": os.path.join(data_dir, "consolidated_output/run1_step4.json"),
        "v2": os.path.join(data_dir, "consolidated_output/run5_step4.json"),
    }

    datasets = {key: load_dataset(path) for key, path in dataset_files.items()}

    results = compare_two_datasets(
        datasets["v1"], datasets["v2"], "Dataset 1", "Dataset 2"
    )

    save_results(results, "src/accuracy/sbert_simple.json")
