"""Tests for JSON to Mermaid conversion functionality."""

import pytest
import json
import os
from src.jsontomermaid import escape_node_text, escape_edge_text

def test_escape_node_text():
    """Test node text escaping functionality."""
    # Test parentheses escaping
    assert escape_node_text("test (with parentheses)") == r"test \(with parentheses\)"
    
    # Test quotes escaping
    assert escape_node_text('test "with quotes"') == r'test &quot;with quotes&quot;'
    
    # Test combined escaping
    assert escape_node_text('test (with "everything")') == r'test \(with &quot;everything&quot;\)'

def test_escape_edge_text():
    """Test edge text escaping functionality."""
    # Test parentheses escaping
    assert escape_edge_text("test (with parentheses)") == "test &#40;with parentheses&#41;"
    
    # Test quotes escaping
    assert escape_edge_text('test "with quotes"') == 'test &quot;with quotes&quot;'
    
    # Test combined escaping
    assert escape_edge_text('test (with "everything")') == 'test &#40;with &quot;everything&quot;&#41;'

def test_mermaid_conversion(tmp_path):
    """Test full JSON to Mermaid conversion."""
    # Create test JSON data
    test_data = {
        "graph": {
            "nodes": [
                {"id": "node1", "type": "state", "description": "Test State (initial)"},
                {"id": "node2", "type": "event", "description": "Test Event"}
            ],
            "edges": [
                {
                    "from": "node1",
                    "to": "node2",
                    "type": "trigger",
                    "description": "Test Edge (with condition)"
                }
            ]
        }
    }
    
    # Create temporary JSON file
    json_file = tmp_path / "test.json"
    with open(json_file, "w") as f:
        json.dump(test_data, f)
    
    # Create temporary output file
    output_file = tmp_path / "test_mermaid.md"
    
    # Import the conversion function
    from src.jsontomermaid import convert_json_to_mermaid
    
    # Convert JSON to Mermaid
    convert_json_to_mermaid(str(json_file), str(output_file))
    
    # Read and verify the output
    with open(output_file, "r") as f:
        mermaid_content = f.read()
    
    # Check if the output contains expected elements
    assert "```mermaid" in mermaid_content
    assert "graph TD" in mermaid_content
    assert r"node1[\"Test State \(initial\)\"]" in mermaid_content
    assert "node2[\"Test Event\"]" in mermaid_content
    assert "node1 -->|Test Edge &#40;with condition&#41;| node2" in mermaid_content
    assert "```" in mermaid_content

def test_invalid_json(tmp_path):
    """Test handling of invalid JSON input."""
    # Create invalid JSON file
    invalid_json = tmp_path / "invalid.json"
    with open(invalid_json, "w") as f:
        f.write("{invalid json}")
    
    # Create output file
    output_file = tmp_path / "invalid_output.md"
    
    # Import the conversion function
    from src.jsontomermaid import convert_json_to_mermaid
    
    # Test that it raises an exception for invalid JSON
    with pytest.raises(json.JSONDecodeError):
        convert_json_to_mermaid(str(invalid_json), str(output_file))

def test_missing_file():
    """Test handling of missing input file."""
    from src.jsontomermaid import convert_json_to_mermaid
    
    # Test that it raises an exception for missing file
    with pytest.raises(FileNotFoundError):
        convert_json_to_mermaid("nonexistent.json", "output.md") 