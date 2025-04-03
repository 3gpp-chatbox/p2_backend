"""Tests for DatabaseHandler connection management functionality."""

import logging
import pytest
from psycopg import OperationalError
from src.db.db_handler import DatabaseHandler


def test_successful_connection(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test that connection is established successfully with valid credentials."""
    caplog.set_level(logging.INFO)
    db = DatabaseHandler()
    db.connect()

    # Verify connection was attempted with correct parameters
    mock_psycopg_connect.assert_called_once()
    conn_string = db._get_connection_string()
    mock_psycopg_connect.assert_called_with(
        conn_string, row_factory=mock_connection.row_factory
    )

    # Verify connection succeeded
    assert db.conn is not None
    assert not db.conn.closed

    # Verify logging
    assert "Establishing database connection..." in caplog.text
    assert "Database connection established successfully" in caplog.text


def test_connection_with_invalid_credentials(
    mock_env_vars, mock_psycopg_connect, caplog
):
    """Test that appropriate error is raised when connection fails due to invalid credentials."""
    caplog.set_level(logging.ERROR)
    mock_psycopg_connect.side_effect = OperationalError("Authentication failed")

    db = DatabaseHandler()
    with pytest.raises(OperationalError) as exc_info:
        db.connect()

    assert "Authentication failed" in str(exc_info.value)
    assert "Failed to connect to database" in caplog.text


def test_connection_timeout(mock_env_vars, mock_psycopg_connect, caplog):
    """Test handling of connection timeout."""
    caplog.set_level(logging.ERROR)
    mock_psycopg_connect.side_effect = OperationalError("Connection timed out")

    db = DatabaseHandler()
    with pytest.raises(OperationalError) as exc_info:
        db.connect()

    assert "Connection timed out" in str(exc_info.value)
    assert "Failed to connect to database" in caplog.text


def test_disconnect_active_connection(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test disconnection of an active database connection."""
    caplog.set_level(logging.INFO)
    db = DatabaseHandler()
    db.connect()

    db.disconnect()

    assert db.conn is None
    mock_connection.close.assert_called_once()
    assert "Closing database connection..." in caplog.text
    assert "Database connection closed" in caplog.text


def test_disconnect_when_already_disconnected(mock_env_vars, caplog):
    """Test disconnection when no active connection exists."""
    caplog.set_level(logging.INFO)
    db = DatabaseHandler()

    # Should not raise any errors
    db.disconnect()

    assert db.conn is None
    assert not caplog.text  # No logging should occur


def test_auto_reconnection(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test that operations automatically reconnect if connection is lost."""
    caplog.set_level(logging.INFO)
    db = DatabaseHandler()

    # Initial connection
    with db.get_cursor() as cursor:
        assert db.conn is not None
        assert not db.conn.closed

    # Simulate connection loss
    db.disconnect()
    assert db.conn is None

    # Should auto-reconnect
    with db.get_cursor() as cursor:
        assert db.conn is not None
        assert not db.conn.closed
        assert "Establishing database connection..." in caplog.text
