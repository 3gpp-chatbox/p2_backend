You are given two inputs:
1. The original content from a 3GPP specification section describing the procedure: "{section_name}".
2. A Flow Property Graph (FPG) generated from this text for all involved entities (UE, AMF, etc.), represented as a JSON object.

Your task is to **evaluate and validate** the FPG based only on the original content. **Do not return a corrected FPG. Instead, return a detailed evaluation report.**

---

## Evaluation Objectives

Assess whether the provided FPG is an accurate, complete, and explicit representation of the procedure as described in the text.

---

## Evaluation Criteria

### 1. Node Validation
- Identify any **missing** or **extra** nodes (states/events).
- **Nodes:**
  - **States:** Must be explicitly named UE states as they appear in the text (e.g., "5GMM-REGISTERED"). Do not invent or modify state names.
  - **Events:** Must be explicitly described visible triggers (e.g., "Receive REGISTRATION REQUEST", "T3510 expires", "Lower layer failure").
  
- Verify all node IDs:
  - States: Must be explicitly named and prefixed with the correct entity (e.g., `"UE_"`, `"AMF_"`).
  - Events: Must begin with `"Event_"` and be clearly described in the spec (e.g., message received, timer expiry).
- Flag any node not directly supported by the original content.

### 2. Edge Validation
- Each valid transition must consist of **two edges**:
  - A `trigger` edge from a state to an event.
  - A `condition` edge from that event to a state.
  
- Verify:
  - Both `from` and `to` values match a node `id` in the `"nodes"` list.
  - Edge types are used correctly.
  - Transitions are explicitly stated in the input text.
  
- **Edges (Transitions):**
  - Each transition described in the text should be represented by **two directed edges**: one from a state to an event, and another from that event to the subsequent state.
  - All event→state edges must use `"condition"` type (even when representing actions).
  - If a procedure describes retry or failure recovery that leads back to the same state, include a self-loop transition (valid if explicitly described).

### 3. Transition Coverage
- Identify **missing transitions** that are described in the text but not represented in the FPG.
- Identify **redundant or invalid transitions** that are not supported by the text.
- Do not remove a transition just because its type is imprecise — only if the transition itself is unsupported.

---

## Output Format

Return a JSON object in the following format:

```json
{{
  "summary": {{
    "valid": true/false,
    "missing_nodes": [{{"id": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "invalid_nodes": [{{"id": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "extra_nodes": [{{"id": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "missing_edges": [{{"from": "...", "to": "...", "type": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "invalid_edges": [{{"from": "...", "to": "...", "type": "...", "reason": "...","suggested_correction": "..."}}, ...]
  }},
  "comments": [
    "Observation or warning about structure or logic",
    ...
  ]
}}

Constraints
Only use the input content to validate — do not infer or assume.
Return all issues you find, no matter how small.
Maintain valid JSON structure for all responses.
Return ONLY the valid JSON object.


Input FPG:
{result_1}

Original Text:
{original_content}
