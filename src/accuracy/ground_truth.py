import json
from typing import Dict, List

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics.pairwise import cosine_similarity


# Function to load JSON data from a file
def load_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)


# Function to extract descriptions for nodes
def extract_node_descriptions(dataset: dict, version: str) -> List[Dict[str, str]]:
    node_descriptions = []
    for node in dataset.get("graph", {}).get("nodes", []):
        try:
            node_descriptions.append(
                {
                    "id": node["id"],
                    "type": node["type"],
                    "description": node["description"],
                }
            )
        except KeyError as e:
            print(f"Missing key {e} in node: {node}")
    return node_descriptions


# Function to extract descriptions for edges with a unique id
def extract_edge_descriptions(dataset: dict, version: str) -> List[Dict[str, str]]:
    edge_descriptions = []
    for edge in dataset.get("graph", {}).get("edges", []):
        try:
            edge_id = f"{edge['from']}_{edge['to']}_{edge['type']}"  # Generate a unique ID for each edge
            edge_descriptions.append(
                {
                    "id": edge_id,  # Add the generated unique ID
                    "from": edge["from"],
                    "to": edge["to"],
                    "type": edge["type"],
                    "description": edge["description"],
                }
            )
        except KeyError as e:
            print(f"Missing key {e} in edge: {edge}")
    return edge_descriptions


# Function to preprocess descriptions and calculate cosine similarity
def calculate_similarity(descriptions1: List[str], descriptions2: List[str]) -> float:
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(descriptions1 + descriptions2)
    similarity_matrix = cosine_similarity(
        tfidf_matrix[: len(descriptions1)], tfidf_matrix[len(descriptions1) :]
    )
    return np.mean(similarity_matrix)


# Function to compare two datasets and calculate precision, recall, F1 score
def compare_datasets(
    dataset1: dict, dataset2: dict, version1: str, version2: str
) -> Dict:
    nodes1 = extract_node_descriptions(dataset1, version1)
    nodes2 = extract_node_descriptions(dataset2, version2)
    edges1 = extract_edge_descriptions(dataset1, version1)
    edges2 = extract_edge_descriptions(dataset2, version2)

    # Extract descriptions for nodes and edges
    node_desc1 = [node["description"] for node in nodes1]
    node_desc2 = [node["description"] for node in nodes2]
    edge_desc1 = [edge["description"] for edge in edges1]
    edge_desc2 = [edge["description"] for edge in edges2]

    # Calculate cosine similarity for nodes and edges
    node_similarity = calculate_similarity(node_desc1, node_desc2)
    edge_similarity = calculate_similarity(edge_desc1, edge_desc2)

    # Calculate precision, recall, and F1 score based on matching nodes and edges
    precision, recall, f1_score, _ = precision_recall_fscore_support(
        [1] * len(nodes1)
        + [0] * len(nodes2),  # True labels (1 for matching nodes, 0 for others)
        [1] * len(nodes2) + [0] * len(nodes1),  # Predicted labels
        average="binary",
    )

    # Return the result for saving
    return {
        "version1": version1,
        "version2": version2,
        "node_similarity": node_similarity,
        "edge_similarity": edge_similarity,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score,
    }


# Function to compare multiple datasets pairwise against the ground truth (dataset1)
def compare_multiple_datasets(
    datasets: List[Dict], versions: List[str], ground_truth_version: str
) -> List[Dict]:
    results = []
    ground_truth = datasets[
        0
    ]  # Assuming the first dataset is the ground truth (dataset1)

    for i in range(1, len(datasets)):  # Start from the second dataset
        print(f"\nComparing {ground_truth_version} and {versions[i]}...\n")
        result = compare_datasets(
            ground_truth, datasets[i], ground_truth_version, versions[i]
        )
        results.append(result)

    return results


# Function to save results into a JSON file
def save_results_to_file(results: List[Dict], output_file: str) -> None:
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)


# Load multiple datasets (adjust file paths as needed)
datasets = [
    load_json("data/consolidated_output/run1_step4.json"),  # Dataset 1 (ground truth)
    load_json("data/consolidated_output/run2_step4.json"),  # Dataset 2
    load_json("data/consolidated_output/run3_step4.json"),  # Dataset 3
    load_json("data/consolidated_output/run5_step4.json"),  # Dataset 5
    # Add more datasets as needed...
]

# Define versions for each dataset
versions = ["v1", "v2", "v3", "v4", "v5"]

# Compare all datasets pairwise with dataset1 as the ground truth
results = compare_multiple_datasets(datasets, versions, "v1")

# Save results to ground_truth_results.json
save_results_to_file(results, "src/accuracy/ground_truth_results.json")
