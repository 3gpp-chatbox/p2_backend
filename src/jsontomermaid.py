import json

# Function to escape text for nodes
def escape_node_text(text):
    return text.replace("(", "\(").replace(")", "\)").replace('"', "&quot;")

# Function to escape text for edge labels
def escape_edge_text(text):
    return text.replace("(", "&#40;").replace(")", "&#41;").replace('"', "&quot;")

# Load JSON data from a file
with open("data/version_1/step3.json", "r", encoding="utf-8") as f:
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
    edge_label = escape_edge_text(edge["description"])  # Escape text for edge labels
    mermaid_code += f'  {from_node} -->|{edge_label}| {to_node};\n'

# Close the Mermaid code block
mermaid_code += "```\n"

# Save to file
with open("data/version_1/mermaid.md", "w", encoding="utf-8") as f:
    f.write(mermaid_code)

print("Mermaid diagram saved to mermaid.md")
