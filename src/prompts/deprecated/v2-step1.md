You will be provided with original content from 3GPP specification sections describing the procedure: "{procedure_name}".
Your task is to extract the **Flow Property Graph (FPG)** for this procedure "{procedure_name}", and represent it as a structured JSON object following the format defined below.
**Do not infer or assume any information beyond what is explicitly stated in the provided text.** Focus only on the information that is directly described and avoid including anything implied.

---

## Objective

Build a Flow Property Graph where:

- **Nodes** represent **states or events** for all entities involved (UE, AMF, etc.)
  - **States:** Explicitly named states for any entity (e.g., "5GMM-DEREGISTERED", "AMF_REGISTERED_STATE"). Do not invent or infer state names.
  - **Events:** Visible triggers such as received messages or expired timers (e.g., "Receive DEREGISTRATION REQUEST", "T3510 expires", "Lower layer failure"). Events describe occurrences/triggers that happen.
- **Edges** represent transitions between states and events. Each transition will be represented by **two directed edges**:
  - One from a state to an event
  - One from that event to the subsequent state
- Each edge must include a specific **type**:
  - "trigger": From state to event (state is triggered by event)
  - "condition": From event to state (event leads to state under conditions)
- **Edge Type Notes**:
  - All event→state transitions inherently represent actions, but currently map these to `"condition"` type edges
- Each node must be clearly identified with its entity type (UE or network entity) in node name, like "UE_5GMM_REGISTERED", "AMF_WAITING_FOR_AUTH".
- For all event nodes, names should have prefix Event\_, like Event_LowerLayer_Failure.

---

## Core Components to identify (All Entities)

### States:

- Include explicitly named states for all entities (UE, AMF, etc.)
- Format: "[ENTITY]\_[STATE_NAME]" (e.g., "UE_5GMM_REGISTERED", "AMF_WAITING_FOR_AUTH")
- Do not invent or infer state names.

### Events:

- These are **visible triggers** like messages received or timers expiring (e.g., `"Receive DEREGISTRATION REQUEST"`, `"T3510 expires"`).
- Include events for all entities involved.

### Conditions:

- Logical checks or criteria that must be met for the transition to occur (e.g., `"registration attempt counter < 5"`).
- Include only if **explicitly described** in the specification and directly associated with the triggering event.

### Actions:

- Actions the entity performs in response to the event and/or condition (e.g., `"Send REGISTRATION REQUEST"`).
- Must be explicitly stated — no inferences allowed.

### Conditions and Actions:

- You may identify conditions and actions during analysis, but only include them as edge types in the final JSON
- Do not include condition/action details in the final output

---

## JSON Output Format

```json
{{
  "procedure_name": "{procedure_name}",
  "graph": {{
    "nodes": [
      {{"id": "UE_5GMM_REGISTERED_INITIATED", "type": "state"}},
      {{"id": "Event_LowerLayer_Failure", "type": "event"}},
      {{"id": "UE_5GMM_DEREGISTERED_ATTEMPTING_REGISTRATION", "type": "state"}},
      {{"id": "AMF_REGISTRATION_PENDING", "type": "state"}}
    ],
    "edges": [
      {{
        "from": "UE_5GMM_REGISTERED_INITIATED",
        "to": "Event_LowerLayer_Failure",
        "type": "trigger"
      }},
      {{
        "from": "Event_LowerLayer_Failure",
        "to": "UE_5GMM_DEREGISTERED_ATTEMPTING_REGISTRATION",
        "type": "condition"
      }},
      {{
        "from": "AMF_REGISTRATION_PENDING",
        "to": "Event_Receive_REGISTRATION_REQUEST",
        "type": "trigger"
      }}
    ]
  }}
}}
```

Constraints
Multiple Entities: Include states and events for all entities involved (UE, AMF, etc.)
No Inference: Use only information that is explicitly stated in the input content.
Multiple Paths: If the spec describes alternate paths (e.g., emergency mode, failure recovery), include them all.
Fallbacks and Edge Cases: Capture fallback or error handling flows if explicitly described.
Support for Self-loops: If a procedure describes retry or failure recovery that leads the UE back to the same state, include a transition from that state to itself. This is valid as long as the loop is explicitly described in the text.
Input Text:
Analyze only the content below. Do not reference external knowledge:
{context}
