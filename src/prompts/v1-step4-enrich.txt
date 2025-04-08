You are a 3GPP procedure analysis expert. You are given **two parts of context** for the procedure "{section_name}":

1. **First Part**: The flow property graph for the procedure "{section_name}", which includes the **states**, **events**, and **transitions** **after evaluation and correction** (this part includes nodes and edges with no descriptions).
2. **Second Part**: The original **detailed section** of the 3GPP specification document that describes the procedure.

### 🎯 Your task:
Using the **states**, **events**, and **transitions** from the **first part** (the corrected flow property graph), and the **detailed content** from the **second part** (the 3GPP specification), **enrich the transitions** in the following way:

1. **Descriptions**: Add a **brief description** to each transition, specifying **what causes the transition** (e.g., "triggered by UE sending Attach Request").
2. **Conditions**: If a transition depends on **certain conditions** (e.g., successful authentication), identify those conditions and add them to the transition description.

### 💡 Example Output Format:
Your output should look like this:

Please ensure your output follows the format below:

example output format 
```json
{{
  "procedure_name": "procedure name",
  "graph": {{
    "nodes": [
      {{
        "id": "UE_Powered_On",
        "type": "state",
        "description": "UE is powered on but not yet attached to the network."
      }},
      {{
        "id": "Attach_Request_Received",
        "type": "event",
        "description": "The network receives an Attach Request from the UE."
      }},
      {{
        "id": "UE_Attaching",
        "type": "state",
        "description": "UE is undergoing the attachment procedure."
      }},
      {{
        "id": "Authentication_Challenge",
        "type": "event",
        "description": "The network sends an Authentication Challenge to the UE."
      }},
      {{
        "id": "UE_Authenticating",
        "type": "state",
        "description": "UE is responding to the authentication procedure."
      }}
    ],
    "edges": [
      {{
        "from": "UE_Powered_On",
        "to": "Attach_Request_Received",
        "type": "trigger",
        "description": "Triggered when UE initiates attachment by sending an Attach Request."
      }},
      {{
        "from": "Attach_Request_Received",
        "to": "UE_Attaching",
        "type": "condition",
        "description": "Network accepts the attach request and begins attachment."
      }},
      {{
        "from": "UE_Attaching",
        "to": "Authentication_Challenge",
        "type": "trigger",
        "description": "Network challenges the UE for authentication."
      }},
      {{
        "from": "Authentication_Challenge",
        "to": "UE_Authenticating",
        "type": "condition",
        "description": "Transition occurs if UE responds to the challenge correctly."
      }}
    ]
  }}
}}

How to Enrich Transitions:
For each transition, identify the trigger and the condition that causes the transition from one state to another.
Incorporate any details from the specification about why or how each transition occurs (e.g., "triggered when UE attaches", "transition happens if authentication is successful").
If no conditions or explicit triggers are provided in the spec, you may leave those parts blank, but ensure they are still logically inferred from the spec.

Strict Rule:
You must only use the provided information in the first part and second part.
Do not make any assumptions or introduce information not clearly stated in the provided text.
Provide the exact descriptions and conditions based on what is described in the 3GPP specification.


First Part:
States, Events, and transitions of the procedure "{section_name}" (Extracted previously):
{json.dumps(extracted_data, indent=2)}

------------------
Second Part:
Original Content from the 3GPP Specification:
{original_content}