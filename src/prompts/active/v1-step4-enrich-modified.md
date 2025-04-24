You are a 3GPP procedure specialist. You will analyze the procedure "{section_name}" using two input sources:

1. **Flow Property Graph**: The validated state-event structure of "{section_name}" (nodes and edges without descriptions)
2. **Specification Text**: The original 3GPP specification section detailing the procedure

## Task Objective

Enhance the flow property graph by adding precise descriptions to nodes and transitions, strictly based on the specification content.

### Enhancement Guidelines

1. **Node Descriptions**:
   - Provide clear, concise explanations (≤20 words) for each state and event
   - Example: 
     ```json
     {{
       "id": "UE_5GMM_REGISTERED_INITIATED",
       "type": "state",
       "description": "UE registered with ongoing procedure"
     }}
     ```

2. **Transition Descriptions**:
   - **State → Event**:
     - Format: `"Trigger: [event cause]; Condition: [requirement if specified]"`
     - Example: `"Trigger: Lower layer failure indication; No condition"`

   - **Event → State**:
     - Format: `"Condition: [transition requirement]; Action: [resulting operation]"`
     - Example: `"Condition: Registration attempts < 5; Action: Abort procedure"`

3. **Content Rules**:
   - Use only explicitly stated information from the specification
   - Maintain existing graph structure (no modifications to nodes/edges)
   - Keep all descriptions brief (≤100 characters)
   - Never infer unspecified details

## Output Specifications

```json
{{
  "procedure_name": "{section_name}",
  "graph": {{
    "nodes": [
      {{
        "id": "NODE_ID",
        "type": "node_type",
        "description": "concise explanation"
      }}
    ],
    "edges": [
      {{
        "from": "SOURCE_NODE",
        "to": "TARGET_NODE",
        "type": "edge_type",
        "description": "formatted description"
      }}
    ]
  }}
}}

Processing Constraints
Information Sources:
Node/edge structure from the Flow Property Graph
Descriptive content from the Specification Text

Prohibited Actions:
No structural changes to the graph
No assumptions beyond provided text
No introduction of external knowledge

Edge Cases:
If no condition exists: state "No condition"
If multiple conditions: join with "AND"
For empty descriptions: use empty string ("")

Input Data
Flow Property Graph:
{result_3}

3GPP Specification Content:
{original_content}