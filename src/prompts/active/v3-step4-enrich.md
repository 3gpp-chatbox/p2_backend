# Flow Property Graph Enrichment

## Input

You are a 3GPP procedure analysis expert. You are given **two parts of context** for the procedure "{section_name}":

1. **First Part**: The unified flow property graph for the procedure "{section_name}" focusing on the {entity} perspective, which includes:
   - States
   - Events
   - Transitions (after evaluation and correction)
   - No existing descriptions for nodes and edges

2. **Second Part**: The original **detailed section** of the 3GPP specification document that describes the procedure.

## Task Description

> **Important**: Using the corrected flow property graph and the specification content, **enrich the transitions** by adding brief descriptions to each node and transition, focusing on the {entity}'s perspective while maintaining the unified graph structure.

### 1. Description Requirements

#### State → Event Transitions (from {entity}'s perspective)
- Format: `"Trigger: [short description of trigger/event]; Condition: [key gating condition]"`
- Example: `"Trigger: Lower layer indicates failure/release; No condition"`
- Describe the role of this transition in the overall flow

#### Event → State Transitions (from {entity}'s perspective)
- Format: `"Condition: [key condition]; Action: [key action]"`
- Example: `"Condition: Registration attempt counter < 5 AND Not Emergency; Action: Abort procedure, Stop T3510"`
- If condition doesn't exist, write: `"No condition"`
- Keep descriptions **concise (≤20 words or 100 chars)**
- Include transition's connection to other states when relevant

#### Conditions/Actions
- Only include key conditions/actions **explicitly stated** in the spec
- Note conditions that affect procedure flow
- Must be relevant to {entity}

### 2. General Rules
- Keep descriptions **concise (≤20 words or 100 chars)**
- Use only **explicitly stated** information from the spec
- Focus on {entity}'s perspective and actions
- Maintain coherent flow in descriptions
- Do **not** infer or assume anything outside the given content
- Do **not** rename, remove, or restructure any nodes or edges
- Only **add** descriptions to the existing graph

---

## Component Definitions

### Conditions
- Logical checks or criteria that must be met for the {entity}'s transition to occur
- Example: `"registration attempt counter < 5"`

### Actions
- Operations that {entity} performs in response to an event/condition
- Example: `"Send REGISTRATION REQUEST"`

---

## JSON Output Format

> **Note**: Only return valid JSON object, **do not include any comments or additional explanations**.

### Example Format:

```json
{{
  "procedure_name": "{section_name}",
  "graph": {{
    "nodes": [
      {{
        "id": "{entity}_5GMM_REGISTERED_INITIATED",
        "type": "state",
        "description": "{entity} is in registered state with ongoing procedure."
      }},
      {{
        "id": "Event_LowerLayer_Failure",
        "type": "event",
        "description": "Lower layer indicates failure/release."
      }}
    ],
    "edges": [
      {{
        "from": "{entity}_5GMM_REGISTERED_INITIATED",
        "to": "Event_LowerLayer_Failure",
        "type": "trigger",
        "description": "Trigger: Lower layer indicates failure/release; No condition"
      }},
      {{
        "from": "Event_LowerLayer_Failure",
        "to": "{entity}_5GMM_DEREGISTERED_ATTEMPTING_REGISTRATION",
        "type": "condition",
        "description": "Condition: Registration attempt counter < 5; Action: Abort procedure, Stop T3510"
      }}
    ]
  }}
}}
```

## Process Guidelines

### Enriching Transitions
1. Identify the trigger (for state→event) from {entity}'s perspective
2. Identify the condition and action (for event→state) from {entity}'s perspective
3. Describe the transition's role in the overall procedure
4. Keep descriptions concise and explicitly derived from the spec

### Strict Rules
- Use only the provided information from both parts
- Focus solely on {entity}'s perspective and actions
- Ensure descriptions maintain graph coherence
- Do not make any assumptions
- Do not introduce information not clearly stated in the provided text

---

## Input Data

### First Part
States, Events, and transitions of the procedure "{section_name}" (Extracted previously):

{result_3}

### Second Part
Original Content from the 3GPP Specification:

{original_context}
