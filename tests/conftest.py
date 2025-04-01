"""Test configuration and shared fixtures for database handler tests."""

import pytest
from unittest.mock import MagicMock, patch
from psycopg import Connection, Cursor
from psycopg.rows import dict_row

# Test database configuration
TEST_DB_CONFIG = {
    "DB_HOST": "localhost",
    "DB_NAME": "test_db",
    "DB_USER": "test_user",
    "DB_PASSWORD": "test_password",
    "DB_PORT": "5432"
}

@pytest.fixture
def mock_env_vars(monkeypatch):
    """Fixture to set up test environment variables.
    
    Args:
        monkeypatch: Pytest fixture for modifying environment variables
        
    Returns:
        dict: Dictionary containing the test configuration
    """
    for key, value in TEST_DB_CONFIG.items():
        monkeypatch.setenv(key, value)
    return TEST_DB_CONFIG

@pytest.fixture
def mock_connection():
    """Fixture to create a mock database connection.
    
    Returns:
        MagicMock: A mock connection object with required attributes and methods
    """
    cursor = MagicMock(spec=Cursor)
    cursor.fetchall.return_value = []
    cursor.close.return_value = None
    
    conn = MagicMock(spec=Connection)
    conn.closed = False
    conn.cursor.return_value = cursor
    conn.commit.return_value = None
    conn.rollback.return_value = None
    conn.close.return_value = None
    # Set row factory to dict_row to match actual implementation
    conn.row_factory = dict_row
    return conn

@pytest.fixture
def mock_psycopg_connect(mock_connection):
    """Fixture to patch psycopg.connect function.
    
    Args:
        mock_connection: The mock connection fixture
        
    Returns:
        MagicMock: A mock connect function that returns the mock connection
    """
    with patch("psycopg.connect", return_value=mock_connection) as mock:
        yield mock

@pytest.fixture(autouse=True)
def cleanup_logging(caplog):
    """Fixture to clean up logging records after each test.
    
    Args:
        caplog: Pytest's built-in fixture for capturing log messages
    """
    caplog.clear()
    yield
    caplog.clear()
