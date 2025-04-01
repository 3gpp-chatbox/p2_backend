import json
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_dataset(file_path: str) -> Dict[str, Any]:
    """Loads a JSON dataset from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_node_descriptions(dataset: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extracts node descriptions and additional metadata for better matching."""
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
                "description": description + metadata
            })
    return nodes

def compute_sbert_embeddings(descriptions: List[str]) -> np.ndarray:
    """Computes SBERT embeddings for the given descriptions."""
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(descriptions, convert_to_tensor=True)
    return embeddings.cpu().numpy()

def find_best_matches(node_set_1: List[Dict[str, Any]], node_set_2: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Finds mutual best matches between two datasets with adaptive thresholding."""
    descriptions_1 = [node["description"] for node in node_set_1]
    descriptions_2 = [node["description"] for node in node_set_2]

    if not descriptions_1 or not descriptions_2:
        return []  # If any dataset is empty, return empty list

    embeddings_1 = compute_sbert_embeddings(descriptions_1)
    embeddings_2 = compute_sbert_embeddings(descriptions_2)
    
    similarity_matrix = cosine_similarity(embeddings_1, embeddings_2)
    
    # Compute adaptive threshold using 90th percentile
    adaptive_threshold = np.percentile(similarity_matrix, 90)
    
    matched_pairs = []
    for i, node_1 in enumerate(node_set_1):
        best_match_idx_1 = np.argmax(similarity_matrix[i])
        best_match_score_1 = float(similarity_matrix[i][best_match_idx_1])
        
        # Check if this match is mutual
        best_match_idx_2 = np.argmax(similarity_matrix[:, best_match_idx_1])
        if best_match_idx_2 == i and best_match_score_1 >= adaptive_threshold:
            matched_pairs.append({
                "id_1": node_1["id"],
                "description_1": node_1["description"],
                "id_2": node_set_2[best_match_idx_1]["id"],
                "description_2": node_set_2[best_match_idx_1]["description"],
                "cosine_similarity": best_match_score_1,
                "valid": True
            })
    
    return matched_pairs

def compare_datasets(datasets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Compares node descriptions across multiple datasets."""
    nodes_v1 = extract_node_descriptions(datasets[0])
    nodes_v2 = extract_node_descriptions(datasets[1])
    nodes_v3 = extract_node_descriptions(datasets[2])
    nodes_v4 = extract_node_descriptions(datasets[3])

    print("Matching v1 to v2...")
    v1_to_v2 = find_best_matches(nodes_v1, nodes_v2)

    print("Matching v2 to v3...")
    v2_to_v3 = find_best_matches(nodes_v2, nodes_v3)
    
    print("Matching v3 to v4...")
    v3_to_v4 = find_best_matches(nodes_v3, nodes_v4)

    return v1_to_v2 + v2_to_v3 + v3_to_v4  # Combine results

def save_results(results: List[Dict[str, Any]], output_path: str):
    """Saves the comparison results to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    v1p3_file = "../../data/consolidated_step3/v01-step3.json"
    v2p3_file = "../../data/consolidated_step3/v02-step3.json"
    v3p3_file = "../../data/consolidated_step3/v03-step3.json"
    v4p3_file = "../../data/consolidated_step3/v04-step3.json"
    
    print("Loading datasets...")
    v1p3 = load_dataset(v1p3_file)
    v2p3 = load_dataset(v2p3_file)
    v3p3 = load_dataset(v3p3_file)
    v4p3 = load_dataset(v4p3_file)

    print("Comparing node descriptions using SBERT...")
    comparison_results = compare_datasets([v1p3, v2p3, v3p3, v4p3])

    output_file = "../../src/accuracy/sbert_comparison_results.json"
    save_results(comparison_results, output_file)
