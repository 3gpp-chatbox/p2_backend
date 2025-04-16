# test_accuracy_validation.py

import json

import numpy as np

from src.accuracy.sbert_simple import (
    compare_two_datasets,
    compute_sbert_embeddings,
    extract_edge_descriptions,
    extract_node_descriptions,
    find_best_matches,
)

# Sample minimal dataset for testing
sample_dataset = {
    "graph": {
        "nodes": [
            {
                "id": "n1",
                "type": "Action",
                "description": "Start session",
                "properties": {"status": "initial"},
            }
        ],
        "edges": [
            {
                "from": "n1",
                "to": "n2",
                "type": "transition",
                "description": "Proceed to next step",
            }
        ],
    }
}

# Another sample with similar structure
similar_dataset = {
    "graph": {
        "nodes": [
            {
                "id": "n1",
                "type": "Action",
                "description": "Begin session",
                "properties": {"status": "initial"},
            }
        ],
        "edges": [
            {
                "from": "n1",
                "to": "n2",
                "type": "transition",
                "description": "Go to next step",
            }
        ],
    }
}


def test_extract_node_descriptions():
    nodes = extract_node_descriptions(sample_dataset, "test")
    assert len(nodes) == 1
    assert "Start session" in nodes[0]["description"]
    assert nodes[0]["dataset"] == "test"


def test_extract_edge_descriptions():
    edges = extract_edge_descriptions(sample_dataset, "test")
    assert len(edges) == 1
    assert "Proceed to next step" in edges[0]["description"]
    assert edges[0]["dataset"] == "test"


def test_compute_sbert_embeddings():
    descriptions = ["This is a test", "Another sentence"]
    embeddings = compute_sbert_embeddings(descriptions)
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape[0] == 2


def test_find_best_matches():
    nodes_1 = extract_node_descriptions(sample_dataset, "v1")
    nodes_2 = extract_node_descriptions(similar_dataset, "v2")
    results = find_best_matches(nodes_1, nodes_2, fixed_threshold=0.8)
    assert "matches" in results
    assert "unmatched" in results
    assert len(results["matches"]) >= 1  # should match loosely


def test_compare_two_datasets_summary():
    results = compare_two_datasets(
        sample_dataset, similar_dataset, "v1", "v2", fixed_threshold=0.8
    )
    summary = results["summary"]
    assert "validity_status" in summary
    assert "node_stats" in summary
    assert isinstance(summary["node_stats"]["matched"], int)
    assert isinstance(summary["edge_stats"]["matched"], int)


def test_output_saving(tmp_path):
    from src.accuracy.sbert_simple import save_results

    output_path = tmp_path / "result.json"
    results = compare_two_datasets(sample_dataset, similar_dataset, "v1", "v2", 0.8)
    save_results(results, str(output_path))
    assert output_path.exists()

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert "summary" in data
