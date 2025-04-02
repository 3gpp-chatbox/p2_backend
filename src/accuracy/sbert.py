import json 
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# This function reads a JSON file from the specified path and returns it as a dictionary.
def load_dataset(file_path: str) -> Dict[str, Any]:
    """Loads a JSON dataset from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_node_descriptions(dataset: Dict[str, Any], dataset_name: str) -> List[Dict[str, Any]]:
    """Extracts node descriptions and additional metadata for better matching then returns a list of dictionaries."""
    nodes = []
    if dataset and "graph" in dataset and "nodes" in dataset["graph"]:
        for node in dataset["graph"]["nodes"]:
            description = node.get("description", "")
            metadata = ""  # Combine additional metadata if available
            if "type" in node:
                metadata += f" Type: {node['type']}"
            if "properties" in node:
                metadata += f" Properties: {node['properties']}"
            
            nodes.append({
                "id": node["id"],
                "description": description + metadata,
                "dataset": dataset_name
            })
    return nodes

def compute_sbert_embeddings(descriptions: List[str]) -> np.ndarray:
    """Computes SBERT embeddings for the given descriptions then returns a numpy array."""
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(descriptions, convert_to_tensor=True)
    return embeddings.cpu().numpy()

def find_best_matches(node_set_1: List[Dict[str, Any]], node_set_2: List[Dict[str, Any]], fixed_threshold: float = 0.7) -> List[Dict[str, Any]]:
    """Finds mutual best matches between two datasets with a fixed cosine similarity threshold and returns a list of dictionaries."""
    descriptions_1 = [node["description"] for node in node_set_1]
    descriptions_2 = [node["description"] for node in node_set_2]

    if not descriptions_1 or not descriptions_2:
        return []  # If any dataset is empty, return empty list

    embeddings_1 = compute_sbert_embeddings(descriptions_1)
    embeddings_2 = compute_sbert_embeddings(descriptions_2)
    
    similarity_matrix = cosine_similarity(embeddings_1, embeddings_2)
    
    matched_pairs = []
    for i, node_1 in enumerate(node_set_1):
        best_match_idx_1 = np.argmax(similarity_matrix[i])
        best_match_score_1 = float(similarity_matrix[i][best_match_idx_1])
        
        # Check if this match is mutual and if it passes the fixed threshold
        best_match_idx_2 = np.argmax(similarity_matrix[:, best_match_idx_1])
        if best_match_idx_2 == i and best_match_score_1 >= fixed_threshold:
            matched_pairs.append({
                "id_1": node_1["id"],
                "description_1": node_1["description"],
                "id_2": node_set_2[best_match_idx_1]["id"],
                "description_2": node_set_2[best_match_idx_1]["description"],
                "cosine_similarity": best_match_score_1,
                "valid": best_match_score_1 >= fixed_threshold
            })
    
    return matched_pairs


def compare_datasets(datasets: Dict[str, Any], fixed_threshold: float = 0.7) -> List[Dict[str, Any]]:
    """Compares node descriptions across multiple datasets."""
    nodes_v1 = extract_node_descriptions(datasets["v1"], "v1")
    nodes_v2 = extract_node_descriptions(datasets["v2"], "v2")
    nodes_v3 = extract_node_descriptions(datasets["v3"], "v3")
    nodes_v4 = extract_node_descriptions(datasets["v4"], "v4")

    print("Matching v1 to v2...")
    v1_to_v2 = find_best_matches(nodes_v1, nodes_v2, fixed_threshold)

    print("Matching v1 to v3...")
    v1_to_v3 = find_best_matches(nodes_v1, nodes_v3, fixed_threshold)

    print("Matching v1 to v4...")
    v1_to_v4 = find_best_matches(nodes_v1, nodes_v4, fixed_threshold)

    print("Matching v2 to v3...")
    v2_to_v3 = find_best_matches(nodes_v2, nodes_v3, fixed_threshold)
    
    print("Matching v2 to v4...")
    v2_to_v4 = find_best_matches(nodes_v2, nodes_v4, fixed_threshold)

    print("Matching v3 to v4...")
    v3_to_v4 = find_best_matches(nodes_v3, nodes_v4, fixed_threshold)

    return v1_to_v2 + v1_to_v3 + v1_to_v4 + v2_to_v3 + v2_to_v4 + v3_to_v4  # Combine results


def save_results(results: List[Dict[str, Any]], output_path: str):
    """Saves the comparison results to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    dataset_files = {
        "v1": "../../data/consolidated_step3/v01-step3.json",
        "v2": "../../data/consolidated_step3/v02-step3.json",
        "v3": "../../data/consolidated_step3/v03-step3.json",
        "v4": "../../data/consolidated_step3/v04-step3.json"
    }
    
    print("Loading datasets...")
    datasets = {name: load_dataset(path) for name, path in dataset_files.items()}

    print("Comparing node descriptions using SBERT...")
    comparison_results = compare_datasets(datasets)

    output_file = "../../src/accuracy/sbert_comparison_results.json"
    save_results(comparison_results, output_file)
