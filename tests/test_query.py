"""Tests for DatabaseHandler query execution functionality."""

import logging
import pytest
from psycopg import Error, ProgrammingError, OperationalError
from src.db.db_handler import DatabaseHandler

def test_select_query_with_fetch(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test that SELECT query with fetch=True returns list of dictionaries."""
    caplog.set_level(logging.INFO)
    expected_results = [{"id": 1, "name": "test1"}, {"id": 2, "name": "test2"}]
    mock_connection.cursor().fetchall.return_value = expected_results

    db = DatabaseHandler()
    results = db.execute_query("SELECT * FROM test_table")

    # Verify query execution
    mock_connection.cursor().execute.assert_called_once_with(
        "SELECT * FROM test_table", None
    )
    assert results == expected_results
    assert mock_connection.commit.called
    assert "Query executed successfully with results" in caplog.text

def test_insert_query_without_fetch(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test that INSERT query with fetch=False returns None."""
    caplog.set_level(logging.INFO)
    db = DatabaseHandler()
    parameters = ("test_value",)

    result = db.execute_query(
        "INSERT INTO test_table (name) VALUES (%s)", parameters=parameters, fetch=False
    )

    # Verify query execution
    mock_connection.cursor().execute.assert_called_once_with(
        "INSERT INTO test_table (name) VALUES (%s)", parameters
    )
    assert result is None
    assert mock_connection.commit.called
    assert not mock_connection.cursor().fetchall.called

def test_empty_result_set(mock_env_vars, mock_psycopg_connect, mock_connection):
    """Test handling of queries that return no results."""
    mock_connection.cursor().fetchall.return_value = []

    db = DatabaseHandler()
    results = db.execute_query("SELECT * FROM empty_table")

    assert results == []
    assert mock_connection.commit.called

def test_query_with_different_parameter_types(
    mock_env_vars, mock_psycopg_connect, mock_connection
):
    """Test query execution with different parameter types."""
    db = DatabaseHandler()
    parameters = (42, "string", True, None, 3.14)

    db.execute_query(
        "INSERT INTO test_table VALUES (%s, %s, %s, %s, %s)", parameters=parameters
    )

    mock_connection.cursor().execute.assert_called_once_with(
        "INSERT INTO test_table VALUES (%s, %s, %s, %s, %s)", parameters
    )

def test_query_with_multiple_parameters(
    mock_env_vars, mock_psycopg_connect, mock_connection
):
    """Test query execution with multiple parameters."""
    db = DatabaseHandler()
    params = (1, "test", True)

    db.execute_query(
        "SELECT * FROM test_table WHERE id = %s AND name = %s AND active = %s",
        parameters=params,
    )

    mock_connection.cursor().execute.assert_called_once_with(
        "SELECT * FROM test_table WHERE id = %s AND name = %s AND active = %s", params
    )

def test_failed_query_rollback(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test that failed queries trigger rollback."""
    caplog.set_level(logging.ERROR)
    mock_connection.cursor().execute.side_effect = ProgrammingError("Invalid SQL")

    db = DatabaseHandler()
    with pytest.raises(ProgrammingError) as exc_info:
        db.execute_query("INVALID SQL")

    assert "Invalid SQL" in str(exc_info.value)
    assert mock_connection.rollback.called
    assert "Query execution failed" in caplog.text

def test_automatic_commit_after_successful_query(
    mock_env_vars, mock_psycopg_connect, mock_connection
):
    """Test that successful queries are automatically committed."""
    db = DatabaseHandler()
    db.execute_query("SELECT * FROM test_table")

    assert mock_connection.commit.called
    assert not mock_connection.rollback.called

def test_automatic_rollback_after_failed_query(
    mock_env_vars, mock_psycopg_connect, mock_connection
):
    """Test that failed queries are automatically rolled back."""
    mock_connection.cursor().execute.side_effect = Error("Database error")

    db = DatabaseHandler()
    with pytest.raises(Error):
        db.execute_query("SELECT * FROM test_table")

    assert mock_connection.rollback.called
    assert not mock_connection.commit.called

def test_sql_injection_prevention(mock_env_vars, mock_psycopg_connect, mock_connection):
    """Test that parameterized queries prevent SQL injection."""
    db = DatabaseHandler()
    malicious_input = "'; DROP TABLE users; --"

    db.execute_query(
        "SELECT * FROM users WHERE name = %s", parameters=(malicious_input,)
    )

    # Verify the input was properly parameterized
    mock_connection.cursor().execute.assert_called_once_with(
        "SELECT * FROM users WHERE name = %s", (malicious_input,)
    )

def test_query_timeout(mock_env_vars, mock_psycopg_connect, mock_connection, caplog):
    """Test handling of query timeout."""
    caplog.set_level(logging.ERROR)
    mock_connection.cursor().execute.side_effect = Error("Query timed out")

    db = DatabaseHandler()
    with pytest.raises(Error) as exc_info:
        db.execute_query("SELECT * FROM large_table")

    assert "Query timed out" in str(exc_info.value)
    assert mock_connection.rollback.called
    assert "Query execution failed" in caplog.text

def test_query_error_with_established_connection(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test error handling in execute_query with established connection that needs rollback."""
    caplog.set_level(logging.ERROR)
    db = DatabaseHandler()

    # First establish connection
    db.connect()
    assert db.conn is not None

    # Then make the query fail
    mock_connection.cursor.side_effect = Error("Query failed")

    with pytest.raises(Error) as exc_info:
        db.execute_query("SELECT * FROM test_table")

    assert "Query failed" in str(exc_info.value)
    assert "Query execution failed" in caplog.text
    # Should trigger rollback since connection exists
    mock_connection.rollback.assert_called_once()

def test_query_error_without_established_connection(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test error handling in execute_query without established connection."""
    caplog.set_level(logging.ERROR)
    db = DatabaseHandler()

    # Prevent auto-connection and force no connection scenario
    mock_psycopg_connect.side_effect = OperationalError("Connection unavailable")
    db.conn = None
    
    # This should try to connect, fail, and then execute the error path without a connection
    with pytest.raises(OperationalError) as exc_info:
        db.execute_query("SELECT * FROM test_table")

    # Verify error message
    assert "Database connection failed" in str(exc_info.value)
    assert "Connection unavailable" in str(exc_info.value)
    
    # Verify logs contain the error
    assert "Failed to connect to database" in caplog.text
    
    # No rollback should happen since there was no connection
    mock_connection.rollback.assert_not_called()

def test_should_convert_type_error_to_programming_error(
    mock_env_vars, mock_psycopg_connect, mock_connection, caplog
):
    """Test that non-psycopg errors during query execution are converted to ProgrammingError."""
    caplog.set_level(logging.ERROR)
    db = DatabaseHandler()

    # Simulate a TypeError during query execution
    mock_connection.cursor().execute.side_effect = TypeError("Cannot convert NoneType to string")

    with pytest.raises(ProgrammingError) as exc_info:
        db.execute_query("SELECT * FROM table WHERE id = %s", parameters=None)

    # Verify error conversion
    assert "Cannot convert NoneType to string" in str(exc_info.value)
    assert isinstance(exc_info.value, ProgrammingError)
    assert "Query execution failed" in caplog.text
