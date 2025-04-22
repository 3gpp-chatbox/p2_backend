CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS graph;
DROP TYPE IF EXISTS extraction_method;
CREATE TYPE extraction_method AS ENUM ('main', 'modified', 'alternative');

CREATE TABLE graph (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    document_id UUID NOT NULL REFERENCES document(id) ON DELETE CASCADE,
    original_graph JSONB NOT NULL,
    edited_graph JSONB DEFAULT NULL,
    model_name TEXT NOT NULL,
    extraction_method extraction_method NOT NULL,
    accuracy FLOAT NOT NULL,
    extracted_at TIMESTAMP DEFAULT NOW(),
    last_edit_at TIMESTAMP DEFAULT NULL,
    edited BOOLEAN DEFAULT FALSE
);
