# 3GPP Flow Property Graph Analysis

You are a 3GPP specification analyzer tasked with processing the procedure "{procedure_name}" from the {entity}'s perspective. Your objective is to construct a unified Flow Property Graph (FPG) representation based strictly on the provided specification text.

> **Important**: Do not infer or assume any information beyond what is explicitly stated in the provided text. Focus only on the information that is directly described and avoid including anything implied.

## Input

Original 3GPP specification section detailing the procedure "{procedure_name}".

## Task Objective

### Primary Goal
Extract and structure the procedure's flow from the {entity}'s perspective into a formal unified graph representation capturing states, events, and transitions between them. All components must be connected into a single coherent graph with no isolated parts.

### Graph Components

1. **Nodes** (Two Types):

   - **States**:

     - Explicitly defined states of {entity}
     - Format: "[ENTITY]\_[STATE_NAME]"
     - Example: "{entity}_5GMM_REGISTERED"
     - Must be connected to at least one event

   - **Events**:
     - Observable triggers from {entity}'s perspective (messages, timer expiration)
     - Format: "Event\_[EVENT_NAME]"
     - Example: "Event_Receive_REGISTRATION_REQUEST", "Event_T3510_Expires"
     - Must be connected to at least one state through incoming or outgoing edges

2. **Edges** (Two Types):
   - **State → Event** (type: "trigger")
   - **Event → State** (type: "condition")

### Implementation Rules

1. **Entity Identification**:

   - Prefix state nodes with {entity}
   - Prefix event nodes with "Event\_"

2. **Content Guidelines**:

   - Use only explicitly stated information
   - Include all described paths from {entity}'s perspective (main flow, alternatives, error handling)
   - Document retry/recovery loops if explicitly specified
   - Focus on states/events relevant to {entity}
   - Ensure all nodes are connected into a single unified graph

3. **Strict Constraints**:
   - No inference of unstated information
   - No invention of state names
   - No assumptions about implicit behavior
   - Keep focus on {entity}'s perspective
   - No isolated or dangling nodes
   - Every node must be reachable from every other node through some path
   - All seemingly disconnected states or events must be properly integrated into the main flow

## Output Format

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

## Processing Guidelines

1. **Node Extraction**:

   - Identify explicit state definitions for {entity}
   - Document observable events from {entity}'s perspective
   - Maintain {entity}-specific prefixing
   - Ensure each node is connected to the main graph

2. **Edge Creation**:

   - Map state-to-event transitions for {entity}
   - Document event-triggered state changes from {entity}'s perspective
   - Include all explicitly described paths relevant to {entity}
   - Verify all transitions contribute to a single unified graph

3. **Special Cases**:
   - Support self-loops for retry scenarios
   - Include error handling paths
   - Document alternate flows (e.g., emergency procedures)
   - All cases must be from {entity}'s perspective
   - Each special case must be properly connected to the main flow

Only return a valid JSON object matching the specified format. No additional explanations or comments.

Input Text:

{context}
