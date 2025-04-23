You are a 3GPP procedure analysis expert and logic validator.

You are given:

1. A **flow property graph** (state-event-transition model) extracted from the 3GPP procedure: "{section_name}".
2. The **original 3GPP specification section text** from which the graph was generated.

---

### Your task:

Evaluate the accuracy and completeness of the flow graph by comparing it to the provided specification content. Identify any of the following issues:

#### What to Detect:

1. **Missing components**: States, events, or transitions that are clearly described in the spec but not included in the graph.
2. **Incorrect components**:
   - Wrong classifications (e.g., event misclassified as state).
   - Mismatches in semantics (e.g., wrong state label).
3. **Incorrect edge types**:
   - `trigger` used where `condition` is correct, or vice versa.
4. **Conflicting node types**:
   - Same node appears as both a state and an event.
5. **Invalid graph structure**:
   - `from` or `to` fields in edges that do not match any node `id`.
6. **Fatal errors**:
   - If the graph is fundamentally incorrect or contains no relevant structure from the spec.

---

### Reasoning Process (Required but do not return your analysis in response):

Before writing the corrections:

- Skim the **spec section line by line**.
- Identify each state, event, and transition described or implied.
- For each, **check whether it exists in the graph**, is correctly classified, and is connected correctly.
- Compare **temporal/cause-effect language** such as: "after", "once", "triggers", "causes", "leads to", etc.

You may use your domain knowledge to **interpret** terminology or message purpose, but you must **not invent or assume** content not clearly supported by the text.

---

### Output Format (JSON)

ONLY Return a list of corrections and inconsistencies in json format, like this:

```json
{{
  "corrections": [
    {{
      "type": "missing_state",
      "state": "UE_Securing",
      "description": "State 'UE_Securing' is missing after successful authentication.",
      "suggested_location": "After 'UE_Authenticated' and before 'UE_Attaching'.",
      "supporting_text_snippet": "After successful authentication, the UE secures its connection before proceeding."
    }},
    {{
      "type": "incorrect_event",
      "event": "Attach_Request",
      "suggested_event": "Attach_Request_Received",
      "description": "The event 'Attach_Request' should reflect that it's received by the MME.",
      "supporting_text_snippet": "The MME receives an Attach Request from the UE."
    }},
    {{
      "type": "incorrect_edge_type",
      "edge": "Attach_Request_Received → UE_Attaching",
      "current_type": "condition",
      "suggested_type": "trigger",
      "description": "This event causes the transition, so it should be a 'trigger'."
    }},
    {{
      "type": "missing_transition",
      "from": "UE_Attaching",
      "event": "Auth_Challenge_Received",
      "to": "UE_Authenticating",
      "description": "Transition missing: UE receives auth challenge after attach.",
      "supporting_text_snippet": "The network initiates authentication once attach is processed."
    }},
    {{
      "type": "conflicting_node_type",
      "node": "Attach_Request",
      "current_types": ["state", "event"],
      "suggested_type": "event",
      "description": "Node is incorrectly labeled as both a state and an event."
    }},
    {{
      "type": "invalid_edge_reference",
      "edge": {{
        "from": "UE_Powered_On",
        "to": "Attach_Started"
      }},
      "description": "The node 'Attach_Started' does not exist in the node list."
    }},
    {{
      "type": "fatal_error",
      "description": "The graph contains no valid states or events from the original spec section. Likely a total extraction failure."
    }}
  ]
}}

Flow Property Graph to Evaluate:
{result_1}

Original 3GPP Specification Section:
{original_content}


##Strict Rules##
Do not make assumptions or insert inferred behavior not grounded in the spec text.
Use domain knowledge only to interpret, not invent.
Return all issues you find, no matter how small.
Maintain valid JSON structure for all responses.
return ONLY the JSON object.
```
