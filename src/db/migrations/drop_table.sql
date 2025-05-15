-- Drop the tables in the correct order to avoid foreign key constraint errors
DROP TABLE IF EXISTS graph CASCADE;
DROP TABLE IF EXISTS section CASCADE;
DROP TABLE IF EXISTS procedure CASCADE;
DROP TABLE IF EXISTS document CASCADE;

-- Drop functions
DROP FUNCTION IF EXISTS encode_for_ltree(text);
DROP FUNCTION IF EXISTS decode_from_ltree(text);

-- Drop types
DROP TYPE IF EXISTS extraction_method;
DROP TYPE IF EXISTS graph_status;

-- Drop extensions
DROP EXTENSION IF EXISTS ltree;
DROP EXTENSION IF EXISTS "uuid-ossp";
