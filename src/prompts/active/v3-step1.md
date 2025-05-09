# Flow Property Graph Extraction

You will be provided with original content from 3GPP specification sections describing the procedure: "{procedure_name}".
Your task is to extract the **Flow Property Graph (FPG)** focusing specifically on the {entity} side of this procedure "{procedure_name}", and represent it as a structured JSON object following the format defined below.
**Do not infer or assume any information beyond what is explicitly stated in the provided text.** Focus only on the information that is directly described and avoid including anything implied.

---

## Objective

### Graph Structure

Build a unified Flow Property Graph focusing on the {entity} perspective where:

- **Nodes** represent **states or events** for {entity}
  - **States:** Explicitly named states from {entity}'s perspective (e.g., "5GMM-DEREGISTERED"). Do not invent or infer state names.
  - **Events:** Visible triggers such as received messages or expired timers from {entity}'s perspective (e.g., "Receive DEREGISTRATION REQUEST", "T3510 expires", "Lower layer failure"). Events describe occurrences/triggers that happen.
- **Edges** represent transitions between states and events. Each transition will be represented by **two directed edges**:
  - One from a state to an event
  - One from that event to the subsequent state
- Each edge must include a specific **type**:
  - "trigger": From state to event (state is triggered by event)
  - "condition": From event to state (event leads to state under conditions)
- **Edge Type Notes**:
  - All event→state transitions inherently represent actions, but currently map these to `"condition"` type edges
- Each node must be clearly identified with {entity} in the node name, like "{entity}\_5GMM_REGISTERED".
- For all event nodes, names should have prefix Event\_, like Event_LowerLayer_Failure.
- **Graph Connectivity**:
  - All nodes must be connected as part of one unified graph
  - There must be no isolated or dangling nodes
  - Every node must be reachable from every other node through some path in the graph
  - Any seemingly disconnected state or event must be properly connected to the main flow

---

## Core Components

### 1. States

- **Requirements**:
  - Include explicitly named states for {entity}
  - Format: "[ENTITY]\_[STATE_NAME]" (e.g., "{entity}\_5GMM_REGISTERED")
  - Do not invent or infer state names
  - Ensure each state is connected to at least one event

### 2. Events

- **Definition**:
  - These are **visible triggers** like messages received or timers expiring
  - Examples: `"Receive DEREGISTRATION REQUEST"`, `"T3510 expires"`
- **Requirements**:
  - Include events from {entity}'s perspective
  - Each event must be connected to at least one state through either incoming or outgoing edges

### 3. Conditions

- **Definition**: Logical checks or criteria that must be met for the transition to occur
- **Requirements**:
  - Include only if **explicitly described** in the specification
  - Must be directly associated with the triggering event
- **Example**: `"registration attempt counter < 5"`

### 4. Actions

- **Definition**: Operations that {entity} performs in response to events/conditions
- **Requirements**:
  - Must be explicitly stated — no inferences allowed
- **Example**: `"Send REGISTRATION REQUEST"`

### 5. Conditions and Actions Notes

- You may identify conditions and actions during analysis, but only include them as edge types in the final JSON
- Do not include condition/action details in the final output

---

## JSON Output Format

```json
{{
  "procedure_name": "{procedure_name}",
  "graph": {{
    "nodes": [
      {{"id": "{entity}_5GMM_REGISTERED_INITIATED", "type": "state"}},
      {{"id": "Event_LowerLayer_Failure", "type": "event"}},
      {{"id": "{entity}_5GMM_DEREGISTERED_ATTEMPTING_REGISTRATION", "type": "state"}}
    ],
    "edges": [
      {{
        "from": "{entity}_5GMM_REGISTERED_INITIATED",
        "to": "Event_LowerLayer_Failure",
        "type": "trigger"
      }},
      {{
        "from": "Event_LowerLayer_Failure",
        "to": "{entity}_5GMM_DEREGISTERED_ATTEMPTING_REGISTRATION",
        "type": "condition"
      }}
    ]
  }}
}}
```

## Constraints

- **Single Entity Focus**: Focus specifically on states and events from {entity}'s perspective
- **Unified Graph**: Ensure all nodes are connected into a single coherent graph with no isolated parts
- **No Inference**: Use only information that is explicitly stated in the input content
- **Multiple Paths**: If the spec describes alternate paths (e.g., emergency mode, failure recovery) for {entity}, include them all
- **Fallbacks**: Capture fallback or error handling flows if explicitly described for {entity}
- **Self-loops**: If a procedure describes retry or failure recovery that leads the {entity} back to the same state, include a transition from that state to itself. This is valid as long as the loop is explicitly described in the text

Input Text:
Analyze only the content below. Do not reference external knowledge:

{context}
