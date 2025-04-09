import json

import numpy as np


# Function to calculate output statistics (min, max, std dev)
def calculate_output_statistics(dataset):
    node_counts = [len(graph["nodes"]) for graph in dataset]
    edge_counts = [len(graph["edges"]) for graph in dataset]

    # Node statistics
    node_min = np.min(node_counts)
    node_max = np.max(node_counts)
    node_mean = np.mean(node_counts)
    node_std = np.std(node_counts)
    node_range = node_max - node_min

    # Edge statistics
    edge_min = np.min(edge_counts)
    edge_max = np.max(edge_counts)
    edge_mean = np.mean(edge_counts)
    edge_std = np.std(edge_counts)
    edge_range = edge_max - edge_min

    return {
        "node_stats": {
            "min": node_min,
            "max": node_max,
            "mean": node_mean,
            "std_dev": node_std,
            "range": node_range,
        },
        "edge_stats": {
            "min": edge_min,
            "max": edge_max,
            "mean": edge_mean,
            "std_dev": edge_std,
            "range": edge_range,
        },
    }


# Function to combine ground truth and output statistics
def combine_metrics_and_statistics(ground_truth, output_statistics):
    combined_results = []

    for gt in ground_truth:
        # Get precision, recall, f1 scores from ground truth
        precision = gt["precision"]
        recall = gt["recall"]
        f1_score = gt["f1_score"]

        # Get output statistics for the version
        version = gt["version1"]  # Assuming version1 corresponds to the dataset
        stats = output_statistics[version]

        # Combine both into a single result
        combined_result = {
            "version1": gt["version1"],
            "version2": gt["version2"],
            "node_similarity": gt["node_similarity"],
            "edge_similarity": gt["edge_similarity"],
            "precision": precision,
            "recall": recall,
            "f1_score": f1_score,
            "node_stats": stats["node_stats"],
            "edge_stats": stats["edge_stats"],
        }

        combined_results.append(combined_result)

    return combined_results


# Main function
def main():
    # Define paths to the datasets
    dataset_files = [
        "data/consolidated_output/run1_step4.json",
        "data/consolidated_output/run2_step4.json",
        "data/consolidated_output/run3_step4.json",
        "data/consolidated_output/run4_step4.json",
        "data/consolidated_output/run5_step4.json",
    ]

    ground_truth = []

    # Load ground truth data
    for file in dataset_files:
        with open(file, "r") as f:
            ground_truth.append(json.load(f))

    # Load output statistics data (assuming each dataset is a list of graph data)
    output_statistics = {}
    for i, file in enumerate(dataset_files, 1):
        with open(f"data/output_statistics_v{i}.json", "r") as f:
            dataset = json.load(f)
            stats = calculate_output_statistics(dataset)
            output_statistics[f"v{i}"] = stats

    # Combine ground truth metrics and output statistics
    combined_results = combine_metrics_and_statistics(ground_truth, output_statistics)

    # Save combined results to an output file
    output_file = "combined_results.json"
    with open(output_file, "w") as f:
        json.dump(combined_results, f, indent=4)

    # Print a summary to the console
    print(f"📁 Combined results saved to {output_file}")
    for result in combined_results:
        print(
            f"\n🔍 Comparison: Version {result['version1']} vs Version {result['version2']}"
        )
        print(f"   ✅ Node Similarity: {result['node_similarity'] * 100:.2f}%")
        print(f"   ✅ Edge Similarity: {result['edge_similarity'] * 100:.2f}%")
        print(f"   📊 Precision: {result['precision'] * 100:.2f}%")
        print(f"   📊 Recall: {result['recall'] * 100:.2f}%")
        print(f"   📊 F1 Score: {result['f1_score'] * 100:.2f}%")
        print(
            f"   📊 Node Stats - Min: {result['node_stats']['min']}, Max: {result['node_stats']['max']}, Mean: {result['node_stats']['mean']:.2f}, Std Dev: {result['node_stats']['std_dev']:.2f}"
        )
        print(
            f"   📊 Edge Stats - Min: {result['edge_stats']['min']}, Max: {result['edge_stats']['max']}, Mean: {result['edge_stats']['mean']:.2f}, Std Dev: {result['edge_stats']['std_dev']:.2f}"
        )


# Run the script
if __name__ == "__main__":
    main()
