CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS graph;
CREATE TABLE graph (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    document_id UUID REFERENCES document(id) ON DELETE CASCADE,
    graph JSONB NOT NULL,
    accuracy FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
