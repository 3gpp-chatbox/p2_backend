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
    
    # Create the structured JSON-like string manually
    prompt = (
        f"You are an expert in telecom procedures and standards, particularly in 3GPP specifications. "
        f"Your task is to extract the **Initial Registration Procedure** based on the TS 24.501 specification. "
        f"The procedure should be structured in the following way:\n\n"
        f"1. **States (Nodes)**: Represent different stages in the process (e.g., 'UE Registered', 'Authentication Successful').\n"
        f"   - For each state, provide a **unique identifier**, **description**, **message**, and **type** (either 'state' or 'event').\n"
        f"   - Example: {{'id': 'state1', 'type': 'state', 'description': 'UE Registered', 'message': 'REGISTRATION REQUEST'}}\n\n"
        f"2. **Triggers and Conditions (Edges)**: Represent the relationships between states.\n"
        f"   - For each edge, provide the **starting node** (from_node), **target node** (to), **type** (either 'trigger' or 'condition'), "
        f"and a **description** of the trigger or condition.\n"
        f"   - Example: {{'from': 'state1', 'to': 'state2', 'type': 'trigger', 'description': 'Authentication Success'}}\n\n"
        f"Please format your output as a structured JSON-like object with the following format:\n\n"
        f"{{\n"
        f"  'graph': {{\n"
        f"    'nodes': [\n"
        f"      {{'id': 'state1', 'type': 'state', 'description': 'UE Registered'}},\n"
        f"      {{'id': 'event1', 'type': 'event', 'description': 'UE Sends Registration Request'}}\n"
        f"    ],\n"
        f"    'edges': [\n"
        f"      {{'from': 'state1', 'to': 'event1', 'type': 'trigger', 'description': 'Power On'}},\n"
        f"      {{'from': 'event1', 'to': 'state2', 'type': 'condition', 'description': 'Authentication Success'}}\n"
        f"    ]\n"
        f"  }}\n"
        f"}}\n\n"
        f"### Input Data:\n"
        f"#### Extracted Procedure Steps:\n"
        f"{json.dumps(step1_data, indent=2)}\n\n"
        f"#### Decision Points & Dependencies:\n"
        f"{json.dumps(step2_data, indent=2)}\n"
    )

    # Generate content using the model
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
