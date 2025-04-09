"""Test module for sections_content_retrieval.py.

This module contains test cases for the section content retrieval functionality.
It tests both the main retrieve_sections_content function and the helper
_generate_markdown function.

The tests use mock DatabaseHandler to simulate database interactions and
verify both successful scenarios and various error conditions.
"""

from unittest.mock import MagicMock

import pytest

from src.db.db_handler import DatabaseHandler
from src.retrieval.sections_content_retrieval import (
    _generate_markdown,
    retrieve_sections_content,
)


@pytest.fixture
def mock_db_handler() -> DatabaseHandler:
    """Create a mock database handler for testing.

    Returns:
        DatabaseHandler: A MagicMock object that simulates a DatabaseHandler.
            The mock is configured with the DatabaseHandler spec to ensure
            it has all the expected methods and attributes.
    """
    mock_handler = MagicMock(spec=DatabaseHandler)
    return mock_handler


@pytest.fixture
def sample_doc_query_result() -> list[dict[str, str | int]]:
    """Provide a sample document query result for testing.

    Returns:
        list[dict[str, str | int]]: A list containing a single document record
            with 'id' and 'name' fields, simulating a successful document query
            response.
    """
    return [{"id": 1, "name": "test_doc"}]


@pytest.fixture
def sample_sections_query_result() -> list[dict[str, str]]:
    """Provide a sample sections query result for testing.

    Returns:
        list[dict[str, str]]: A list of section records, each containing
            'heading' and 'path' fields, simulating a successful sections
            query response.
    """
    return [
        {"heading": "4.2 Test Section", "path": "1.4.2"},
        {"heading": "5.2 Another Section", "path": "1.5.2"},
    ]


@pytest.fixture
def sample_content_query_result() -> list[dict[str, str | int]]:
    """Provide a sample content query result for testing.

    Returns:
        list[dict[str, str | int]]: A list of content records, each containing
            'heading', 'level', and 'content' fields, simulating a successful
            hierarchical content query response.
    """
    return [
        {
            "heading": "4.2 Test Section",
            "level": 2,
            "content": "This is test section content",
        },
        {
            "heading": "5.2 Another Section",
            "level": 2,
            "content": "This is another section content",
        },
    ]


def test_retrieve_sections_content_normal_execution(
    mock_db_handler,
    sample_doc_query_result,
    sample_sections_query_result,
    sample_content_query_result,
):
    """Test that retrieve_sections_content correctly processes and formats section content.

    Verifies that the function correctly queries for document existence,
    fetches section paths, retrieves hierarchical content, and generates
    proper markdown output.
    """
    # Configure mock to return test data
    mock_db_handler.execute_query.side_effect = [
        sample_doc_query_result,  # First call: document query
        sample_sections_query_result,  # Second call: sections query
        sample_content_query_result,  # Third call: content query
    ]

    # Execute function
    result = retrieve_sections_content(mock_db_handler, "test_doc", ["4.2", "5.2"])

    # Verify the expected markdown format
    expected_markdown = (
        "# test_doc\n\n"
        "## 4.2 Test Section\n\n"
        "This is test section content\n\n"
        "## 5.2 Another Section\n\n"
        "This is another section content"
    )

    assert result == expected_markdown

    # Verify all database calls were made correctly
    assert mock_db_handler.execute_query.call_count == 3


def test_retrieve_sections_content_missing_doc_name(
    mock_db_handler: DatabaseHandler,
) -> None:
    """Test that empty document name validation raises appropriate error.

    Verifies that attempting to retrieve sections with an empty document name
    raises a ValueError with an appropriate error message.
    """
    with pytest.raises(ValueError, match="Missing required argument: doc_name"):
        retrieve_sections_content(mock_db_handler, "", ["4.2"])


def test_retrieve_sections_content_empty_section_list(
    mock_db_handler: DatabaseHandler,
) -> None:
    """Test that empty section list validation raises appropriate error.

    Verifies that attempting to retrieve content with an empty section list
    raises a ValueError with the expected error message.
    """
    with pytest.raises(ValueError, match="Missing required argument: section_list"):
        retrieve_sections_content(mock_db_handler, "test_doc", [])


def test_retrieve_sections_content_invalid_section_type(
    mock_db_handler: DatabaseHandler,
) -> None:
    """Test that section list validation rejects non-string elements.

    Verifies that attempting to retrieve sections with a list containing
    non-string elements (e.g., numbers) raises a ValueError with appropriate
    error message.
    """
    with pytest.raises(ValueError, match="All section identifiers must be strings"):
        retrieve_sections_content(mock_db_handler, "test_doc", ["4.2", 5.2])


def test_retrieve_sections_content_document_not_found(
    mock_db_handler: DatabaseHandler,
) -> None:
    """Test that retrieving sections from non-existent documents raises an error.

    Verifies the function correctly handles cases where the requested document
    doesn't exist in the database by raising an appropriate exception.
    """
    # Configure mock to return empty result for document query
    mock_db_handler.execute_query.return_value = []

    with pytest.raises(
        Exception,
        match="fetch_sections_content: Failed to retrieve sections: Document 'non_existent_doc' not found in the database",
    ):
        retrieve_sections_content(mock_db_handler, "non_existent_doc", ["4.2"])


def test_retrieve_sections_content_no_sections_found(
    mock_db_handler: DatabaseHandler,
    sample_doc_query_result: list[dict[str, str | int]],
) -> None:
    """Test that appropriate error is raised when no sections match the criteria.

    Verifies that the function handles cases where the document exists but no
    sections match the requested section identifiers.
    """
    # Configure mock to return document but no sections
    mock_db_handler.execute_query.side_effect = [
        sample_doc_query_result,  # Document exists
        [],  # No sections found
    ]

    with pytest.raises(
        Exception,
        match="fetch_sections_content: Failed to retrieve sections: No sections found for document 'test_doc' with the given parameter:",
    ):
        retrieve_sections_content(mock_db_handler, "test_doc", ["non_existent_section"])


def test_retrieve_sections_content_hierarchical_query_failure(
    mock_db_handler: DatabaseHandler,
    sample_doc_query_result: list[dict[str, str | int]],
    sample_sections_query_result: list[dict[str, str]],
) -> None:
    """Test that hierarchical content query failures are properly handled.

    Verifies the function correctly handles cases where document and sections exist,
    but the hierarchical content query returns no results.
    """
    # Configure mock to return document and sections but no content
    mock_db_handler.execute_query.side_effect = [
        sample_doc_query_result,  # Document exists
        sample_sections_query_result,  # Sections exist
        [],  # No content found
    ]

    with pytest.raises(
        Exception,
        match="fetch_sections_content: Failed to retrieve sections: Failed to perform hierarchical search for document 'test_doc' with the given parameter:",
    ):
        retrieve_sections_content(mock_db_handler, "test_doc", ["4.2", "5.2"])


def test_generate_markdown_normal_execution() -> None:
    """Test that _generate_markdown correctly formats hierarchical content.

    Verifies proper formatting of document title, section headings with
    appropriate heading levels, and content with proper spacing.
    """
    doc_name = "Test Document"
    sections_content = [
        {"heading": "First Section", "level": 1, "content": "First section content"},
        {"heading": "Subsection", "level": 2, "content": "Subsection content"},
        {"heading": "Deep Section", "level": 3, "content": "Deep section content"},
    ]

    result = _generate_markdown(doc_name, sections_content)

    expected_markdown = (
        "# Test Document\n\n"
        "# First Section\n\n"
        "First section content\n\n"
        "## Subsection\n\n"
        "Subsection content\n\n"
        "### Deep Section\n\n"
        "Deep section content"
    )

    assert result == expected_markdown


def test_generate_markdown_missing_required_key() -> None:
    """Test that _generate_markdown properly handles missing required keys in section data.

    Verifies the function raises appropriate exceptions when attempting to process
    section dictionaries that are missing required fields like 'level'.
    """
    doc_name = "Test Document"
    sections_content = [
        {
            "heading": "Section",  # missing 'level'
            "content": "Content",
        }
    ]

    with pytest.raises(
        Exception, match="`_generate_markdown`: Failed to generate markdown:"
    ):
        _generate_markdown(doc_name, sections_content)
