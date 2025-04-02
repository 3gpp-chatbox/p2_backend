import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the datasets (replace with your actual data loading method)
def load_datasets(file_paths):
    datasets = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            datasets.append(json.load(file))
    return datasets

# Compute cosine similarity for conditions, triggers, and outcomes
def calculate_cosine_similarity(text1, text2):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # You can use another model if needed
    embeddings1 = model.encode([text1])
    embeddings2 = model.encode([text2])
    similarity = cosine_similarity(embeddings1, embeddings2)[0][0]
    return similarity

# Compare edges across datasets based on "from" and "to" nodes
def compare_edges(datasets):
    discrepancies = []

    print("Starting edge comparison...")

    for dataset_idx, dataset in enumerate(datasets):
        print(f"Comparing edges in dataset {dataset_idx + 1}/{len(datasets)}...")
        for edge in dataset['graph']['edges']:
            from_node = edge['from']
            to_node = edge['to']
            edge_condition = edge.get('properties', {}).get('condition', "")
            edge_trigger = edge.get('properties', {}).get('trigger', "")
            edge_outcome = edge.get('properties', {}).get('outcome', "")

            print(f"  Comparing edge {from_node}->{to_node}...")

            # Compare the edge with the same "from" and "to" in other datasets
            for other_dataset_idx, other_dataset in enumerate(datasets):
                if dataset_idx != other_dataset_idx:
                    found_match = False
                    for other_edge in other_dataset['graph']['edges']:
                        # Ensure that the edge connects the same nodes (from and to)
                        if edge['from'] == other_edge['from'] and edge['to'] == other_edge['to']:
                            found_match = True
                            comparisons = []
                            valid = True

                            # Compare edge conditions using cosine similarity
                            condition_similarity = calculate_cosine_similarity(edge_condition, other_edge.get('properties', {}).get('condition', ""))
                            condition_valid = condition_similarity >= 0.8
                            comparisons.append({
                                'property': 'condition',
                                'similarity': condition_similarity,
                                'valid': condition_valid
                            })
                            if not condition_valid:
                                valid = False

                            # Compare edge triggers using cosine similarity
                            trigger_similarity = calculate_cosine_similarity(edge_trigger, other_edge.get('properties', {}).get('trigger', ""))
                            trigger_valid = trigger_similarity >= 0.8
                            comparisons.append({
                                'property': 'trigger',
                                'similarity': trigger_similarity,
                                'valid': trigger_valid
                            })
                            if not trigger_valid:
                                valid = False

                            # Compare edge outcomes using cosine similarity
                            outcome_similarity = calculate_cosine_similarity(edge_outcome, other_edge.get('properties', {}).get('outcome', ""))
                            outcome_valid = outcome_similarity >= 0.8
                            comparisons.append({
                                'property': 'outcome',
                                'similarity': outcome_similarity,
                                'valid': outcome_valid
                            })
                            if not outcome_valid:
                                valid = False

                            # If any property is invalid, mark the edge as invalid
                            if not valid:
                                discrepancies.append({
                                    'dataset': dataset_idx,
                                    'edge': f"{from_node}->{to_node}",
                                    'other_dataset': other_dataset_idx,
                                    'other_edge': f"{other_edge['from']}->{other_edge['to']}",
                                    'comparisons': comparisons,
                                    'valid': False
                                })
                            else:
                                discrepancies.append({
                                    'dataset': dataset_idx,
                                    'edge': f"{from_node}->{to_node}",
                                    'other_dataset': other_dataset_idx,
                                    'other_edge': f"{other_edge['from']}->{other_edge['to']}",
                                    'comparisons': comparisons,
                                    'valid': True
                                })

                    # If no matching edge found in the other dataset, it's considered missing
                    if not found_match:
                        discrepancies.append({
                            'dataset': dataset_idx,
                            'edge': f"{from_node}->{to_node}",
                            'missing_in': other_dataset_idx
                        })

    return discrepancies

# Helper function to recursively convert numpy float32 to regular float
def convert_float32_to_float(obj):
    if isinstance(obj, dict):
        return {key: convert_float32_to_float(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_float32_to_float(item) for item in obj]
    elif isinstance(obj, np.float32):  # Check for numpy float32
        return float(obj)  # Convert to regular float
    else:
        return obj  # Return other types unchanged
    
def convert_numpy_types_to_native(obj):
    if isinstance(obj, dict):
        return {key: convert_numpy_types_to_native(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types_to_native(item) for item in obj]
    elif isinstance(obj, np.float32):  # Check for numpy float32
        return float(obj)  # Convert to regular float
    elif isinstance(obj, np.bool_):  # Check for numpy boolean
        return bool(obj)  # Convert to regular bool
    else:
        return obj  # Return other types unchanged


# Main validation function
def validate_edge_consistency(file_paths, output_file):
    datasets = load_datasets(file_paths)

    # Check edge consistency
    print("Validating edge consistency...")
    edge_discrepancies = compare_edges(datasets)
    if edge_discrepancies:
        print("Edge Discrepancies Found. Writing to output file...")

        # Convert any numpy types (float32, bool_) to native Python types before dumping to JSON
        edge_discrepancies_serializable = convert_numpy_types_to_native(edge_discrepancies)
        
        # Write discrepancies to a file
        with open(output_file, 'w') as out_file:
            json.dump(edge_discrepancies_serializable, out_file, indent=4)
        print(f"Discrepancies written to {output_file}")
    else:
        print("No edge discrepancies found.")

# Example usage
if __name__ == "__main__":
    # Replace these with the actual paths to your JSON files
    file_paths = ["../../data/consolidated_step3/v01-step3.json", 
                  "../../data/consolidated_step3/v02-step3.json", 
                  "../../data/consolidated_step3/v03-step3.json", 
                  "../../data/consolidated_step3/v04-step3.json"]
    output_file = "edge_discrepancies.json"  # Output file for discrepancies
    validate_edge_consistency(file_paths, output_file)
