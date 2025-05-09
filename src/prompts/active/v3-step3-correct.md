# Flow Property Graph Correction

## Input Requirements

You are given the following inputs:

1. A Flow Property Graph (FPG) in JSON format for the procedure "{section_name}" focusing on the {entity} perspective.
2. An evaluation report identifying missing or incorrect nodes and edges in the FPG, including any connectivity issues.

> **Important**: Your task is to **correct the FPG** using the evaluation report provided, ensuring the focus remains on the {entity} side of the procedure and all nodes are properly connected in a unified graph.

---

## Correction Instructions

### Basic Updates
Using the evaluation report, update the FPG:

- **Add missing nodes or edges** from {entity}'s perspective that are explicitly described in the text.
- **Remove invalid or extra nodes and edges** that are not supported by the content or not relevant to {entity}.
- **Ensure consistency** between all `from`/`to` values in edges and `id`s in the node list.

### Component Requirements
- **Edge Types**:
  - State→event must be `"trigger"`
  - Event→state must be `"condition"` (note: these transitions always represent actions in the actual procedure)
- **Node names and structure** must follow:
  - States: `"[ENTITY]_[STATE_NAME]"` (e.g., `"{entity}_5GMM_DEREGISTERED"`)
  - Events: `"Event_[DESCRIPTION]"` (e.g., `"Event_T3510_Expires"`)

## Graph Connectivity Requirements

### 1. Unified Structure
- All nodes must be part of one coherent graph
- No isolated nodes or disconnected subgraphs allowed
- Every node must be reachable from every other node through some path

### 2. Node Integration
- Each state must connect to at least one event
- Each event must have both incoming and outgoing edges (except for terminal events)
- All paths must be properly integrated into the main flow

### 3. Handling Isolated Components
- If isolated nodes are identified in the evaluation report, integrate them into the main graph
- If disconnected subgraphs exist, merge them appropriately with the main flow
- Ensure any new connections are supported by the specification text

---

## Output Instructions

Return a single corrected FPG JSON object with the same structure as the input.

### Requirements
- Do not include the evaluation report.
- Do not include comments or explanations.
- Use only data supported by the original text.
- Focus only on {entity}'s states and transitions.
- Ensure all nodes are connected in a single unified graph.
- Do **not** invent new states, events, or transitions beyond those described.
- Do **not** make assumptions or corrections not supported by the evaluation.

### Output Format (JSON)
Return ONLY the corrected graph in this format:

```json
{{
  "procedure_name": "{section_name}",
  "graph": {{
    "nodes": [...],
    "edges": [...]
  }}
}}
```

## Strict Rules

- Return only a valid JSON object
- Focus only on {entity}'s perspective in the procedure
- Ensure all nodes are connected in a single unified graph
- No commentary, explanation, or text before/after the JSON
- Maintain exact original JSON structure

---

## Input Data

### Extracted procedure flow property graph info:  
{result_1}

### Evaluation Report:  
{result_2}
