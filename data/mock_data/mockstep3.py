import json
import os
import sys

import google.generativeai as genai
from dotenv import load_dotenv

# Add p2_backend/src to Python path
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src")
)
from src.schema_validation import validate_data

load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")


def read_json_file(file_path):
    """Reads content from a JSON file and returns the parsed JSON object."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
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
You are an expert in telecom procedures and standards, particularly in 3GPP specifications.
Your task is to extract the **Initial Registration Procedure** based on the TS 24.501 specification.
The procedure should be structured in the following way:

1. **States and Events(Nodes)**: Represent different stages in the process (e.g., 'UE Registered', 'Authentication Successful').
   - For each state, provide a **unique identifier**, **description**, and **type** (either 'state' or 'event').
   - Example: {{'id': 'state1', 'type': 'state', 'description': 'UE Registered'}}

2. **Triggers and Conditions (Edges)**: Represent the relationships between states.
   - For each edge, provide the **starting node** (from_node), **target node** (to), **type** (either 'trigger' or 'condition'),
     and a **description** of the trigger or condition.
   - Example: {{'from': 'state1', 'to': 'state2', 'type': 'trigger', 'description': 'Authentication Success'}}

Please format your output as a structured JSON object (without any markdown code block markers):

{{
  "graph": {{
    "nodes": [
      {{"id": "state1", "type": "state", "description": "UE Registered"}},
      {{"id": "event1", "type": "event", "description": "UE Sends Registration Request"}}
    ],
    "edges": [
      {{"from": "state1", "to": "event1", "type": "trigger", "description": "Power On"}},
      {{"from": "event1", "to": "state2", "type": "condition", "description": "Authentication Success"}}
    ]
  }}
}}

### Input Data:
#### Extracted Procedure Steps:
{json.dumps(step1_data, indent=2)}

#### Decision Points & Dependencies:
{json.dumps(step2_data, indent=2)}
"""

    # Generate content using Gemini model
    response = model.generate_content(
        contents=prompt,
        generation_config={
            "temperature": 0,
        },
    )

    # Print the raw response to inspect its structure
    print(f"Raw response from model:\n{response.text}")

    # Check if response is empty
    if not response.text:
        print("Error: Empty response received.")
        return None

    # Clean up the response by removing markdown code block markers
    cleaned_response = response.text.strip()
    if cleaned_response.startswith("```"):
        cleaned_response = cleaned_response.split("\n", 1)[1]  # Remove first line
    if cleaned_response.endswith("```"):
        cleaned_response = cleaned_response.rsplit("\n", 1)[0]  # Remove last line
    if cleaned_response.startswith("json"):
        cleaned_response = cleaned_response.split("\n", 1)[1]  # Remove "json" line

    # Try to parse the JSON response
    try:
        parsed_response = json.loads(cleaned_response)
        # Validate the parsed response using Pydantic models
        if validate_data(parsed_response):
            return parsed_response
        else:
            print("Error: Validation failed.")
            return None
    except json.JSONDecodeError as e:
        print(f"✗ Failed to decode JSON from the extracted data: {e}")
        return None


def save_to_json(data, file_path):
    """Saves procedural info to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(f"Procedural info saved to {file_path}")


def process_procedure(section_name):
    """Processes the procedure using step1.json and step2.json as input."""

    step1_data = read_json_file("data/mock_pydantic/mockstep1.json")
    step2_data = read_json_file("data/mock_pydantic/mockstep2.json")

    if step1_data is None or step2_data is None:
        print("Failed to load step1.json or step2.json")
        return None

    procedural_info = extract_procedural_info(section_name, step1_data, step2_data)
    return procedural_info


# Example usage: Processing the procedure with step1.json and step2.json
section_name = "Registration procedure for initial registration"

procedural_info = process_procedure(section_name)

if procedural_info:
    save_to_json(procedural_info, "data/mock_pydantic/mockstep3.json")
else:
    print("Failed to extract procedural information")
