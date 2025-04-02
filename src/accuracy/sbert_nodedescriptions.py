import json 
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Load JSON dataset

def load_dataset(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Extract node descriptions

def extract_node_descriptions(dataset: Dict[str, Any], dataset_name: str) -> List[Dict[str, Any]]:
    nodes = []
    if dataset and "graph" in dataset and "nodes" in dataset["graph"]:
        for node in dataset["graph"]["nodes"]:
            description = node.get("description", "")
            metadata = ""
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

# Compute SBERT embeddings

def compute_sbert_embeddings(descriptions: List[str]) -> np.ndarray:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(descriptions, convert_to_tensor=True)
    return embeddings.cpu().numpy()

# Find best matches with unmatched nodes tracking

def find_best_matches(node_set_1: List[Dict[str, Any]], node_set_2: List[Dict[str, Any]], fixed_threshold: float = 0.7) -> Dict[str, Any]:
    descriptions_1 = [node["description"] for node in node_set_1]
    descriptions_2 = [node["description"] for node in node_set_2]

    if not descriptions_1 or not descriptions_2:
        return {"matches": [], "unmatched": node_set_1}  # If either dataset is empty

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
            matched_pairs.append({
                "id_1": node_1["id"],
                "description_1": node_1["description"],
                "dataset_1": node_1["dataset"],
                "id_2": node_set_2[best_match_idx_1]["id"],
                "description_2": node_set_2[best_match_idx_1]["description"],
                "dataset_2": node_set_2[best_match_idx_1]["dataset"],
                "cosine_similarity": best_match_score_1,
                "valid": True
            })
        else:
            unmatched_nodes.append(node_1)
    
    return {"matches": matched_pairs, "unmatched": unmatched_nodes}

# Compare datasets and include unmatched nodes

def compare_datasets(datasets: Dict[str, Any], fixed_threshold: float = 0.7) -> Dict[str, Any]:
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

    return {
        "matches": v1_to_v2["matches"] + v1_to_v3["matches"] + v1_to_v4["matches"] + v2_to_v3["matches"] + v2_to_v4["matches"] + v3_to_v4["matches"],
        "unmatched_nodes": v1_to_v2["unmatched"] + v1_to_v3["unmatched"] + v1_to_v4["unmatched"] + v2_to_v3["unmatched"] + v2_to_v4["unmatched"] + v3_to_v4["unmatched"]
    }

# Save results

def save_results(results: Dict[str, Any], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    # Use absolute paths based on workspace
    workspace_dir = "C:/Users/Mediatek/3gppchatbot"
    data_dir = os.path.join(workspace_dir, "p2_backend", "data", "consolidated_step3")
    
    dataset_files = {
        "v1": os.path.join(data_dir, "v01-step3.json"),
        "v2": os.path.join(data_dir, "v02-step3.json"),
        "v3": os.path.join(data_dir, "v03-step3.json"),
        "v4": os.path.join(data_dir, "v04-step3.json")
    }
    
    print("Loading datasets...")
    print(f"Looking for files in: {data_dir}")
    
    # Check if files exist
    missing_files = []
    for name, path in dataset_files.items():
        if not os.path.exists(path):
            missing_files.append(f"{name}: {path}")
    
    if missing_files:
        print("\nError: The following files are missing:")
        for file in missing_files:
            print(f"- {file}")
        print("\nPlease ensure all required files are in the correct location.")
        exit(1)
    
    # Load datasets
    try:
        datasets = {name: load_dataset(path) for name, path in dataset_files.items()}
    except Exception as e:
        print(f"Error loading datasets: {str(e)}")
        exit(1)

    print("\nComparing node descriptions using SBERT...")
    comparison_results = compare_datasets(datasets)

    # Save results in the accuracy directory
    output_file = os.path.join(data_dir, "sbert_comparison_results.json")
    save_results(comparison_results, output_file)