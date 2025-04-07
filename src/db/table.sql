CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS ltree;

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

CREATE TABLE document (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL UNIQUE,
    toc TEXT NOT NULL,
    extracted_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE section (
    section_id SERIAL PRIMARY KEY,
    document_id UUID REFERENCES document(id) ON DELETE CASCADE,
    heading TEXT NOT NULL,
    level INT NOT NULL,
    content TEXT NOT NULL,
    parent TEXT,
    path LTREE NOT NULL -- Will store hex-encoded paths
);

-- Indexes for optimization
CREATE INDEX idx_section_document_id ON section(document_id);
CREATE INDEX idx_section_path ON section USING GIST (path);
