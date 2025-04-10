----------------------------------------------------------------
-- graph table
----------------------------------------------------------------
-- test insertgraph
WITH doc AS (
    SELECT id FROM document WHERE name = 'Sample Document 1'
)
INSERT INTO graph (name, document_id, graph, accuracy)
SELECT
  'Initial Registration Procedure',
  doc.id,
  '{
  "graph": {
    "nodes": [
      {
        "id": "start",
        "type": "start",
        "description": "Procedure starts",
        "properties": {}
      },
      {
        "id": "1",
        "type": "process",
        "description": "UE sends REGISTRATION REQUEST message to the AMF",
        "properties": {
          "state_change": "5GMM-DEREGISTERED",
          "entity": "UE",
          "messages": ["REGISTRATION REQUEST"]
        }
      }
    ],
    "edges": [
      {
        "from": "start",
        "to": "1",
        "type": "sequential",
        "properties": {
          "trigger": "UE sends REGISTRATION REQUEST"
        }
      },
      {
        "from": "1",
        "to": "2",
        "type": "sequential",
        "properties": {
          "trigger": "UE starts timer T3510"
        }
      }
    ]
  }
}'::jsonb,
1.0
FROM doc;



        


