import json

# Load JSON data from a file
with open("step3.json", "r", encoding="utf-8") as f:
    graph_data = json.load(f)

# Initialize Mermaid diagram
mermaid_code = "```mermaid\ngraph TD;\n"

# Add nodes
node_map = {}  # Store node descriptions
for node in graph_data["graph"]["nodes"]:
    node_id = node["id"]
    description = node["description"]
    node_map[node_id] = description
    mermaid_code += f'  {node_id}["{description}"];\n'

# Add edges
for edge in graph_data["graph"]["edges"]:
    from_node = edge["from"]
    to_node = edge["to"]
    edge_label = edge["description"]
    mermaid_code += f'  {from_node} -->|{edge_label}| {to_node};\n'

# Close the Mermaid code block
mermaid_code += "```\n"

# Save to file
with open("mermaid.md", "w", encoding="utf-8") as f:
    f.write(mermaid_code)

print("Mermaid diagram saved to output.md!")
