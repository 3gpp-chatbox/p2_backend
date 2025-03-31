import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

def read_json_file(file_path):
    """Reads content from a JSON file and returns the parsed JSON object."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def extract_procedural_info(section_name, step1_data, step2_data):
    """Generates a structured **flow property graph** using data from step1.json and step2.json"""
    
    prompt = f"""
You are a graph generation tool. Using your knowledge of 3GPP procedures but based on the provided input data, construct a structured **flow property graph** for the procedure "{section_name}".

### Represent:
- The sequence of steps as nodes, including their descriptions and any relevant properties (e.g., state changes, involved entities, triggers).
- The flow between steps as edges, including their types (sequential, conditional, retry) and any associated conditions.
- Decision points and timers as specific node types, with their conditions, properties, and multiple outcomes if applicable.
- Dependencies, retry conditions, and fallback paths as edge properties.

Ensure the graph:
- Clearly shows the main flow and alternative paths.
- Includes detailed properties for each node and edge, such as conditions, outcomes, retries, and reasons for transitions.
- Captures retry counts, error types, timeouts, and fallback paths where applicable.

### Example Output Format:

{{
  "graph": {{
    "nodes": [
      {{
        "id": "start",
        "type": "start",
        "description": "Procedure starts",
        "properties": {{}}
      }},
      {{
        "id": "1",
        "type": "process",
        "description": "UE sends REGISTRATION REQUEST",
        "properties": {{
          "state_change": "N/A",
          "entity": "UE",
          "messages": ["REGISTRATION REQUEST"]
        }}
      }},
      {{
        "id": "2",
        "type": "timer",
        "description": "Timer T3510 starts",
        "properties": {{
          "action": "start",
          "timeout": "5 seconds"
        }}
      }},
      {{
        "id": "3",
        "type": "decision",
        "description": "Decision based on timer expiration",
        "properties": {{
          "condition": "Timer T3510 expires",
          "outcomes": [
            {{
              "outcome": "Success",
              "next_step": 4
            }},
            {{
              "outcome": "Failure - Retry",
              "next_step": 2,
              "reason": "Timeout"
            }}
          ]
        }}
      }},
      {{
        "id": "4",
        "type": "process",
        "description": "AMF processes REGISTRATION REQUEST",
        "properties": {{
          "state_change": "5GMM-DEREGISTERED → 5GMM-REGISTERED",
          "entity": "AMF",
          "messages": ["REGISTRATION ACCEPT"]
        }}
      }}
    ],
    "edges": [
      {{
        "from": "start",
        "to": "1",
        "type": "sequential",
        "properties": {{
          "trigger": "UE sends REGISTRATION REQUEST"
        }}
      }},
      {{
        "from": "1",
        "to": "2",
        "type": "sequential",
        "properties": {{
          "trigger": "Timer T3510 starts"
        }}
      }},
      {{
        "from": "2",
        "to": "3",
        "type": "conditional",
        "properties": {{
          "condition": "Timer T3510 expires",
          "error_type": "Timeout",
          "retry_count": 3
        }}
      }},
      {{
        "from": "3",
        "to": "4",
        "type": "sequential",
        "properties": {{
          "trigger": "AMF sends REGISTRATION ACCEPT"
        }}
      }}
    ]
  }}
}}


### Input Data:
#### Extracted Procedure Steps:
{json.dumps(step1_data, indent=2)}

#### Decision Points & Dependencies:
{json.dumps(step2_data, indent=2)}
"""

    response = model.generate_content(prompt).text.strip()
    return response

def save_to_json(data, file_path):
    """Saves procedural info to a JSON file."""
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(data)
    print(f"Procedural info saved to {file_path}")

def process_procedure(section_name):
    """Processes the procedure using step1.json and step2.json as input."""
    
    step1_data = read_json_file("step1.json")
    step2_data = read_json_file("step2.json")

    if step1_data is None or step2_data is None:
        print("Failed to load step1.json or step2.json")
        return None

    procedural_info = extract_procedural_info(section_name, step1_data, step2_data)
    return procedural_info

# Example usage: Processing the procedure with step1.json and step2.json
section_name = "Registration procedure for initial registration"

procedural_info = process_procedure(section_name)

if procedural_info:
    save_to_json(procedural_info, "step3.json")
else:
    print("Failed to extract procedural information")
