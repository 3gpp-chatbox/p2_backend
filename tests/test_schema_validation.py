"""Tests for schema validation using mock data."""

import json
import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add p2_backend to path
from src.schema_validation import validate_data

# Path to mock data directory
MOCK_DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "data", "mock_data"
)


@pytest.fixture
def mock_step1_data():
    """Load mock step1 data."""
    with open(os.path.join(MOCK_DATA_DIR, "mockstep1.json"), "r") as f:
        return json.load(f)


@pytest.fixture
def mock_step2_data():
    """Load mock step2 data."""
    with open(os.path.join(MOCK_DATA_DIR, "mockstep2.json"), "r") as f:
        return json.load(f)


def test_mock_data_extraction():
    """Test that mock data can be processed and validated."""
    # Import here to avoid circular imports
    from data.mock_data.mockstep3 import extract_procedural_info

    section_name = "Registration procedure for initial registration"
    with open(os.path.join(MOCK_DATA_DIR, "mockstep1.json"), "r") as f:
        step1_data = json.load(f)
    with open(os.path.join(MOCK_DATA_DIR, "mockstep2.json"), "r") as f:
        step2_data = json.load(f)

    # Process the mock data
    result = extract_procedural_info(section_name, step1_data, step2_data)

    # Validate the output
    assert result is not None, "Extraction failed to produce output"
    assert validate_data(result), "Generated graph failed validation"


def test_node_structure(mock_step1_data, mock_step2_data):
    """Test that generated nodes have valid structure."""
    from data.mock_data.mockstep3 import extract_procedural_info

    section_name = "Registration procedure for initial registration"
    result = extract_procedural_info(section_name, mock_step1_data, mock_step2_data)

    assert "graph" in result
    assert "nodes" in result["graph"]

    for node in result["graph"]["nodes"]:
        # Test required fields
        assert "id" in node, "Node missing id"
        assert "type" in node, "Node missing type"
        assert "description" in node, "Node missing description"

        # Test valid node types
        assert node["type"] in ["state", "event"], f"Invalid node type: {node['type']}"


def test_edge_structure(mock_step1_data, mock_step2_data):
    """Test that generated edges have valid structure."""
    from data.mock_data.mockstep3 import extract_procedural_info

    section_name = "Registration procedure for initial registration"
    result = extract_procedural_info(section_name, mock_step1_data, mock_step2_data)

    assert "graph" in result
    assert "edges" in result["graph"]

    node_ids = {node["id"] for node in result["graph"]["nodes"]}

    for edge in result["graph"]["edges"]:
        # Test required fields
        assert "from" in edge, "Edge missing 'from' field"
        assert "to" in edge, "Edge missing 'to' field"
        assert "type" in edge, "Edge missing type"

        # Test edge connections
        assert edge["from"] in node_ids, f"Edge from non-existent node: {edge['from']}"
        assert edge["to"] in node_ids, f"Edge to non-existent node: {edge['to']}"


def test_complete_graph_validation(mock_step1_data, mock_step2_data):
    """Test complete graph structure validation."""
    from data.mock_data.mockstep3 import extract_procedural_info

    section_name = "Registration procedure for initial registration"
    result = extract_procedural_info(section_name, mock_step1_data, mock_step2_data)

    # Test overall structure
    assert "graph" in result
    assert "nodes" in result["graph"]
    assert "edges" in result["graph"]
    assert len(result["graph"]["nodes"]) > 0, "Graph should have nodes"

    # Validate using schema validation
    assert validate_data(result), "Complete graph failed validation"


def test_invalid_node_type():
    """Test that invalid node types are rejected."""
    invalid_graph = {
        "graph": {
            "nodes": [
                {
                    "id": "1",
                    "type": "invalid_type",  # Invalid type
                    "description": "Test node",
                }
            ],
            "edges": [],
        }
    }
    assert not validate_data(invalid_graph), "Invalid node type should be rejected"


def test_invalid_edge_references():
    """Test that edges must reference existing nodes."""
    invalid_graph = {
        "graph": {
            "nodes": [{"id": "1", "type": "state", "description": "Test state"}],
            "edges": [
                {
                    "from": "1",
                    "to": "nonexistent",  # References non-existent node
                    "type": "trigger",
                    "description": "Test edge",
                }
            ],
        }
    }
    assert not validate_data(invalid_graph), "Invalid edge reference should be rejected"
