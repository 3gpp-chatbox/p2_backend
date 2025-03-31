import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

def load_dataset(file_path: str) -> Dict[str, any]:
    """Loads a JSON dataset from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_step_descriptions(dataset: Dict[str, any]) -> List[str]:
    """Extracts step descriptions from the dataset."""
    return [step.get("step", "") for step in dataset.get("steps", [])]

def compute_cosine_similarity(text1: str, text2: str) -> float:
    """Computes the cosine similarity between two text strings."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

def compare_steps(dataset1: Dict[str, any], dataset2: Dict[str, any], threshold: float = 0.8) -> Dict[str, any]:
    """Compares the steps between two datasets using cosine similarity."""
    results = []
    steps1 = dataset1.get("steps", [])
    steps2 = dataset2.get("steps", [])
    
    # Assuming steps are in the same order for simplicity
    for step1, step2 in zip(steps1, steps2):
        step_desc1 = step1.get("step", "")
        step_desc2 = step2.get("step", "")
        
        # Compute cosine similarity
        similarity = float(compute_cosine_similarity(step_desc1, step_desc2))  # Convert to float
        
        # Check if the steps are similar enough
        valid = bool(similarity >= threshold)  # Explicitly convert to bool
        
        results.append({
            "id": step1.get("id"),
            "step_description_1": step_desc1,
            "step_description_2": step_desc2,
            "cosine_similarity": similarity,
            "valid": int(valid)  # Convert bool to int (0 or 1)
        })
    
    return results

def save_results(results: Dict[str, any], output_path: str):
    """Saves the comparison results to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    # Load datasets (v1 and v2)
    v1p1_file = "../../data/version_1/step1.json"
    v2p1_file = "../../data/version_2/step1-v2.json"
    
    print("Loading datasets...")
    v1 = load_dataset(v1p1_file)
    v2 = load_dataset(v2p1_file)
    
    print("Comparing steps using cosine similarity...")
    comparison_results = compare_steps(v1, v2)
    
    output_file = "../../src/accuracy/cosine_comparison_results.json"
    save_results(comparison_results, output_file)
