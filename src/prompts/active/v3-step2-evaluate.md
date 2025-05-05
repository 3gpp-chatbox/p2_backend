# Flow Property Graph Evaluation

## Input Requirements

You are given two inputs:

1. The original content from a 3GPP specification section describing the procedure: "{section_name}".
2. A Flow Property Graph (FPG) generated from this text focusing on the {entity} perspective, represented as a JSON object.

> **Important**: Your task is to **evaluate and validate** the FPG based only on the original content, specifically focusing on the {entity} side. **Do not return a corrected FPG. Instead, return a detailed evaluation report.**

---

## Evaluation Objectives

### Primary Goals
Assess whether the provided FPG is:
- An accurate, complete, and explicit representation of the {entity}'s perspective in the procedure
- A unified graph where all nodes are properly connected with no isolated parts
- A coherent representation where every node is reachable from every other node through some path

---

## Evaluation Criteria

### 1. Node Validation

- Identify any **missing** or **extra** nodes (states/events).
- **Nodes:**
  - **States:** Must be explicitly named {entity} states as they appear in the text (e.g., "5GMM-REGISTERED"). Do not invent or modify state names.
  - **Events:** Must be explicitly described visible triggers from {entity}'s perspective (e.g., "Receive REGISTRATION REQUEST", "T3510 expires", "Lower layer failure").
- Verify all node IDs:
  - States: Must be explicitly named and prefixed with {entity} (e.g., `"{entity}_[STATE_NAME]"`).
  - Events: Must begin with `"Event_"` and be clearly described in the spec (e.g., message received, timer expiry).
- Flag any node not directly supported by the original content.
- Verify each node is connected to at least one other node through edges.

### 2. Edge Validation

- Each valid transition must consist of **two edges**:
  - A `trigger` edge from a {entity} state to an event.
  - A `condition` edge from that event to a {entity} state.
- Verify:
  - Both `from` and `to` values match a node `id` in the `"nodes"` list.
  - Edge types are used correctly.
  - Transitions are explicitly stated in the input text.
  - Edges form continuous paths connecting all nodes.
- **Edges (Transitions):**
  - Each transition described in the text should be represented by **two directed edges**: one from a state to an event, and another from that event to the subsequent state.
  - All event→state edges must use `"condition"` type (even when representing actions).
  - If a procedure describes retry or failure recovery that leads back to the same state, include a self-loop transition (valid if explicitly described).

### 3. Transition Coverage

- Identify **missing transitions** from {entity}'s perspective that are described in the text but not represented in the FPG.
- Identify **redundant or invalid transitions** that are not supported by the text.
- Do not remove a transition just because its type is imprecise — only if the transition itself is unsupported.

### 4. Graph Connectivity

- Verify that all nodes are part of one unified graph:
  - No isolated nodes or subgraphs
  - Every node must be reachable from every other node through some path
  - States must be connected through appropriate events
  - Events must have both incoming and outgoing edges (except for terminal events)
  - All paths must be properly integrated into the main flow

---

## Output Format

Return a JSON object in the following format:

```json
{{
  "summary": {{
    "valid": true/false,
    "unified_graph": true/false,
    "missing_nodes": [{{"id": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "invalid_nodes": [{{"id": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "extra_nodes": [{{"id": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "missing_edges": [{{"from": "...", "to": "...", "type": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "invalid_edges": [{{"from": "...", "to": "...", "type": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "isolated_nodes": [{{"id": "...", "reason": "...","suggested_correction": "..."}}, ...],
    "disconnected_subgraphs": [{{"nodes": ["...", "..."], "reason": "...","suggested_correction": "..."}}, ...]
  }},
  "comments": [
    "Observation or warning about structure or logic",
    ...
  ]
}}
```

## Constraints

- **Focus on {entity}**: Only validate states and events from {entity}'s perspective
- **Unified Graph**: Ensure the FPG is one coherent graph with no isolated parts
- **No Inference**: Use only information that is explicitly stated in the input content
- **Completeness**: Return all issues you find, no matter how small
- **Format**: Maintain valid JSON structure for all responses
- **Output**: Return ONLY the valid JSON object

Input FPG:
{result_1}

Original Text:
{original_context}
