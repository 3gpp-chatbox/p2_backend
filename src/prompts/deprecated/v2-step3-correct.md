You are given the following inputs:

1. A Flow Property Graph (FPG) in JSON format for the procedure "{section_name}".
2. An evaluation report identifying missing or incorrect nodes and edges in the FPG.

Your task is to **correct the FPG** using the evaluation report provided.

---

## Correction Instructions

Using the evaluation report, update the FPG:

- **Add missing nodes or edges** that are explicitly described in the text.
- **Remove invalid or extra nodes and edges** that are not supported by the content.
- **Ensure consistency** between all `from`/`to` values in edges and `id`s in the node list.
- **Edge Types**:
  - State→event must be `"trigger"`
  - Event→state must be `"condition"` (note: these transitions always represent actions in the actual procedure)
- **Node names and structure** must follow:
  - States: `"ENTITY_STATE_NAME"` (e.g., `"UE_5GMM_DEREGISTERED","AMF_REGISTRATION_PENDING"`)
  - Events: `"Event_[DESCRIPTION]"` (e.g., `"Event_T3510_Expires"`)

---

## Output Instructions

Return a single corrected FPG JSON object with the same structure as the input.

- Do not include the evaluation report.
- Do not include comments or explanations.
- Use only data supported by the original text.
- Do **not** invent new states, events, or transitions beyond those described.
- Do **not** make assumptions or corrections that are not supported by the evaluation.

---

###  Output Format (JSON):
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

---
Strict Rules:
Return only a valid JSON object.
No commentary, explanation, or text before/after the JSON.
Maintain exact original JSON structure.

Input Data

#### **Extracted procedure flow property graph info:**  
{result_1}

------------------
#### **Evaluation Report:**  
{result_2}