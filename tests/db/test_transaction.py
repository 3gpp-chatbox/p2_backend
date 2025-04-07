"""Tests for transaction management functionality in DatabaseHandler.

This module contains tests for transaction-related operations including commits,
rollbacks, and error handling using the transaction context manager.
"""

import logging

import pytest
from psycopg import Error, ProgrammingError
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


def test_should_commit_transaction_when_no_errors(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test successful transaction commit when no errors occur.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
        caplog: Fixture to capture log messages.
    """
    caplog.set_level(logging.DEBUG)

    # Reset any previous calls
    mock_connection.commit.reset_mock()

    with db_handler.transaction():
        pass  # Just test the transaction commit

    # Verify commit was called once
    mock_connection.commit.assert_called_once()
    assert "Transaction committed" in caplog.text
    assert "Transaction rolled back" not in caplog.text


def test_should_rollback_transaction_on_error(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test transaction rollback when an error occurs.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
        caplog: Fixture to capture log messages.
    """
    caplog.set_level(logging.DEBUG)

    # Reset any previous calls
    mock_connection.rollback.reset_mock()

    with pytest.raises(ProgrammingError):
        with db_handler.transaction():
            raise ProgrammingError("Test error")

    # Verify rollback was called
    mock_connection.rollback.assert_called_once()
    assert "Transaction rolled back" in caplog.text
    assert "Transaction committed" not in caplog.text


def test_should_connect_if_not_connected_when_starting_transaction(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
) -> None:
    """Test that transaction automatically connects if not already connected.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
    """
    db_handler.disconnect()
    assert db_handler.conn is None

    with db_handler.transaction():
        assert db_handler.conn is not None
        assert not db_handler.conn.closed


def test_should_handle_connection_loss_during_transaction(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test handling of connection loss during transaction.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
        caplog: Fixture to capture log messages.
    """
    caplog.set_level(logging.ERROR)

    def simulate_connection_loss() -> None:
        """Simulate database connection loss."""
        raise Error("Connection lost")

    mock_connection.commit.side_effect = simulate_connection_loss

    with pytest.raises(Error):
        with db_handler.transaction():
            pass  # Just test the transaction behavior

    assert "Transaction failed" in caplog.text
    mock_connection.rollback.assert_called_once()


def test_should_propagate_database_errors_from_transaction(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
) -> None:
    """Test that database errors are properly propagated from transaction.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
    """
    # Reset any previous calls
    mock_connection.commit.reset_mock()

    # Set up the error
    mock_connection.commit.side_effect = Error("Database error")

    with pytest.raises(Error) as exc_info:
        with db_handler.transaction():
            pass

    assert "Database error" in str(exc_info.value)


def test_should_convert_value_error_to_programming_error(
    db_handler: DatabaseHandler,
    mock_connection: MockerFixture,
    mock_psycopg_connect: MockerFixture,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test that non-psycopg errors in transaction are converted to ProgrammingError.

    Args:
        db_handler: Database handler instance.
        mock_connection: Mocked database connection object.
        mock_psycopg_connect: Mocked psycopg.connect function.
        caplog: Fixture to capture log messages.
    """
    caplog.set_level(logging.ERROR)

    with pytest.raises(ProgrammingError) as exc_info:
        with db_handler.transaction():
            # Simulate a non-psycopg error occurring within transaction
            raise ValueError("Invalid data format")

    # Verify error conversion
    assert "Invalid data format" in str(exc_info.value)
    assert isinstance(exc_info.value, ProgrammingError)
    assert "Transaction failed" in caplog.text
    mock_connection.rollback.assert_called_once()
