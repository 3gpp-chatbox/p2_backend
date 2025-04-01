import json
import os
from pathlib import Path
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

# Get the absolute path to p2_backend directory
p2_backend_dir = Path(__file__).resolve().parents[2]
env_path = p2_backend_dir / '.env'

# Load environment variables from .env file
load_dotenv(env_path)

def load_dataset(file_path: str) -> Dict[str, any]:
    """Loads a JSON dataset from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_node_descriptions(dataset: Dict[str, any]) -> List[Dict[str, str]]:
    """Extracts node descriptions from the dataset."""
    return [
        {"id": node.get("id", ""), "description": node.get("description", "").strip()}
        for node in dataset.get("graph", {}).get("nodes", [])
        if node.get("description", "").strip()
    ]

def compute_cosine_similarity(text1: str, text2: str) -> float:
    """Computes the cosine similarity between two text strings."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

def compare_nodes(dataset1: Dict[str, any], dataset2: Dict[str, any], dataset3: Dict[str, any], threshold: float = 0.7) -> List[Dict[str, any]]:
    """Compares the node descriptions across three datasets using cosine similarity."""
    results = []
    nodes1 = get_node_descriptions(dataset1)
    nodes2 = get_node_descriptions(dataset2)
    nodes3 = get_node_descriptions(dataset3)
    
    # Ensure all datasets have the same number of nodes
    for node1, node2, node3 in zip(nodes1, nodes2, nodes3):
        # Convert numpy float32 to native Python float
        similarity_12 = float(compute_cosine_similarity(node1["description"], node2["description"]))
        similarity_13 = float(compute_cosine_similarity(node1["description"], node3["description"]))
        similarity_23 = float(compute_cosine_similarity(node2["description"], node3["description"]))

        # Consensus validation (majority voting)
        valid_count = sum([
            similarity_12 >= threshold,
            similarity_13 >= threshold,
            similarity_23 >= threshold
        ])
        
        valid = 1 if valid_count >= 2 else 0  # Majority agreement
        
        results.append({
            "id": node1.get("id"),
            "description_1": node1["description"],
            "description_2": node2["description"],
            "description_3": node3["description"],
            "cosine_similarity_12": float(similarity_12),  # Ensure float conversion
            "cosine_similarity_13": float(similarity_13),  # Ensure float conversion
            "cosine_similarity_23": float(similarity_23),  # Ensure float conversion
            "valid": valid
        })
    
    return results

def save_results(results: List[Dict[str, any]], output_path: str):
    """Saves the comparison results to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    # Load datasets (v1, v2, v3)
    v1_file = "../../data/version_1/step3.json"
    v2_file = "../../data/version_2/step3-v2.json"
    v3_file = "../../data/version_3/step3-v3.json"
    
    print("Loading datasets...")
    v1 = load_dataset(v1_file)
    v2 = load_dataset(v2_file)
    v3 = load_dataset(v3_file)
    
    print("Comparing node descriptions using cosine similarity...")
    comparison_results = compare_nodes(v1, v2, v3)
    
    output_file = "../../src/accuracy/cosine_comparison_results.json"
    save_results(comparison_results, output_file)
