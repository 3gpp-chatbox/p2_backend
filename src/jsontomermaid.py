import json


# Function to escape text for nodes
def escape_node_text(text):
    return text.replace("(", r"\(").replace(")", r"\)").replace('"', "&quot;")


# Function to escape text for edge labels
def escape_edge_text(text):
    return text.replace("(", "&#40;").replace(")", "&#41;").replace('"', "&quot;")


def convert_json_to_mermaid(input_file, output_file):
    """Convert JSON graph data to Mermaid diagram format.

    Args:
        input_file (str): Path to input JSON file
        output_file (str): Path to output Mermaid markdown file
    """
    # Load JSON data from a file
    with open(input_file, "r", encoding="utf-8") as f:
        graph_data = json.load(f)

    # Initialize Mermaid diagram
    mermaid_code = "```mermaid\ngraph TD;\n"

    # Add nodes
    node_map = {}  # Store node descriptions
    for node in graph_data["graph"]["nodes"]:
        node_id = node["id"]
        description = escape_node_text(node["description"])  # Escape text for nodes
        node_map[node_id] = description
        mermaid_code += f'  {node_id}["{description}"];\n'

    # Add edges
    for edge in graph_data["graph"]["edges"]:
        from_node = edge["from"]
        to_node = edge["to"]
        edge_label = escape_edge_text(
            edge["description"]
        )  # Escape text for edge labels
        mermaid_code += f"  {from_node} -->|{edge_label}| {to_node};\n"

    # Close the Mermaid code block
    mermaid_code += "```\n"

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(mermaid_code)


if __name__ == "__main__":
    # When run as a script, process version_1 by default
    input_file = "data/test_input.json"
    output_file = "data/test_output.md"
    convert_json_to_mermaid(input_file, output_file)
    print(f"Mermaid diagram saved to {output_file}")
