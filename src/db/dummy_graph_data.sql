
-- Insert dummy graph data with proper JSON structure
WITH doc AS (
    SELECT id FROM document WHERE name = 'Sample Document 1'
)
INSERT INTO graph (name, document_id, original_graph, edited_graph, model_name, extraction_method, accuracy, extracted_at, last_edit_at, edited)
VALUES 
-- Original graph (no edits) 
(
    'Sample Graph 1',
    (SELECT id FROM doc),
    '{
        "nodes": [
            {"id": "1", "type": "state", "description": "User"},
            {"id": "2", "type": "event", "description": "Login"},
            {"id": "3", "type": "state", "description": "System"}
        ],
        "edges": [
            {"from": "1", "to": "2", "type": "trigger", "description": "performs"},
            {"from": "2", "to": "3", "type": "condition", "description": "authenticates with"}
        ]
    }',
    NULL,
    'gpt-4-1106-preview',
    'main',
    0.95,
    NOW() - INTERVAL '2 days',
    NULL,
    FALSE
),
-- Edited graph - explicitly set status to 'edited'
(
    'Sample Graph 2',
    (SELECT id FROM doc),
    '{
        "nodes": [
            {"id": "1", "type": "state", "description": "User"},
            {"id": "2", "type": "event", "description": "Login"},
            {"id": "3", "type": "state", "description": "System"}
        ],
        "edges": [
            {"from": "1", "to": "2", "type": "trigger", "description": "performs"},
            {"from": "2", "to": "3", "type": "condition", "description": "authenticates with"}
        ]
    }',
    '{
        "nodes": [
            {"id": "1", "type": "state", "description": "User"},
            {"id": "2", "type": "event", "description": "Login"},
            {"id": "3", "type": "state", "description": "System"},
            {"id": "4", "type": "state", "description": "Database"}
        ],
        "edges": [
            {"from": "1", "to": "2", "type": "trigger", "description": "performs"},
            {"from": "2", "to": "3", "type": "condition", "description": "authenticates with"},
            {"from": "3", "to": "4", "type": "condition", "description": "queries"}
        ]
    }',
    'gpt-4-1106-preview',
    'main',
    0.92,
    NOW() - INTERVAL '1 day',
    NOW(),
    TRUE
);


-- Insert another graph for the second document
WITH doc2 AS (
    SELECT id FROM document WHERE name = 'Sample Document 2'
)
INSERT INTO graph (name, document_id, original_graph, edited_graph, model_name, extraction_method, accuracy, extracted_at, last_edit_at, edited)
VALUES 
-- Another original graph
(
    'Sample Graph 3',
    (SELECT id FROM doc2),
    '{
        "nodes": [
            {"id": "1", "type": "state", "description": "Customer"},
            {"id": "2", "type": "event", "description": "Place Order"},
            {"id": "3", "type": "state", "description": "Product"},
            {"id": "4", "type": "state", "description": "Payment"}
        ],
        "edges": [
            {"from": "1", "to": "2", "type": "trigger", "description": "performs"},
            {"from": "2", "to": "3", "type": "condition", "description": "orders"},
            {"from": "2", "to": "4", "type": "condition", "description": "pays with"}
        ]
    }',
    NULL,
    'gpt-4-1106-preview',
    'main',
    0.88,
    NOW() - INTERVAL '12 hours',
    NULL,
    FALSE
);
