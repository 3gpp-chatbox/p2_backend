"""Tests for DatabaseHandler initialization and configuration validation."""

import pytest

from src.db.db_handler import DatabaseHandler


def test_initialization_with_valid_config(mock_env_vars):
    """Test successful initialization with all environment variables set."""
    db = DatabaseHandler()
    assert db.host == mock_env_vars["DB_HOST"]
    assert db.dbname == mock_env_vars["DB_NAME"]
    assert db.user == mock_env_vars["DB_USER"]
    assert db.password == mock_env_vars["DB_PASSWORD"]
    assert db.port == mock_env_vars["DB_PORT"]
    assert db.conn is None


def test_initialization_with_default_optional_params(mock_env_vars, monkeypatch):
    """Test initialization with only required variables and default optional ones."""
    # Remove optional parameters from environment
    monkeypatch.delenv("DB_HOST", raising=False)
    monkeypatch.delenv("DB_PORT", raising=False)

    db = DatabaseHandler()
    assert db.host == "localhost"  # Default value
    assert db.port == "5432"  # Default value
    assert db.dbname == mock_env_vars["DB_NAME"]
    assert db.user == mock_env_vars["DB_USER"]
    assert db.password == mock_env_vars["DB_PASSWORD"]


@pytest.mark.parametrize("missing_var", ["DB_NAME", "DB_USER", "DB_PASSWORD"])
def test_initialization_fails_with_missing_required_var(
    mock_env_vars, monkeypatch, missing_var
):
    """Test that initialization fails when a required environment variable is missing.

    Args:
        mock_env_vars: Fixture providing test environment variables
        monkeypatch: Pytest fixture for modifying environment variables
        missing_var: Name of the environment variable to remove
    """
    monkeypatch.delenv(missing_var)

    with pytest.raises(ValueError) as exc_info:
        DatabaseHandler()

    assert "Missing required database configuration" in str(exc_info.value)


def test_initialization_fails_with_all_vars_missing(monkeypatch):
    """Test that initialization fails when all environment variables are missing."""
    # Remove all environment variables
    for var in ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD", "DB_PORT"]:
        monkeypatch.delenv(var, raising=False)

    with pytest.raises(ValueError) as exc_info:
        DatabaseHandler()

    assert "Missing required database configuration" in str(exc_info.value)


def test_initialization_with_empty_values(mock_env_vars, monkeypatch):
    """Test that initialization fails when required variables are empty strings."""
    # Set required variables to empty strings
    for var in ["DB_NAME", "DB_USER", "DB_PASSWORD"]:
        monkeypatch.setenv(var, "")

    with pytest.raises(ValueError) as exc_info:
        DatabaseHandler()

    assert "Missing required database configuration" in str(exc_info.value)


def test_connection_string_formatting(mock_env_vars):
    """Test that the connection string is properly formatted."""
    db = DatabaseHandler()
    conn_string = db._get_connection_string()

    assert f"host={mock_env_vars['DB_HOST']}" in conn_string
    assert f"dbname={mock_env_vars['DB_NAME']}" in conn_string
    assert f"user={mock_env_vars['DB_USER']}" in conn_string
    assert f"password={mock_env_vars['DB_PASSWORD']}" in conn_string
    assert f"port={mock_env_vars['DB_PORT']}" in conn_string
