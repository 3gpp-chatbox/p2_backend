import json
from pathlib import Path

def convert_node_type_to_shape(node_type):
    """Convert node type to Mermaid shape."""
    shapes = {
        'start': '[',  # Box
        'end': '[',    # Box
        'process': '(',  # Round edges
        'decision': '{',  # Diamond
        'timer': '[[',   # Double box for timers
        'state': '((',   # Double circle for states
    }
    return shapes.get(node_type, '[')  # Default to box if type unknown

def create_mermaid_node(node):
    """Create a Mermaid node definition."""
    node_id = str(node['id'])
    node_type = node.get('type', 'process')
    description = node['description'].replace('"', "'")  # Replace quotes to avoid syntax issues
    
    shape_start = convert_node_type_to_shape(node_type)
    shape_end = shape_start.replace('[', ']').replace('(', ')').replace('{', '}')
    
    return f"{node_id}{shape_start}\"{description}\"{shape_end}"

def create_mermaid_edge(edge):
    """Create a Mermaid edge definition."""
    edge_type = edge.get('type', 'sequential')
    arrow = '-->' if edge_type == 'sequential' else '-..->' if edge_type == 'conditional' else '-->'
    
    return f"{edge['from']} {arrow} {edge['to']}"

def convert_to_mermaid(json_file, output_file):
    """Convert JSON graph to Mermaid flowchart."""
    try:
        # Read JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Start building Mermaid flowchart
        mermaid_lines = ['```mermaid', 'flowchart TD']
        
        # Add nodes
        for node in data['graph']['nodes']:
            mermaid_lines.append('    ' + create_mermaid_node(node))
        
        # Add edges
        for edge in data['graph']['edges']:
            mermaid_lines.append('    ' + create_mermaid_edge(edge))
        
        # Close Mermaid block
        mermaid_lines.append('```')
        
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(mermaid_lines))
            
        print(f"Successfully converted to Mermaid flowchart: {output_file}")
        
    except Exception as e:
        print(f"Error converting to Mermaid: {str(e)}")

if __name__ == "__main__":
    # Get the current directory
    current_dir = Path(__file__).parent.parent
    
    # Define input and output files
    input_file = current_dir / "version_3" / "step3-v3.json"
    output_file = current_dir / "version_3" / "flowchart-v3.md"
    
    print(f"Converting {input_file} to Mermaid flowchart...")
    convert_to_mermaid(input_file, output_file)