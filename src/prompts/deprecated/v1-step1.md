You are a 3GPP procedure analysis expert and a large language model with strong reasoning capabilities.

Your task is to extract a **State-Event Transition Graph** from the 3GPP procedure: "{section_name}". This graph represents a high-level logical flow of the procedure, with clearly defined **States**, **Events**, and **Transitions** between them.

---

###  DEFINITIONS

1. **State**: A system condition or phase of an entity (e.g., UE, gNB, MME). These often appear with verbs like: *enters*, *is in*, *waits for*, *has completed*, *moves to*.  
    Examples: `UE_Idle`, `MME_WaitingForAuthResponse`, `UE_Attaching`

2. **Event**: A message or action that triggers a transition between states. Usually indicated by: *sends*, *receives*, *triggers*, *initiates*, *detects*.  
    Examples: `Attach_Request_Received`, `Auth_Request_Sent`, `RRC_Connection_Established`

3. **Transition**: A directed link from one state to another via an event.  
    Format: `State_A → Event_X → State_B`

---

###  THINK STEP: Extract Candidates First

Before building the final graph, **analyze the section step-by-step** and extract:

- All **possible States**: Quote the exact phrase or rephrase only if meaning is clear
- All **Events**: Capture all message exchanges or triggering actions
- Candidate **Transitions**: Where a state leads to another based on event

Rely **only on the text** provided. However, you may use 3GPP domain knowledge **to interpret terminology or infer intent** — **but not to invent missing steps**.

 If a message or state is **not clearly stated or inferable from sentence structure**, **do not include it**.

---

###  STRUCTURE CHECK RULES

- All **edges** (transitions) must go: `state → event → state`
- Do not create orphan nodes or duplicate edges
- Only include nodes/transitions explicitly stated or unambiguously implied

---

###  OUTPUT FORMAT (JSON)

**Your entire response must ONLY be a single valid JSON object** in the following format. Do not include explanation, comments, or extra text.

{{
  "procedure_name": "{section_name}",
  "graph": {{
    "nodes": [
      {{ "id": "UE_Idle", "type": "state" }},
      {{ "id": "Attach_Request_Received", "type": "event" }},
      {{ "id": "UE_Attaching", "type": "state" }}
    ],
    "edges": [
      {{
        "from": "UE_Idle",
        "to": "Attach_Request_Received",
        "type": "trigger"
      }},
      {{
        "from": "Attach_Request_Received",
        "to": "UE_Attaching",
        "type": "condition"
      }}
    ]
  }}
}}

---

###  EXAMPLE TRANSITION LINE FROM TEXT

**Spec line**: "Once the UE powers on, it sends an Attach Request to the MME."

 Extract:
- State: `UE_Powered_On`
- Event: `Attach_Request_Sent`
- Transition: `UE_Powered_On → Attach_Request_Sent → UE_Attaching`

---

### PROCEDURE SECTION

Extract the State-Event Graph below **using only the provided text**, and return ONLY the JSON object.


{text}
