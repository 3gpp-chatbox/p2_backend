"""Tests for schema validation using mock data."""

import json
import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add p2_backend to path
from src.schema_validation import validate_data

# Path to mock data directory
MOCK_DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "data", "mock_pydantic"
)

# Valid node types based on the actual graph structure
VALID_NODE_TYPES = {"start", "process", "timer", "decision", "end", "state", "event"}


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
    from data.mock_pydantic.mockstep3 import extract_procedural_info

    section_name = "Registration procedure for initial registration"
    with open(os.path.join(MOCK_DATA_DIR, "mockstep1.json"), "r") as f:
        step1_data = json.load(f)
    with open(os.path.join(MOCK_DATA_DIR, "mockstep2.json"), "r") as f:
        step2_data = json.load(f)

    # Process the mock data
    result_json_str = extract_procedural_info(section_name, step1_data, step2_data)
    result = json.loads(result_json_str)

    # Ensure result is a dictionary
    assert isinstance(result, dict), "Result should be a dictionary"

    # Validate basic structure
    assert "graph" in result, "Result should contain a 'graph' key"
    assert "nodes" in result["graph"], "Graph should contain nodes"
    assert "edges" in result["graph"], "Graph should contain edges"
    assert len(result["graph"]["nodes"]) > 0, "Graph should have at least one node"
    assert len(result["graph"]["edges"]) > 0, "Graph should have at least one edge"


def test_node_structure(mock_step1_data, mock_step2_data):
    """Test that generated nodes have valid structure."""
    from data.mock_pydantic.mockstep3 import extract_procedural_info

    section_name = "Registration procedure for initial registration"
    result_json_str = extract_procedural_info(
        section_name, mock_step1_data, mock_step2_data
    )
    result = json.loads(result_json_str)

    # Ensure result is a dictionary
    assert isinstance(result, dict), "Result should be a dictionary"

    assert "graph" in result
    assert "nodes" in result["graph"], "Graph should contain nodes"

    for node in result["graph"]["nodes"]:
        # Test required fields
        assert "id" in node, "Node missing id"
        assert "type" in node, "Node missing type"
        assert "description" in node, "Node missing description"
        assert "properties" in node, "Node missing properties"

        # Test valid node types
        assert node["type"] in VALID_NODE_TYPES, f"Invalid node type: {node['type']}"


def test_edge_structure(mock_step1_data, mock_step2_data):
    """Test that generated edges have valid structure."""
    from data.mock_pydantic.mockstep3 import extract_procedural_info

    section_name = "Registration procedure for initial registration"
    result_json_str = extract_procedural_info(
        section_name, mock_step1_data, mock_step2_data
    )
    result = json.loads(result_json_str)

    # Ensure result is a dictionary
    assert isinstance(result, dict), "Result should be a dictionary"

    assert "graph" in result
    assert "edges" in result["graph"], "Graph should contain edges"

    node_ids = {node["id"] for node in result["graph"]["nodes"]}

    for edge in result["graph"]["edges"]:
        # Test required fields
        assert "from" in edge, "Edge missing 'from' field"
        assert "to" in edge, "Edge missing 'to' field"
        assert "type" in edge, "Edge missing type"
        assert "properties" in edge, "Edge missing properties"

        # Test edge connections
        assert edge["from"] in node_ids, f"Edge from non-existent node: {edge['from']}"
        assert edge["to"] in node_ids, f"Edge to non-existent node: {edge['to']}"

        # Test edge type
        assert edge["type"] in [
            "sequential",
            "conditional",
        ], f"Invalid edge type: {edge['type']}"


def test_complete_graph_validation(mock_step1_data, mock_step2_data):
    """Test complete graph structure validation."""
    from data.mock_pydantic.mockstep3 import extract_procedural_info

    section_name = "Registration procedure for initial registration"
    result_json_str = extract_procedural_info(
        section_name, mock_step1_data, mock_step2_data
    )
    result = json.loads(result_json_str)

    # Ensure result is a dictionary
    assert isinstance(result, dict), "Result should be a dictionary"

    # Test overall structure
    assert "graph" in result
    assert "nodes" in result["graph"], "Graph should contain nodes"
    assert "edges" in result["graph"], "Graph should contain edges"

    # Test graph connectivity
    node_ids = {node["id"] for node in result["graph"]["nodes"]}
    edge_froms = {edge["from"] for edge in result["graph"]["edges"]}
    edge_tos = {edge["to"] for edge in result["graph"]["edges"]}

    # Every node should be connected
    assert edge_froms.union(edge_tos) == node_ids, "Graph should be fully connected"

    # Should have start and end nodes
    assert any(
        node["type"] == "start" for node in result["graph"]["nodes"]
    ), "Graph should have a start node"
    assert any(
        node["type"] == "end" for node in result["graph"]["nodes"]
    ), "Graph should have an end node"


def test_invalid_node_type():
    """Test that invalid node types are rejected."""
    invalid_graph = {
        "graph": {
            "nodes": [
                {
                    "id": "1",
                    "type": "invalid_type",  # Invalid type
                    "description": "Test node",
                    "properties": {},
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
            "nodes": [
                {
                    "id": "1",
                    "type": "state",
                    "description": "Test state",
                    "properties": {},
                }
            ],
            "edges": [
                {
                    "from": "1",
                    "to": "nonexistent",  # References non-existent node
                    "type": "sequential",
                    "properties": {},
                }
            ],
        }
    }
    assert not validate_data(invalid_graph), "Invalid edge reference should be rejected"
