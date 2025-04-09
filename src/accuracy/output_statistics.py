import json
import os
from statistics import mean, stdev

# Paths to all LLM output files
version_files = [
    "data/consolidated_output/run1_step4.json",
    "data/consolidated_output/run2_step4.json",
    "data/consolidated_output/run3_step4.json",
    "data/consolidated_output/run4_step4.json",
    "data/consolidated_output/run5_step4.json",
]

# Extract node and edge counts
node_counts = []
edge_counts = []
dataset_details = []

for file_path in version_files:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)["graph"]
            num_nodes = len(data["nodes"])
            num_edges = len(data["edges"])
            node_counts.append(num_nodes)
            edge_counts.append(num_edges)
            dataset_details.append(
                {"file": file_path, "nodes": num_nodes, "edges": num_edges}
            )
    except FileNotFoundError:
        print(f"Warning: File not found: {file_path}")
    except KeyError:
        print(f"Warning: Invalid file format in {file_path}")
    except json.JSONDecodeError:
        print(f"Warning: Invalid JSON in {file_path}")


# Helper function for printing stats
def print_stats(name, counts):
    if not counts:
        print(f"\n📊 Stats for {name}:")
        print("   ➤ No data available")
        return

    print(f"\n📊 Stats for {name}:")
    print(f"   ➤ Min: {min(counts)}")
    print(f"   ➤ Max: {max(counts)}")
    print(f"   ➤ Mean: {mean(counts):.2f}")
    print(
        f"   ➤ Std Dev: {stdev(counts):.2f}"
        if len(counts) > 1
        else "   ➤ Std Dev: N/A (only one value)"
    )
    print(f"   ➤ Range: {max(counts) - min(counts)}")


# Print stats
print_stats("Node Counts", node_counts)
print_stats("Edge Counts", edge_counts)

# Save to JSON
output = {
    "summary": {
        "nodes": {
            "min": min(node_counts) if node_counts else 0,
            "max": max(node_counts) if node_counts else 0,
            "mean": mean(node_counts) if node_counts else 0,
            "stdev": stdev(node_counts) if len(node_counts) > 1 else 0.0,
        },
        "edges": {
            "min": min(edge_counts) if edge_counts else 0,
            "max": max(edge_counts) if edge_counts else 0,
            "mean": mean(edge_counts) if edge_counts else 0,
            "stdev": stdev(edge_counts) if len(edge_counts) > 1 else 0.0,
        },
    },
    "datasets": dataset_details,
}


# Ensure the directory exists
os.makedirs("src/accuracy", exist_ok=True)

with open("src/accuracy/output_statistics.json", "w") as f:
    json.dump(output, f, indent=4)

print("\n📁 Structure consistency saved to 'src/accuracy/output_statistics.json'")
