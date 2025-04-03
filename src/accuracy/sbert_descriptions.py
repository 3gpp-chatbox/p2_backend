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

# Extract edge descriptions
def extract_edge_descriptions(dataset: Dict[str, Any], dataset_name: str) -> List[Dict[str, Any]]:
    edges = []
    if dataset and "graph" in dataset and "edges" in dataset["graph"]:
        for edge in dataset["graph"]["edges"]:
            description = edge.get("description", "")
            metadata = ""
            if "type" in edge:
                metadata += f" Type: {edge['type']}"
            if "properties" in edge:
                metadata += f" Properties: {edge['properties']}"
            
            # Create a composite ID from 'from' and 'to' fields
            edge_id = f"{edge['from']}->{edge['to']}"
            
            edges.append({
                "id": edge_id,
                "description": description + metadata,
                "dataset": dataset_name
            })
    return edges

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

# Compare edge descriptions
def find_best_edge_matches(edge_set_1: List[Dict[str, Any]], edge_set_2: List[Dict[str, Any]], fixed_threshold: float = 0.7) -> Dict[str, Any]:
    descriptions_1 = [edge["description"] for edge in edge_set_1]
    descriptions_2 = [edge["description"] for edge in edge_set_2]

    if not descriptions_1 or not descriptions_2:
        return {"matches": [], "unmatched": edge_set_1}  # If either dataset is empty

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
            matched_pairs.append({
                "id_1": edge_1["id"],
                "description_1": edge_1["description"],
                "dataset_1": edge_1["dataset"],
                "id_2": edge_set_2[best_match_idx_1]["id"],
                "description_2": edge_set_2[best_match_idx_1]["description"],
                "dataset_2": edge_set_2[best_match_idx_1]["dataset"],
                "cosine_similarity": best_match_score_1,
                "valid": True
            })
        else:
            unmatched_edges.append(edge_1)
    
    return {"matches": matched_pairs, "unmatched": unmatched_edges}

# Compare datasets and include unmatched nodes and edges
def compare_datasets(datasets: Dict[str, Any], fixed_threshold: float = 0.7) -> Dict[str, Any]:
    nodes_v1 = extract_node_descriptions(datasets["v1"], "v1")
    nodes_v2 = extract_node_descriptions(datasets["v2"], "v2")
    nodes_v3 = extract_node_descriptions(datasets["v3"], "v3")
    nodes_v4 = extract_node_descriptions(datasets["v4"], "v4")
    
    edges_v1 = extract_edge_descriptions(datasets["v1"], "v1")
    edges_v2 = extract_edge_descriptions(datasets["v2"], "v2")
    edges_v3 = extract_edge_descriptions(datasets["v3"], "v3")
    edges_v4 = extract_edge_descriptions(datasets["v4"], "v4")

    print("Matching v1 to v2 (nodes)...")
    v1_to_v2_nodes = find_best_matches(nodes_v1, nodes_v2, fixed_threshold)
    print("Matching v1 to v2 (edges)...")
    v1_to_v2_edges = find_best_edge_matches(edges_v1, edges_v2, fixed_threshold)

    print("Matching v1 to v3 (nodes)...")
    v1_to_v3_nodes = find_best_matches(nodes_v1, nodes_v3, fixed_threshold)
    print("Matching v1 to v3 (edges)...")
    v1_to_v3_edges = find_best_edge_matches(edges_v1, edges_v3, fixed_threshold)

    print("Matching v1 to v4 (nodes)...")
    v1_to_v4_nodes = find_best_matches(nodes_v1, nodes_v4, fixed_threshold)
    print("Matching v1 to v4 (edges)...")
    v1_to_v4_edges = find_best_edge_matches(edges_v1, edges_v4, fixed_threshold)

    print("Matching v2 to v3 (nodes)...")
    v2_to_v3_nodes = find_best_matches(nodes_v2, nodes_v3, fixed_threshold)
    print("Matching v2 to v3 (edges)...")
    v2_to_v3_edges = find_best_edge_matches(edges_v2, edges_v3, fixed_threshold)

    print("Matching v2 to v4 (nodes)...")
    v2_to_v4_nodes = find_best_matches(nodes_v2, nodes_v4, fixed_threshold)
    print("Matching v2 to v4 (edges)...")
    v2_to_v4_edges = find_best_edge_matches(edges_v2, edges_v4, fixed_threshold)

    print("Matching v3 to v4 (nodes)...")
    v3_to_v4_nodes = find_best_matches(nodes_v3, nodes_v4, fixed_threshold)
    print("Matching v3 to v4 (edges)...")
    v3_to_v4_edges = find_best_edge_matches(edges_v3, edges_v4, fixed_threshold)

    # Separate node and edge matches
    node_matches = (
        v1_to_v2_nodes["matches"] + v1_to_v3_nodes["matches"] + v1_to_v4_nodes["matches"] +
        v2_to_v3_nodes["matches"] + v2_to_v4_nodes["matches"] + v3_to_v4_nodes["matches"]
    )
    edge_matches = (
        v1_to_v2_edges["matches"] + v1_to_v3_edges["matches"] + v1_to_v4_edges["matches"] +
        v2_to_v3_edges["matches"] + v2_to_v4_edges["matches"] + v3_to_v4_edges["matches"]
    )
    
    # Separate unmatched nodes and edges
    unmatched_nodes = (
        v1_to_v2_nodes["unmatched"] + v1_to_v3_nodes["unmatched"] + v1_to_v4_nodes["unmatched"] +
        v2_to_v3_nodes["unmatched"] + v2_to_v4_nodes["unmatched"] + v3_to_v4_nodes["unmatched"]
    )
    unmatched_edges = (
        v1_to_v2_edges["unmatched"] + v1_to_v3_edges["unmatched"] + v1_to_v4_edges["unmatched"] +
        v2_to_v3_edges["unmatched"] + v2_to_v4_edges["unmatched"] + v3_to_v4_edges["unmatched"]
    )

    validity = "valid" if len(unmatched_nodes) + len(unmatched_edges) == 0 else "invalid"
    
    # Calculate separate totals for nodes and edges
    total_node_matches = len(node_matches)
    total_edge_matches = len(edge_matches)
    total_unmatched_nodes = len(unmatched_nodes)
    total_unmatched_edges = len(unmatched_edges)
    total_nodes = total_node_matches + total_unmatched_nodes
    total_edges = total_edge_matches + total_unmatched_edges

    # Create summary section with separate node and edge statistics
    summary = {
        "validity_status": validity,
        "validation_reason": "There are unmatched nodes or edges" if validity == "invalid" else "All nodes and edges are matched",
        "node_stats": {
            "total": total_nodes,
            "matched": total_node_matches,
            "unmatched": total_unmatched_nodes,
            "match_percentage": (total_node_matches / total_nodes * 100) if total_nodes > 0 else 0
        },
        "edge_stats": {
            "total": total_edges,
            "matched": total_edge_matches,
            "unmatched": total_unmatched_edges,
            "match_percentage": (total_edge_matches / total_edges * 100) if total_edges > 0 else 0
        }
    }

    return {
        "summary": summary,
        "node_matches": node_matches,
        "edge_matches": edge_matches,
        "unmatched_nodes": unmatched_nodes,
        "unmatched_edges": unmatched_edges
    }

# Save results with formatted output
def save_results(results: Dict[str, Any], output_path: str):
    # Print summary to console
    summary = results["summary"]
    print("\n=== VALIDATION SUMMARY ===")
    print(f"Status: {summary['validity_status'].upper()}")
    print(f"Reason: {summary['validation_reason']}")
    
    print("\nNode Statistics:")
    print(f"Total Nodes: {summary['node_stats']['total']}")
    print(f"Matched Nodes: {summary['node_stats']['matched']} ({summary['node_stats']['match_percentage']:.2f}%)")
    print(f"Unmatched Nodes: {summary['node_stats']['unmatched']}")
    
    print("\nEdge Statistics:")
    print(f"Total Edges: {summary['edge_stats']['total']}")
    print(f"Matched Edges: {summary['edge_stats']['matched']} ({summary['edge_stats']['match_percentage']:.2f}%)")
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
        "v3": os.path.join(data_dir, "version_3/step3-v3.json"),
        "v4": os.path.join(data_dir, "version_4/step3-v4.json"),
    }

    # Load the datasets
    datasets = {key: load_dataset(file) for key, file in dataset_files.items()}

    # Compare datasets
    results = compare_datasets(datasets)
    
    # Save the results
    save_results(results, "src/accuracy/sbert_comparison_results.json")
