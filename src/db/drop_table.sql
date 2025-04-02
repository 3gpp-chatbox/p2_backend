-- Drop tables in correct order due to foreign key constraints
DROP TABLE IF EXISTS section;
DROP TABLE IF EXISTS document;

-- Drop functions
DROP FUNCTION IF EXISTS encode_for_ltree(text);
DROP FUNCTION IF EXISTS decode_from_ltree(text);

DROP EXTENSION IF EXISTS ltree;
DROP EXTENSION IF EXISTS "uuid-ossp";