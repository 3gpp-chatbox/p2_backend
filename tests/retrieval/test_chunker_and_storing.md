# Document Parser Module Test Plan

## Overview
This test plan outlines the testing strategy for the document parser module, focusing on unit tests for both the extraction and database storage functionalities.

## General Test Framework
- [x] Use pytest exclusively for all tests
- [x] Utilize existing mock fixtures from `tests/conftest.py` for database operations
- [x] Implement only unit tests (no integration tests)

## Tests for `extract_chunks` (`tests/retrieval/test_document_parser_extract.py`)

### 1. Correct Input Handling
- [x] Create sample markdown files with proper headings and content
- [x] Test `extract_chunks` returns correct `ExtractedDocument` structure
  - [x] Validate with string path input
  - [x] Validate with Path object input
  - [x] Verify correct document name extraction
  - [x] Verify proper chunk structure (heading, content, level)

### 2. Edge Cases
- [x] Test empty markdown file
  - [x] Verify empty chunks list is returned
  - [x] Ensure document name is still extracted
- [x] Test markdown without headings
  - [x] Verify behavior with only content
  - [x] Verify behavior with mixed content (no headings)

### 3. Error Scenarios
- [x] Test non-existent file
  - [x] Verify FileNotFoundError is raised
  - [x] Validate error message
- [x] Test directory path
  - [x] Verify ValueError is raised
  - [x] Validate error message
- [x] Test malformed markdown
  - [x] Verify graceful handling of edge cases
  - [x] Ensure no unexpected crashes

## Tests for `store_extracted_sections` (`tests/retrieval/test_document_parser_db.py`)

### 1. Successful Operations
- [x] Mock successful document insertion
  - [x] Verify document ID retrieval
  - [x] Validate TOC storage
- [x] Test section processing
  - [x] Verify LTREE path computation
  - [x] Validate parent-child relationships
  - [x] Confirm correct hierarchy storage

### 2. Transaction and Error Handling
- [x] Test invalid document ID scenario
  - [x] Verify ValueError is raised
  - [x] Confirm proper error message
- [x] Test failed section insertion
  - [x] Simulate database error
  - [x] Verify exception propagation
  - [x] Confirm transaction rollback
- [x] Test empty chunks list
  - [x] Verify warning is logged
  - [x] Confirm function returns without error

### 3. Logging and Exception Checks
- [x] Verify logging for successful operations
  - [x] Document creation
  - [x] Section storage
- [x] Verify logging for error conditions
  - [x] Database errors
  - [x] Invalid data
  - [x] Warning messages

## Test Directory Structure
```
tests/
└── retrieval/
    ├── test_document_parser_extract.py
    ├── test_document_parser_db.py
    └── test_document_parser_plan.md
```

## Implementation Notes
- Ensure all tests follow project's coding standards
- Include proper type hints and docstrings
- Use descriptive test names following pytest conventions
- Implement proper test isolation
- Follow the "Arrange-Act-Assert" pattern
- Include comments explaining complex test scenarios
