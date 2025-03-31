import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

def extract_procedural_info_from_text_v3(section_name, text):
    prompt = f"""
You are a 3GPP specification expert. Enhance the extracted procedure "{section_name}" by adding:
- **Decision points** (where the procedure branches based on conditions)
- **Fallback paths** (e.g., retries, failures, timeouts)
- **Dependencies** (which steps depend on others)
- **State transitions** (what changes in each step)

The updated output format:
{{
  "procedure_name": string,
  "steps": [
    {{
      "id": number,
      "description": string,
      "entities": string,
      "state_changes": string,
      "messages": [
        {{
          "name": string,
          "from": string,
          "to": string
        }}
      ],
      "trigger": string,
      "conditions": [
        {{
          "if": string,
          "then": number,
          "else": number,
          "timeout": string
        }}
      ],
      "dependencies": [
        {{
          "step": number,
          "depends_on": number,
          "type": "hard" | "soft" | "retry",
          "condition": string
        }}
      ],
      "alternative_paths": [
        {{
          "condition": string,
          "next_step": number
        }}
      ],
      "side_effects": string
    }}
  ]
}}

Enhance this extracted JSON by adding **alternative paths, decisions, and dependencies**:

"""

    try:
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            print("Error: Empty response from Gemini model")
            return None
            
        response_text = response.text.strip()
        print("\nRaw response from model:")
        print(response_text[:500] + "..." if len(response_text) > 500 else response_text)

        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()

        response_text = response_text.replace(",]", "]").replace(",}", "}")

        if not response_text:
            print("Error: Empty response after cleaning")
            return None

        parsed_response = json.loads(response_text)
        return parsed_response
        
    except json.JSONDecodeError as e:
        print(f"\nError parsing JSON response: {e}")
        print("\nFull raw response:")
        print(response_text if 'response_text' in locals() else "No response text available")
        return None
    except Exception as e:
        print(f"\nUnexpected error: {type(e).__name__}: {str(e)}")
        return None


def read_text_file(file_path):
    """Reads content from a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def save_procedural_info_to_json(procedural_info, file_path):
    with open(file_path, "w", encoding='utf-8') as file:
        # Ensure that the procedural_info is properly formatted as JSON
        json.dump(procedural_info, file, indent=2)
    print(f"Procedural info saved to {file_path}")

def process_text_file(input_file_path, section_name):
    """Processes content from a text file instead of database."""
    text_content = read_text_file(input_file_path)
    if text_content is None:
        return None
        
    procedural_info = extract_procedural_info_from_text_v3(section_name, text_content)
    return procedural_info

# Example usage: Processing a text file
input_file_path = "5.5.1.2.txt"  # Path to your input text file
section_name = "Primary authentication and key agreement procedure"  # Name of the section/procedure

procedural_info = process_text_file(input_file_path, section_name)

if procedural_info:
    save_procedural_info_to_json(procedural_info, "step2-v3.json")
else:
    print("Failed to extract procedural information")
