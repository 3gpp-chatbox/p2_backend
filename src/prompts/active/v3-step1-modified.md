# 3GPP Flow Property Graph Extraction

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
     - Example: "{entity}\_5GMM_REGISTERED"
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
    "nodes": [
        {{
            "id": "{entity}_5GMM_REGISTERED_INITIATED",
            "type": "state",
            "section_reference": "5.5.1.2.7 Abnormal cases in the UE",
            "text_reference": "If the UE receives a DEREGISTRATION REQUEST message from the network in state 5GMM-REGISTERED-INITIATED"
        }},
        {{
            "id": "Event_LowerLayer_Failure",
            "type": "event",
            "section_reference": "5.5.1.2.7 Abnormal cases in the UE",
            "text_reference": "Lower layer failure or release of the NAS signalling connection received from lower layers"
        }},
        {{
            "id": "{entity}_5GMM_DEREGISTERED_ATTEMPTING_REGISTRATION",
            "type": "state",
            "section_reference": "5.5.1.2.5 Initial registration not accepted by the network",
            "text_reference": "Cause #22 (Congestion). ... enter state 5GMM-DEREGISTERED.ATTEMPTING-REGISTRATION."
        }}
    ],
    "edges": [
        {{
            "from": "{entity}_5GMM_REGISTERED_INITIATED",
            "to": "Event_LowerLayer_Failure",
            "type": "trigger",
            "section_reference": "5.5.1.2.7 Abnormal cases in the UE",
            "text_reference": "Lower layer failure or release of the NAS signalling connection received from lower layers"
        }},
        {{
            "from": "Event_LowerLayer_Failure",
            "to": "{entity}_5GMM_DEREGISTERED_ATTEMPTING_REGISTRATION",
            "type": "condition",
            "section_reference": "5.5.1.2.7 Abnormal cases in the UE",
            "text_reference": "If the registration attempt counter is less than 5: ... timer T3511 is started and the state is changed to 5GMM-DEREGISTERED.ATTEMPTING-REGISTRATION."
        }}
    ]
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

---

# **INPUT: CONTEXT FROM 3GPP SPECIFICATION:**

{context}
