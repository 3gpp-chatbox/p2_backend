import itertools
import json

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load all four versions
version_files = [
    "data/consolidated_output/run1_step4.json",
    "data/consolidated_output/run2_step4.json",
    "data/consolidated_output/run3_step4.json",
    "data/consolidated_output/run4_step4.json",
    "data/consolidated_output/run5_step4.json",
]

versions = []
for file in version_files:
    with open(file, "r") as f:
        versions.append(json.load(f)["graph"])


# Function to extract nodes and edges as sets, focusing on description and type
def extract_sets(graph):
    nodes = [
        (node["type"], node["description"].strip().lower()) for node in graph["nodes"]
    ]
    edges = [
        (edge["type"], edge["description"].strip().lower()) for edge in graph["edges"]
    ]
    return nodes, edges


# Function to compute SBERT cosine similarity between two lists of descriptions
def sbert_similarity(list1, list2, model):
    # Create a list of descriptions for nodes and edges
    descriptions1 = [item[1] for item in list1]
    descriptions2 = [item[1] for item in list2]

    # Compute embeddings using SBERT
    embeddings1 = model.encode(descriptions1, convert_to_tensor=True)
    embeddings2 = model.encode(descriptions2, convert_to_tensor=True)

    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(embeddings1, embeddings2)
    return np.mean(similarity_matrix)  # Average similarity


# Load SBERT model
model = SentenceTransformer("all-MiniLM-L6-v2")  # You can use any SBERT model

# Store results
results = []
validity_threshold = 0.50  # Adjust if needed

# Compare all pairs (V1 vs V2, V1 vs V3, ..., V3 vs V4)
for (i, v1), (j, v2) in itertools.combinations(enumerate(versions, start=1), 2):
    nodes_v1, edges_v1 = extract_sets(v1)
    nodes_v2, edges_v2 = extract_sets(v2)

    # Compute SBERT similarity for nodes and edges separately
    node_similarity = sbert_similarity(nodes_v1, nodes_v2, model)
    edge_similarity = sbert_similarity(edges_v1, edges_v2, model)

    # Combine node and edge similarity for overall similarity
    overall_similarity = (node_similarity + edge_similarity) / 2

    # Determine validity
    valid = overall_similarity >= validity_threshold

    # Reasoning for similarity
    reasons = []
    reasons.append(f"Node similarity (SBERT) is {node_similarity * 100:.2f}%.")
    reasons.append(f"Edge similarity (SBERT) is {edge_similarity * 100:.2f}%.")
    reasons.append(f"Overall similarity is {overall_similarity * 100:.2f}%.")

    results.append(
        {
            "comparison": f"Version {i} vs Version {j}",
            "node_similarity": round(node_similarity, 4),
            "edge_similarity": round(edge_similarity, 4),
            "overall_similarity": round(overall_similarity, 4),
            "valid": valid,
            "reasons": reasons,
        }
    )

# Save results to JSON file
output_file = "src/accuracy/sbert_validation.json"
with open(output_file, "w") as f:
    json.dump(results, f, indent=4)

# Print summary
total_valid_comparisons = sum(1 for res in results if res["valid"])
total_comparisons = len(results)

print("\n🔍 Summary of Comparisons:")
print(f"   Total Comparisons: {total_comparisons}")
print(
    f"   Valid Comparisons: {total_valid_comparisons} ({(total_valid_comparisons / total_comparisons) * 100:.2f}%)\n"
)

for res in results:
    print(f"\n🔍 {res['comparison']}")
    print(f"   ✅ Node Similarity: {res['node_similarity'] * 100:.2f}%")
    print(f"   ✅ Edge Similarity: {res['edge_similarity'] * 100:.2f}%")
    print(f"   ✅ Overall Similarity: {res['overall_similarity'] * 100:.2f}%")
    print(f"   {'✔️ VALID' if res['valid'] else '❌ NOT VALID'}")
    print("   📌 Reason:", "; ".join(res["reasons"]))

print(f"\n📁 Results saved to {output_file}")
