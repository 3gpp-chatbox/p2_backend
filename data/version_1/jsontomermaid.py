import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

flash_model = "gemini-2.0-flash"
pro_model = "gemini-2.0-pro-exp-02-05"

# Load the Google API Key from the .env file
load_dotenv(override=True)

# Get API key from environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found in environment variables. Please set it in your .env file."
    )

# Configure the API key
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel(flash_model)

def extract_procedural_info_from_text(section_name, text):
    prompt = f"""
Convert the provided JSON code to Mermaid flowchart syntax. Use this exact format:

```mermaid
flowchart TD
    start([Start]) --> ...
    ... other nodes and connections ...
    ... --> finish([End])
```

Rules for valid Mermaid syntax:
1. Each node must have a unique ID (not using reserved words like 'end')
2. Use proper node declarations:
   - ([text]) for rounded boxes (start/end)
   - [text] for regular boxes
   - {{text}} for curved boxes
   - (text) for circles
   - >text] for flags
3. Connections must use proper arrows:
   - --> for normal flow
   - -.-> for dashed lines
   - ==> for thick lines
4. Add labels to edges using |text| syntax
5. For decision nodes, use diamond shape: {{{{text}}}}

Please convert my provided JSON code to a valid Mermaid flowchart following these rules.

Input JSON:
{text}
"""

    model_to_use = flash_model  # or pro_model depending on your requirement
    response = model.generate_content(
        contents=prompt,
        generation_config={
            "temperature": 0,
        },
    )

    # Extract the text content from the response
    procedural_info = response.text.strip() if hasattr(response, 'text') else str(response)
    
    # Clean up the response to ensure it only contains the Mermaid diagram
    if "```mermaid" in procedural_info:
        procedural_info = procedural_info[procedural_info.find("```mermaid"):].strip()
        procedural_info = procedural_info.replace("```mermaid", "").replace("```", "").strip()

    return procedural_info

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

def save_procedural_info_to_md(procedural_info, file_path):
    """Saves the Mermaid diagram to a markdown file with proper formatting."""
    with open(file_path, "w", encoding='utf-8') as file:
        file.write("# Registration Procedure Flow\n\n")  # Add a title
        file.write("```mermaid\n")  # Start Mermaid code block
        file.write(procedural_info.strip())  # Write the diagram
        file.write("\n```\n")  # End Mermaid code block
    print(f"Mermaid diagram saved to {file_path}")

def process_text_file(input_file_path, section_name):
    """Processes content from a text file instead of database."""
    text_content = read_text_file(input_file_path)
    if text_content is None:
        return None
        
    procedural_info = extract_procedural_info_from_text(section_name, text_content)
    return procedural_info

# Example usage: Processing a text file
input_file_path = "step3.json"  # Path to your input text file
section_name = "Registration procedure for initial registration"  # Name of the section/procedure

procedural_info = process_text_file(input_file_path, section_name)

if procedural_info:
    save_procedural_info_to_md(procedural_info, "mermaid.md")
else:
    print("Failed to extract procedural information")
