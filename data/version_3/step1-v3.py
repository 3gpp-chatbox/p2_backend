import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
from pathlib import Path

load_dotenv()

# Check API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

# Configure API key
genai.configure(api_key=api_key)

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

def extract_procedural_info_from_text_v3(section_name, text):
    if not text:
        print("Error: Empty input text")
        return None

    print(f"Processing text of length: {len(text)} characters")
    prompt = f"""
You are a 3GPP specification expert. Extract the detailed flow of the procedure "{section_name}" from the provided context. 

Return a JSON object with the following structure, ensuring NO duplicate keys and NO truncated strings:
{{
  "procedure_name": string,
  "steps": [
    {{
      "id": number,
      "description": string,  // Main step description
      "entities": string,     // Comma-separated list of entities
      "state_changes": string,
      "messages": [
        {{
          "name": string,
          "from": string,
          "to": string
        }}
      ],
      "trigger": string,      // Single trigger description
      "conditions": string,   // All conditions in one string
      "side_effects": string  // All side effects in one string
    }}
  ]
}}

Rules:
1. Keep all strings complete - do not truncate
2. Use only the fields shown above
3. Combine related information into single strings
4. Ensure valid JSON format
5. Maximum 6 main steps
6. Keep descriptions concise

Context:
{text}
"""

    try:
        # Generate response
        response = model.generate_content(prompt)
        
        # Check if response is valid
        if not response or not response.text:
            print("Error: Empty response from Gemini model")
            return None
            
        # Get response text
        response_text = response.text.strip()
        print("\nRaw response from model:")
        print(response_text[:500] + "..." if len(response_text) > 500 else response_text)
        
        # Clean the response
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()
            
        # Remove any trailing commas before closing braces/brackets
        response_text = response_text.replace(",]", "]").replace(",}", "}")
        
        # Parse the response into JSON
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
    # Convert to absolute path for clarity
    abs_path = os.path.abspath(input_file_path)
    if not os.path.exists(abs_path):
        print(f"Error: File not found at {abs_path}")
        return None
        
    print(f"Reading file: {abs_path}")
    text_content = read_text_file(abs_path)
    if text_content is None:
        return None
        
    procedural_info = extract_procedural_info_from_text_v3(section_name, text_content)
    return procedural_info

# Example usage: Processing a text file
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "5.5.1.2.txt")
section_name = "Registration procedure for initial registration"

print(f"Current directory: {current_dir}")
print(f"Looking for file: {input_file_path}")

procedural_info = process_text_file(input_file_path, section_name)

if procedural_info:
    output_file = os.path.join(current_dir, "step1-v3.json")
    save_procedural_info_to_json(procedural_info, output_file)
else:
    print("Failed to extract procedural information")
