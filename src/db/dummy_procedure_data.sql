----------------------------------------------------------------
-- Procedure table
----------------------------------------------------------------
-- test insert procedure
WITH doc AS (
    SELECT id FROM document WHERE name = 'Sample Document 1'
)
INSERT INTO procedure (name, document_id, graph)
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
}'::jsonb
FROM doc
WHERE NOT EXISTS (
  SELECT 1 FROM procedure WHERE name = 'Initial Registration Procedure' AND document_id = doc.id
);
-- test update procedure
UPDATE procedure
SET graph = '{
  "nodes": [
    {
      "id": "start",
      "type": "start",
      "description": "Procedure starts",
      "properties": {
        "state_change": "5GMM-DEREGISTERED",
        "entity": "UE",
        "messages": ["REGISTRATION REQUEST"]
      }
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
}'
WHERE id = 'c4f146c0-c7d5-4b8f-b727-b7bc4a859a05';


        


