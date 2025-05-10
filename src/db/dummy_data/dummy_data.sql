INSERT INTO document (name, toc) VALUES
  ('Sample Document 1', '4 General, 4.1 Overview, 4.1.1 Details'),
  ('Sample Document 2', '5 Introduction, 5.1 Main Points, 5.1.1 Specifics');

-- Get document IDs dynamically (replace manually if needed)
WITH doc_ids AS (
    SELECT id FROM document ORDER BY extracted_at LIMIT 2
)
INSERT INTO section (document_id, heading, level, content, parent, path) VALUES
  ((SELECT id FROM doc_ids LIMIT 1), '4 General', 1, 'This is section 4.', NULL, 
   encode_for_ltree('4 General')::ltree),
  
  ((SELECT id FROM doc_ids LIMIT 1), '4.1 Overview', 2, 'Overview of section 4.', '4 General',
   (encode_for_ltree('4 General') || '.' || encode_for_ltree('4.1 Overview'))::ltree),
  
  ((SELECT id FROM doc_ids LIMIT 1), '4.1.1 Details', 3, 'Detailed information.', '4.1 Overview',
   (encode_for_ltree('4 General') || '.' || encode_for_ltree('4.1 Overview') || '.' || encode_for_ltree('4.1.1 Details'))::ltree),

  ((SELECT id FROM doc_ids OFFSET 1 LIMIT 1), '5 Introduction', 1, 'Introduction section.', NULL,
   encode_for_ltree('5 Introduction')::ltree),
  
  ((SELECT id FROM doc_ids OFFSET 1 LIMIT 1), '5.1 Main Points', 2, 'Main points discussion.', '5 Introduction',
   (encode_for_ltree('5 Introduction') || '.' || encode_for_ltree('5.1 Main Points'))::ltree),
  
  ((SELECT id FROM doc_ids OFFSET 1 LIMIT 1), '5.1.1 Specifics', 3, 'Specific details.', '5.1 Main Points',
   (encode_for_ltree('5 Introduction') || '.' || encode_for_ltree('5.1 Main Points') || '.' || encode_for_ltree('5.1.1 Specifics'))::ltree);

