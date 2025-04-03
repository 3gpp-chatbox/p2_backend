import json
import itertools

# Load all four versions
version_files = [
    "data/version_1/step3.json",
    "data/version_2/v02-step3.json",
    "data/version_3/step3-v3.json",
    "data/version_4/step3-v4.json",
]

versions = []
for file in version_files:
    with open(file, "r") as f:
        versions.append(json.load(f)["graph"])

# Function to extract nodes and edges as sets, excluding IDs
def extract_sets(graph):
    # Exclude the "id" field from nodes and edges
    nodes = { (node["type"], node["description"].strip().lower()) for node in graph["nodes"] }
    edges = { (edge["from"], edge["to"], edge["type"], edge["description"].strip().lower()) for edge in graph["edges"] }
    return nodes, edges

# Compute Jaccard similarity
def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0  # Avoid division by zero

# Store results
results = []
validity_threshold = 0.75  # Adjust if needed

# Compare all pairs (V1 vs V2, V1 vs V3, ..., V3 vs V4)
for (i, v1), (j, v2) in itertools.combinations(enumerate(versions, start=1), 2):
    nodes_v1, edges_v1 = extract_sets(v1)
    nodes_v2, edges_v2 = extract_sets(v2)

    jaccard_nodes = jaccard_similarity(nodes_v1, nodes_v2)
    jaccard_edges = jaccard_similarity(edges_v1, edges_v2)

    # Determine validity
    valid_nodes = jaccard_nodes >= validity_threshold
    valid_edges = jaccard_edges >= validity_threshold
    overall_valid = valid_nodes and valid_edges

    # Reasoning for validity
    reasons = []
    if valid_nodes:
        reasons.append("Nodes have high agreement across datasets.")
    else:
        reasons.append(f"Node similarity is low ({jaccard_nodes:.2%}). Possible inconsistencies in node extraction.")

    if valid_edges:
        reasons.append("Edges have high agreement across datasets.")
    else:
        reasons.append(f"Edge similarity is low ({jaccard_edges:.2%}). Possible inconsistencies in edge extraction.")

    results.append({
        "comparison": f"Version {i} vs Version {j}",
        "jaccard_nodes": round(jaccard_nodes, 4),
        "jaccard_edges": round(jaccard_edges, 4),
        "is_valid": overall_valid,
        "reasons": reasons
    })

# Save results to JSON file
output_file = "src/accuracy/jaccard_validation_no_ids.json"
with open(output_file, "w") as f:
    json.dump(results, f, indent=4)

# Print summary
for res in results:
    print(f"\n🔍 {res['comparison']}")
    print(f"   ✅ Node Similarity: {res['jaccard_nodes']:.2%}")
    print(f"   ✅ Edge Similarity: {res['jaccard_edges']:.2%}")
    print(f"   {'✔️ VALID' if res['is_valid'] else '❌ NOT VALID'}")
    print("   📌 Reason:", "; ".join(res["reasons"]))

print(f"\n📁 Results saved to {output_file}")
