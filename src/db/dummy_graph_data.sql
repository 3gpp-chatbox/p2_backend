
-- Insert dummy graph data with proper JSON structure
WITH doc AS (
    SELECT id FROM document WHERE name = 'Sample Document 1'
)
INSERT INTO graph (name, document_id, original_graph, edited_graph, accuracy, extracted_at, last_edit_at, status)
VALUES 
-- Original graph (no edits) 
(
    'Sample Graph 1',
    (SELECT id FROM doc),
    '{
        "nodes": [
            {"id": "1", "type": "entity", "label": "User"},
            {"id": "2", "type": "action", "label": "Login"},
            {"id": "3", "type": "entity", "label": "System"}
        ],
        "edges": [
            {"source": "1", "target": "2", "label": "performs"},
            {"source": "2", "target": "3", "label": "authenticates with"}
        ]
    }',
    NULL,
    0.95,
    NOW() - INTERVAL '2 days',
    NULL,
    'original'
),
-- Edited graph - explicitly set status to 'edited'
(
    'Sample Graph 2',
    (SELECT id FROM doc),
    '{
        "nodes": [
            {"id": "1", "type": "entity", "label": "User"},
            {"id": "2", "type": "action", "label": "Login"},
            {"id": "3", "type": "entity", "label": "System"}
        ],
        "edges": [
            {"source": "1", "target": "2", "label": "performs"},
            {"source": "2", "target": "3", "label": "authenticates with"}
        ]
    }',
    '{
        "nodes": [
            {"id": "1", "type": "entity", "label": "User"},
            {"id": "2", "type": "action", "label": "Login"},
            {"id": "3", "type": "entity", "label": "System"},
            {"id": "4", "type": "entity", "label": "Database"}
        ],
        "edges": [
            {"source": "1", "target": "2", "label": "performs"},
            {"source": "2", "target": "3", "label": "authenticates with"},
            {"source": "3", "target": "4", "label": "queries"}
        ]
    }',
    0.92,
    NOW() - INTERVAL '1 day',
    NOW(),
    'edited'
);


-- Insert another graph for the second document
WITH doc2 AS (
    SELECT id FROM document WHERE name = 'Sample Document 2'
)
INSERT INTO graph (name, document_id, original_graph, edited_graph, accuracy, extracted_at, last_edit_at, status)
VALUES 
-- Another original graph - status will default to 'original'
(
    'Sample Graph 3',
    (SELECT id FROM doc2),
    '{
        "nodes": [
            {"id": "1", "type": "entity", "label": "Customer"},
            {"id": "2", "type": "action", "label": "Place Order"},
            {"id": "3", "type": "entity", "label": "Product"},
            {"id": "4", "type": "entity", "label": "Payment"}
        ],
        "edges": [
            {"source": "1", "target": "2", "label": "performs"},
            {"source": "2", "target": "3", "label": "orders"},
            {"source": "2", "target": "4", "label": "pays with"}
        ]
    }',
    NULL,
    0.88,
    NOW() - INTERVAL '12 hours',
    NULL,
    'original'
);

