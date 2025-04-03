import json
from collections import defaultdict
from itertools import combinations

# Load all four versions
version_files = [
    "data/version_1/step3.json",
    "data/version_2/v02-step3.json",
    "data/version_3/step3-v3.json",
    "data/version_4/step3-v4.json"
]
versions = [json.load(open(file))["graph"] for file in version_files]

# Extract nodes and edges from each version
node_sets = []
edge_sets = []

for version in versions:
    nodes = {(node["id"], node["type"], node["description"].strip().lower()) for node in version["nodes"]}
    edges = {(edge["from"], edge["to"], edge["type"], edge["description"].strip().lower()) for edge in version["edges"]}
    node_sets.append(nodes)
    edge_sets.append(edges)

# Define majority threshold (3 out of 4 datasets)
threshold = 3

# Count occurrences of nodes and edges
node_counts = defaultdict(int)
edge_counts = defaultdict(int)

for nodes, edges in zip(node_sets, edge_sets):
    for node in nodes:
        node_counts[node] += 1
    for edge in edges:
        edge_counts[edge] += 1

# Find majority agreement nodes and edges
majority_nodes = {k for k, v in node_counts.items() if v >= threshold}
majority_edges = {k for k, v in edge_counts.items() if v >= threshold}

# Identify flagged nodes and edges (less than majority)
flagged_nodes = {k: v for k, v in node_counts.items() if v < threshold}
flagged_edges = {k: v for k, v in edge_counts.items() if v < threshold}

# Pairwise comparisons to check dataset similarity
pairwise_similarities = {}

for (i, nodes_i), (j, nodes_j) in combinations(enumerate(node_sets), 2):
    common_nodes = nodes_i & nodes_j
    similarity_nodes = len(common_nodes) / max(len(nodes_i), len(nodes_j))  # Jaccard similarity
    pairwise_similarities[f"Nodes V{i+1} vs V{j+1}"] = similarity_nodes

for (i, edges_i), (j, edges_j) in combinations(enumerate(edge_sets), 2):
    common_edges = edges_i & edges_j
    similarity_edges = len(common_edges) / max(len(edges_i), len(edges_j))  # Jaccard similarity
    pairwise_similarities[f"Edges V{i+1} vs V{j+1}"] = similarity_edges

# Compute overall accuracy metrics
avg_extracted_nodes = sum(len(nodes) for nodes in node_sets) / len(node_sets)
avg_extracted_edges = sum(len(edges) for edges in edge_sets) / len(edge_sets)

accuracy_nodes = len(majority_nodes) / avg_extracted_nodes
accuracy_edges = len(majority_edges) / avg_extracted_edges
disagreement_rate_nodes = len(flagged_nodes) / avg_extracted_nodes
disagreement_rate_edges = len(flagged_edges) / avg_extracted_edges

# Save results
results = {
    "accuracy_nodes": accuracy_nodes,
    "accuracy_edges": accuracy_edges,
    "disagreement_rate_nodes": disagreement_rate_nodes,
    "disagreement_rate_edges": disagreement_rate_edges,
    "pairwise_similarities": pairwise_similarities,
    "flagged_nodes": list(flagged_nodes.keys()),
    "flagged_edges": list(flagged_edges.keys()),
}

with open("src/accuracy/majorityvoting.json", "w") as f:
    json.dump(results, f, indent=4)

# Print results
print(f"✅ Node Accuracy: {accuracy_nodes:.2%}")
print(f"✅ Edge Accuracy: {accuracy_edges:.2%}")
print(f"⚠️ Node Disagreement Rate: {disagreement_rate_nodes:.2%}")
print(f"⚠️ Edge Disagreement Rate: {disagreement_rate_edges:.2%}")

print("\n🔍 Pairwise Similarities:")
for pair, score in pairwise_similarities.items():
    print(f"{pair}: {score:.2%}")

print("\n🔍 Nodes flagged for review:")
for node in flagged_nodes:
    print(f"{node} (appeared in {flagged_nodes[node]} versions)")

print("\n🔍 Edges flagged for review:")
for edge in flagged_edges:
    print(f"{edge} (appeared in {flagged_edges[edge]} versions)")
