-- Drop tables in correct order due to foreign key constraints

DROP TABLE IF EXISTS graph;
DROP TABLE IF EXISTS section;
DROP TABLE IF EXISTS document;
-- Drop functions
DROP FUNCTION IF EXISTS encode_for_ltree(text);
DROP FUNCTION IF EXISTS decode_from_ltree(text);

-- Drop types
DROP TYPE IF EXISTS extraction_method;

-- Drop extensions
DROP EXTENSION IF EXISTS ltree;
DROP EXTENSION IF EXISTS "uuid-ossp";