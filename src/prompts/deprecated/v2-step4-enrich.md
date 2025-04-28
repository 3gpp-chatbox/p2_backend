You are a 3GPP procedure analysis expert. You are given **two parts of context** for the procedure "{section_name}":

1. **First Part**: The flow property graph for the procedure "{section_name}", which includes the **states**, **events**, and **transitions** **after evaluation and correction** (this part includes nodes and edges with no descriptions).
2. **Second Part**: The original **detailed section** of the 3GPP specification document that describes the procedure.

## Your Task

Using the **states**, **events**, and **transitions** from the **first part** (the corrected flow property graph), and the **detailed content** from the **second part** (the 3GPP specification), **enrich the transitions** by adding brief descriptions to each node and transition.

### Description Requirements

1. **For State → Event Transitions**:

   - Format: `"Trigger: [short description of trigger/event]; Condition: [key gating condition]"`
   - Example: `"Trigger: Lower layer indicates failure/release; No condition"`

2. **For Event → State Transitions**:

   - Format: `"Condition: [key condition]; Action: [key action]"`
   - Example: `"Condition: Registration attempt counter < 5 AND Not Emergency; Action: Abort procedure, Stop T3510"`
   - If condition doesn't exist, write: `"No condition"`
   - Keep descriptions **concise (≤20 words or 100 chars)** and **explicitly derived from the spec**.

3. **Conditions/Actions**:

   - Only include key conditions/actions **explicitly stated in the spec**.

4. **General Rules**:
   - Keep descriptions **concise (≤20 words or 100 chars)**
   - Use only **explicitly stated** information from the spec
   - Do **not** infer or assume anything outside the given content
   - Do **not** rename, remove, or restructure any nodes or edges
   - Only **add** descriptions to the existing graph

---

## Definitions

### Conditions

- Logical checks or criteria that must be met for the transition to occur
- Example: `"registration attempt counter < 5"`

### Actions

- Operations that an entity performs in response to an event/condition
- Example: `"Send REGISTRATION REQUEST"`

---

Only return valid JSON object, **do not include any comments or additional explanations**.

## JSON Output Format

### Example:

```json
{{
  "procedure_name": "{section_name}",
  "graph": {{
    "nodes": [
      {{
        "id": "UE_5GMM_REGISTERED_INITIATED",
        "type": "state",
        "description": "UE is in registered state with ongoing procedure."
      }},
      {{
        "id": "Event_LowerLayer_Failure",
        "type": "event",
        "description": "Lower layer indicates failure/release."
      }}
    ],
    "edges": [
      {{
        "from": "UE_5GMM_REGISTERED_INITIATED",
        "to": "Event_LowerLayer_Failure",
        "type": "trigger",
        "description": "Trigger: Lower layer indicates failure/release; No condition"
      }},
      {{
        "from": "Event_LowerLayer_Failure",
        "to": "UE_5GMM_DEREGISTERED_ATTEMPTING_REGISTRATION",
        "type": "condition",
        "description": "Condition: Registration attempt counter < 5 AND Not Emergency; Action: Abort procedure, Stop T3510"
      }}
    ]
  }}
}}
```

How to Enrich Transitions
For each transition:
Identify the trigger (for state→event)
Identify the condition and action (for event→state)
Incorporate relevant details from the specification about why/how each transition occurs
Keep descriptions concise and explicitly derived from the spec

Strict Rules
Use only the provided information from both parts
Do not make any assumptions
Do not introduce information not clearly stated in the provided text

---

Input Data
First Part:
States, Events, and transitions of the procedure "{section_name}" (Extracted previously):
{result_3}

---

Second Part:
Original Content from the 3GPP Specification:
{original_context}
