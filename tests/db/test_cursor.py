"""Tests for DatabaseHandler cursor management functionality."""

import logging
import pytest
from psycopg import Error, OperationalError, ProgrammingError
from src.db.db_handler import DatabaseHandler


def test_cursor_acquisition_and_closure(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test that cursor is properly acquired and closed."""
    caplog.set_level(logging.INFO)
    db = DatabaseHandler()

    with db.get_cursor() as cursor:
        assert cursor is mock_connection.cursor.return_value
        assert not cursor.closed

    # Verify cursor was closed after context exit
    cursor.close.assert_called_once()


def test_cursor_attributes_accessible(
    mock_env_vars, mock_psycopg_connect, mock_connection
):
    """Test that cursor attributes and methods are accessible within context."""
    db = DatabaseHandler()

    with db.get_cursor() as cursor:
        # Test basic cursor attributes
        assert hasattr(cursor, "execute")
        assert hasattr(cursor, "fetchall")
        assert hasattr(cursor, "close")

        # Test method calls
        cursor.execute("SELECT 1")
        cursor.fetchall.assert_not_called()  # Shouldn't be called unless explicitly requested


def test_cursor_closure_after_exception(
    mock_env_vars, mock_psycopg_connect, mock_connection
):
    """Test that cursor is properly closed even if an exception occurs."""
    db = DatabaseHandler()

    with pytest.raises(ValueError):
        with db.get_cursor() as cursor:
            raise ValueError("Test exception")

    # Verify cursor was closed despite exception
    cursor.close.assert_called_once()


def test_cursor_creation_with_closed_connection(
    mock_env_vars, mock_psycopg_connect, mock_connection
):
    """Test cursor creation when connection is closed."""
    mock_connection.closed = True
    db = DatabaseHandler()

    with db.get_cursor() as cursor:
        assert not db.conn.closed
        assert cursor is mock_connection.cursor.return_value

    # Verify auto-reconnection happened
    assert mock_psycopg_connect.called


def test_cursor_operations_after_connection_loss(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test handling of cursor operations when connection is lost."""
    caplog.set_level(logging.ERROR)
    db = DatabaseHandler()

    # Simulate connection loss during cursor operation
    mock_connection.cursor.side_effect = OperationalError("Connection lost")

    with pytest.raises(OperationalError) as exc_info:
        with db.get_cursor() as cursor:
            pass

    assert "Connection lost" in str(exc_info.value)
    assert "Error while getting cursor" in caplog.text


def test_cursor_error_propagation(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test that cursor errors are properly propagated and logged."""
    caplog.set_level(logging.ERROR)
    db = DatabaseHandler()

    # Test different types of errors
    error_types = [
        (OperationalError, "Database operation failed"),
        (ProgrammingError, "Invalid cursor operation"),
        (Exception, "Unexpected error"),
    ]

    for error_class, message in error_types:
        mock_connection.cursor.side_effect = error_class(message)

        with pytest.raises(
            error_class if isinstance(error_class, type(Error)) else ProgrammingError
        ) as exc_info:
            with db.get_cursor() as cursor:
                pass

        assert message in str(exc_info.value)
        assert "Error while getting cursor" in caplog.text
        caplog.clear()


def test_cursor_cleanup_after_errors(
    mock_env_vars, mock_psycopg_connect, mock_connection
):
    """Test proper cleanup of cursor resources after various error conditions."""
    db = DatabaseHandler()
    cursor = mock_connection.cursor()

    # Test cleanup after execution error
    cursor.execute.side_effect = Error("Execute failed")
    with pytest.raises(Error):
        with db.get_cursor() as cur:
            cur.execute("SELECT 1")

    # Verify cursor was closed
    cursor.close.assert_called()


def test_cursor_state_lifecycle(mock_env_vars, mock_psycopg_connect, mock_connection):
    """Test cursor state throughout its lifecycle."""
    db = DatabaseHandler()

    # Before context
    assert not hasattr(db, "_cursor")

    # Enter context
    with db.get_cursor() as cursor:
        assert cursor is mock_connection.cursor.return_value
        assert not cursor.closed

        # During context
        cursor.execute("SELECT 1")
        assert mock_connection.cursor().execute.called

    # After context
    assert cursor.close.called


def test_cursor_logging(mock_env_vars, mock_psycopg_connect, mock_connection, caplog):
    """Test logging of cursor-related operations and errors."""
    caplog.set_level(logging.ERROR)
    db = DatabaseHandler()

    # Test logging of cursor creation error
    mock_connection.cursor.side_effect = OperationalError("Cursor creation failed")

    with pytest.raises(OperationalError):
        with db.get_cursor() as cursor:
            pass

    assert "Error while getting cursor: Cursor creation failed" in caplog.text
