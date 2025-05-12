CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS ltree;

CREATE TYPE extraction_method AS ENUM ('main', 'modified', 'alternative');
CREATE TYPE graph_status AS ENUM ('new', 'verified');
CREATE TYPE entity_type AS ENUM ('UE', 'AMF', 'SMF', 'gNB');

-- Helper function to encode text to hex for ltree paths
CREATE OR REPLACE FUNCTION encode_for_ltree(text) RETURNS text AS $$
BEGIN
    -- Convert text to hex
    RETURN encode(convert_to($1, 'UTF8'), 'hex');
END;
$$ LANGUAGE plpgsql IMMUTABLE;

--  Decode hex ltree path label back to text
CREATE OR REPLACE FUNCTION decode_from_ltree(text) RETURNS text AS $$
BEGIN
    -- Remove any leading/trailing quotes
    RETURN convert_from(decode(trim(both '"' from $1), 'hex'), 'UTF8');
EXCEPTION
    WHEN OTHERS THEN
        -- Return original text if decoding fails
        RETURN $1;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Document Table
CREATE TABLE document (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL UNIQUE,
    toc TEXT NOT NULL,
    extracted_at TIMESTAMP DEFAULT NOW()
);

-- Section Table
CREATE TABLE section (
    section_id SERIAL PRIMARY KEY,
    document_id UUID REFERENCES document(id) ON DELETE CASCADE,
    heading TEXT NOT NULL,
    level INT NOT NULL,
    content TEXT NOT NULL,
    parent TEXT,
    path LTREE NOT NULL -- Will store hex-encoded paths
);


-- Procedure Table
CREATE TABLE procedure (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    document_id UUID NOT NULL REFERENCES document(id) ON DELETE CASCADE,
    retrieved_top_sections TEXT[] NOT NULL,  -- stores array of top-level section identifiers
    extracted_at TIMESTAMP DEFAULT NOW()
);

-- Graph Table
CREATE TABLE graph (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity entity_type NOT NULL,
    extracted_data JSONB NOT NULL,
    model_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    status graph_status NOT NULL,
    procedure_id UUID NOT NULL REFERENCES procedure(id) ON DELETE CASCADE,
    accuracy FLOAT NOT NULL,
    extraction_method extraction_method NOT NULL,
    commit_title TEXT NOT NULL,
    commit_message TEXT NOT NULL,
    version TEXT NOT NULL,

    -- Ensures version uniqueness per procedure
    UNIQUE(procedure_id, entity,version)
);

-- Indexes for optimization
CREATE INDEX idx_section_document_id ON section(document_id);
CREATE INDEX idx_section_path ON section USING GIST (path);
CREATE INDEX idx_procedure_document_id ON procedure(document_id);
CREATE INDEX idx_graph_procedure_id ON graph(procedure_id);
CREATE INDEX idx_graph_status ON graph(status);