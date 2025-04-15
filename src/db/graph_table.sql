CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS graph;
DROP TYPE IF EXISTS status;
CREATE TYPE status AS ENUM ('original', 'edited');

CREATE TABLE graph (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    document_id UUID REFERENCES document(id) ON DELETE CASCADE,
    original_graph JSONB NOT NULL,
    edited_graph JSONB DEFAULT NULL,
    accuracy FLOAT NOT NULL,
    extracted_at TIMESTAMP DEFAULT NOW(),
    last_edit_at TIMESTAMP DEFAULT NULL,
    status status DEFAULT 'original'
);
