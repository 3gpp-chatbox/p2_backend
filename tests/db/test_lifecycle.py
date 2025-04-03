"""Tests for DatabaseHandler's context management and lifecycle functionality.

This module contains tests for the DatabaseHandler's context manager methods and
resource cleanup behavior, ensuring proper connection management throughout the
lifecycle of the handler.
"""

import logging
import pytest
from psycopg import Error
from pytest_mock import MockerFixture

from src.db.db_handler import DatabaseHandler


@pytest.fixture
def db_handler(mock_env_vars: None) -> DatabaseHandler:
    """Provides a DatabaseHandler instance with mocked environment variables.

    Args:
        mock_env_vars: Fixture that sets up mock environment variables.

    Returns:
        DatabaseHandler: Configured database handler instance.
    """
    return DatabaseHandler()


def test_should_connect_on_context_entry(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test that entering context manager establishes connection.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
        caplog: Fixture to capture log messages.
    """
    caplog.set_level(logging.INFO)

    assert db_handler.conn is None

    with db_handler:
        assert db_handler.conn is not None
        assert not db_handler.conn.closed
        assert "Database connection established successfully" in caplog.text


def test_should_disconnect_on_context_exit(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test that exiting context manager closes connection.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
        caplog: Fixture to capture log messages.
    """
    caplog.set_level(logging.INFO)

    with db_handler:
        assert db_handler.conn is not None
        assert not db_handler.conn.closed

    assert "Database connection closed" in caplog.text
    mock_connection.close.assert_called_once()


def test_should_cleanup_on_deletion(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
) -> None:
    """Test that deleting handler cleans up resources.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
    """
    db_handler.connect()
    assert db_handler.conn is not None

    # Simulate deletion
    db_handler.__del__()

    mock_connection.close.assert_called_once()
    assert db_handler.conn is None


def test_should_handle_errors_during_context_exit(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test error handling during context manager exit.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
        caplog: Fixture to capture log messages.
    """
    caplog.set_level(logging.ERROR)

    # Simulate error during close
    mock_connection.close.side_effect = Error("Failed to close connection")

    # Context manager should handle the error gracefully
    with pytest.raises(Error) as exc_info:
        with db_handler:
            pass  # Just test the exit behavior

    assert "Failed to close connection" in str(exc_info.value)


def test_should_handle_nested_context_managers(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
) -> None:
    """Test behavior with nested context manager usage.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
    """
    # Each context manager operates independently, so we expect connect/disconnect pairs
    mock_connection.close.reset_mock()

    # First level - should connect and stay connected within its block
    with db_handler:
        assert db_handler.conn is not None
        assert not db_handler.conn.closed
        mock_connection.close.reset_mock()  # Reset to test inner context

        # Second level - should reconnect since previous context closed
        with db_handler:
            assert db_handler.conn is not None
            assert not db_handler.conn.closed
            mock_connection.close.reset_mock()  # Reset to test inner context exit

        # Inner context exit should close its connection
        mock_connection.close.assert_called_once()

    # Outer context exit should close its connection
    mock_connection.close.assert_called_once()
