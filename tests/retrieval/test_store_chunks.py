"""Unit tests for document parser's store_extracted_sections function."""

from typing import Any, Dict, List
from unittest.mock import MagicMock, call

import pytest

from src.retrieval.chunker import Chunk
from src.retrieval.store_chunks import store_extracted_sections


@pytest.fixture
def sample_chunks() -> List[Chunk]:
    """Create a sample list of document chunks for testing.

    Returns:
        List[Chunk]: List of chunk dictionaries with test data
    """
    return [
        {"heading": "First Section", "level": 1, "content": "Content 1"},
        {"heading": "Subsection", "level": 2, "content": "Content 2"},
        {"heading": "Second Section", "level": 1, "content": "Content 3"},
    ]


@pytest.fixture
def mock_db_success(mock_connection: MagicMock) -> MagicMock:
    """Setup mock database handler for successful operations.

    Args:
        mock_connection: pytest fixture providing a mock database connection

    Returns:
        MagicMock: Configured mock database handler with custom query handling
    """

    def mock_execute_query(*args: Any, **kwargs: Any) -> List[Dict[str, Any]]:
        """Mock database query execution with context-aware responses.

        Returns appropriate mock data based on the type of query being executed:
        - Document insertion returns a document ID
        - LTREE encoding returns encoded heading strings
        - Other queries return empty list
        """
        if "RETURNING id" in args[0]:
            return [{"id": 1}]
        if "encode_for_ltree" in args[0]:
            heading = args[1][0]
            # Convert heading to lowercase and replace spaces with underscores
            encoded = heading.lower().replace(" ", "_")
            return [{"encoded": encoded}]
        return []

    return MagicMock(
        transaction=MagicMock(return_value=mock_connection),
        execute_query=MagicMock(side_effect=mock_execute_query),
    )


def test_store_sections_successful(
    mock_db_success: MagicMock, sample_chunks: List[Chunk]
) -> None:
    """Test successful storage of document sections.

    Verifies:
    - Document record is created
    - Sections are stored with correct hierarchical paths
    - Parent-child relationships are properly established
    """
    # Arrange
    doc_name = "test_doc"
    toc = "Sample TOC"

    # Act
    store_extracted_sections(mock_db_success, doc_name, toc, sample_chunks)

    # Assert
    # Verify document insertion
    mock_db_success.execute_query.assert_any_call(
        """
                INSERT INTO document (name, toc)
                VALUES (%s, %s)
                RETURNING id;
            """,
        ("test_doc", "Sample TOC"),
        fetch=True,
    )

    # Verify section insertions with correct paths
    expected_section_calls = [
        call(
            """
                    INSERT INTO section (document_id, heading, level, content, parent, path)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """,
            (1, "First Section", 1, "Content 1", None, "first_section"),
            fetch=False,
        ),
        call(
            """
                    INSERT INTO section (document_id, heading, level, content, parent, path)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """,
            (
                1,
                "Subsection",
                2,
                "Content 2",
                "First Section",
                "first_section.subsection",
            ),
            fetch=False,
        ),
        call(
            """
                    INSERT INTO section (document_id, heading, level, content, parent, path)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """,
            (1, "Second Section", 1, "Content 3", None, "second_section"),
            fetch=False,
        ),
    ]
    mock_db_success.execute_query.assert_has_calls(
        expected_section_calls, any_order=True
    )


def test_store_sections_no_chunks(
    mock_db_success: MagicMock, caplog: pytest.LogCaptureFixture
) -> None:
    """Test handling of empty chunks list.

    Verifies that:
    - Warning is logged
    - No database operations are attempted
    """
    # Act
    store_extracted_sections(mock_db_success, "test_doc", "toc", [])

    # Assert
    assert "No chunks provided for storage" in caplog.text
    assert not mock_db_success.execute_query.called


def test_store_sections_failed_document_insert(mock_connection: MagicMock) -> None:
    """Test handling of failed document insertion.

    Verifies proper error handling when document insertion fails to return an ID.
    """
    # Arrange
    # Mock that always returns empty list for document insertion
    db_handler = MagicMock(
        transaction=MagicMock(return_value=mock_connection),
        execute_query=MagicMock(return_value=[]),
    )

    # Act & Assert
    with pytest.raises(ValueError) as exc:
        store_extracted_sections(
            db_handler,
            "test_doc",
            "toc",
            [{"heading": "Test", "level": 1, "content": "Content"}],
        )
    assert "Failed to get document ID" in str(exc.value)


def test_store_sections_database_error(mock_connection: MagicMock) -> None:
    """Test handling of database error during section insertion.

    Verifies that database errors are properly propagated and not swallowed.
    """
    # Arrange
    # Mock that raises an exception for database error
    db_handler = MagicMock(
        transaction=MagicMock(return_value=mock_connection),
        execute_query=MagicMock(side_effect=Exception("Database error")),
    )

    # Act & Assert
    with pytest.raises(Exception) as exc:
        store_extracted_sections(
            db_handler,
            "test_doc",
            "toc",
            [{"heading": "Test", "level": 1, "content": "Content"}],
        )
    assert "Database error" in str(exc.value)
