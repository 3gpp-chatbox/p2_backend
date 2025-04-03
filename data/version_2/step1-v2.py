# Primary authentication and key agreement procedure - TXT file version
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

# Define the model name
flash_model = "gemini-2.0-flash"

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel(flash_model)

def extract_procedural_info_from_text(section_name, text):
    prompt = f"""
You are a **3GPP procedure extraction tool**. Using your knowledge of 3GPP procedures, but strictly based on the provided text, **extract the high-level flow and key properties** of the procedure **"{section_name}"**.

---

## **🔹 What to Extract (Fixed Scope)**
Extract the following **essential elements** while preserving the cause-effect structure:  
- **Steps**: Actions performed by the **UE, AMF, or other entities**.
- **Messages**: Key messages exchanged (**e.g., REGISTRATION REQUEST, REGISTRATION ACCEPT**).
- **State Changes**: The **main state transitions** of the UE (**e.g., 5GMM-DEREGISTERED → 5GMM-REGISTERED**).
- **Timers**: Important timers started or stopped.
- **Entities**: The entity performing each step (**UE, AMF, etc.**).

🚨 **Strict Rule**: Do **not** make assumptions or introduce information beyond the provided text.  

---

## **🔹 How to Extract (Refinable Method)**
 

Follow these key principles when extracting data:  
- Identify the **main sequence of steps** in the procedure.  
- Capture how **messages influence state changes** or **start timers**.  
- Preserve the **exact cause-effect relationships** mentioned in the text.  


---


Output the information in the following JSON format:


{{
  "procedure_name": "{section_name}",
  "steps": [
    {{
      "id": 1,
      "step": "Description of the first main step",
      "state_before": "Initial UE state",
      "entity": "UE or AMF"
    }},
    {{
      "id": 2,
      "step": "Description of the second main step",
      "state_after": "State after step 1",
      "entity": "UE or AMF"
    }},
    // ... more steps ...
  ],
  "messages": [
    {{
      "name": "Message name",
      "from": "UE or AMF",
      "to": "UE or AMF"
    }},
    // ... more messages ...
  ],
  "timers": [
    {{
      "name": "Timer name",
      "action": "start or stop",
      "step_id": 1
    }},
    // ... more timers ...
  ]
}}

Provided Context:
{text}
"""

    response = model.generate_content(
        contents=prompt,
        generation_config={
            "temperature": 0,
        }
    )

    return response.text.strip()

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
        file.write(procedural_info)
    print(f"Procedural info saved to {file_path}")

def process_text_file(input_file_path, section_name):
    """Processes content from a text file instead of database."""
    text_content = read_text_file(input_file_path)
    if text_content is None:
        return None
        
    procedural_info = extract_procedural_info_from_text(section_name, text_content)
    return procedural_info

# Example usage: Processing a text file
input_file_path = "5.5.1.2.txt"  # Path to your input text file
section_name = "Registration procedure for initial registration"  # Name of the section/procedure

procedural_info = process_text_file(input_file_path, section_name)

if procedural_info:
    save_procedural_info_to_json(procedural_info, "v02-step1.json")
else:
    print("Failed to extract procedural information")