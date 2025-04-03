import json

# Function to escape parentheses and double quotes
def escape_text(text):
    return text.replace("(", "&#40;").replace(")", "&#41;").replace('"', "&quot;")

# Load JSON data from a file
with open("data/version_4/step3-v4.json", "r", encoding="utf-8") as f:
    graph_data = json.load(f)

# Initialize Mermaid diagram
mermaid_code = "```mermaid\ngraph TD;\n"

# Add nodes
node_map = {}  # Store node descriptions
for node in graph_data["graph"]["nodes"]:
    node_id = node["id"]
    description = escape_text(node["description"])  # Escape text
    node_map[node_id] = description
    mermaid_code += f'  {node_id}["{description}"];\n'

# Add edges
for edge in graph_data["graph"]["edges"]:
    from_node = edge["from"]
    to_node = edge["to"]
    edge_label = escape_text(edge["description"])  # Escape text
    mermaid_code += f'  {from_node} -->|{edge_label}| {to_node};\n'

# Close the Mermaid code block
mermaid_code += "```\n"

# Save to file
with open("data/version_4/mermaid.md", "w", encoding="utf-8") as f:
    f.write(mermaid_code)

print("Mermaid diagram saved to mermaid.md")
