-- Example 1: Find a section and all its descendants by heading (encoded paths)
WITH target_section AS (
    SELECT path
    FROM section 
    WHERE heading = '4 General'
)
SELECT 
    s.heading,
    s.level,
    s.content,
    s.path AS encoded_path
FROM section s,
     target_section ts
WHERE s.path <@ ts.path  -- Find this section and all descendants
ORDER BY s.path;

-- Example 3: Find a section and all its descendants by heading (encoded paths)
WITH target_section AS (
    SELECT path
    FROM section 
    WHERE heading = '4 General'
)
SELECT 
    s.heading,
    s.level,
    s.content,
    s.path,
    string_agg(decode_from_ltree(label), '.' ORDER BY ordinality) AS decoded_path
FROM section s,
     target_section ts,
     unnest(string_to_array(s.path::text, '.')) WITH ORDINALITY AS u(label, ordinality)
WHERE s.path <@ ts.path
GROUP BY s.section_id, s.heading, s.level, s.content, s.path
ORDER BY s.path;