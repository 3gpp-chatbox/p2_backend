import itertools
import json

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


# Function to extract nodes and edges as sets, focusing on description and type
def extract_sets(graph):
    nodes = {
        (node["type"], node["description"].strip().lower()) for node in graph["nodes"]
    }
    edges = {
        (edge["type"], edge["description"].strip().lower()) for edge in graph["edges"]
    }
    return nodes, edges


# Compute Jaccard similarity
def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0  # Avoid division by zero


# Store results
results = []
validity_threshold = 0.50  # Adjust if needed

# Compare all pairs (V1 vs V2, V1 vs V3, ..., V3 vs V4)
for (i, v1), (j, v2) in itertools.combinations(enumerate(versions, start=1), 2):
    nodes_v1, edges_v1 = extract_sets(v1)
    nodes_v2, edges_v2 = extract_sets(v2)

    jaccard_nodes = jaccard_similarity(nodes_v1, nodes_v2)
    jaccard_edges = jaccard_similarity(edges_v1, edges_v2)

    # Combine node and edge similarity for overall similarity
    overall_similarity = (jaccard_nodes + jaccard_edges) / 2

    # Determine validity
    valid = overall_similarity >= validity_threshold

    # Reasoning for similarity
    reasons = []
    reasons.append(f"Overall similarity is {overall_similarity * 100:.2f}%.")

    results.append(
        {
            "comparison": f"Version {i} vs Version {j}",
            "overall_similarity": round(overall_similarity, 4),
            "valid": valid,
            "reasons": reasons,
        }
    )

# Save results to JSON file
output_file = "src/accuracy/jaccard_validation.json"
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
    print(f"   ✅ Overall Similarity: {res['overall_similarity'] * 100:.2f}%")
    print(f"   {'✔️ VALID' if res['valid'] else '❌ NOT VALID'}")
    print("   📌 Reason:", "; ".join(res["reasons"]))

print(f"\n📁 Results saved to {output_file}")
