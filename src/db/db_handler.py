"""Database handler module for managing PostgreSQL database connections and operations.

This module provides a DatabaseHandler class that manages database connections,
transactions, and CRUD operations with proper resource management and error handling.
"""

import os
import logging
from contextlib import contextmanager
from typing import Any, Dict, List, Optional, Generator

from dotenv import load_dotenv
import psycopg
from psycopg import OperationalError, ProgrammingError, Error
from psycopg.rows import dict_row
from psycopg.connection import Connection
from psycopg.cursor import Cursor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv(override=True)


class DatabaseHandler:
    """A class to handle PostgreSQL database operations with connection pooling and error handling.

    This class provides methods for database operations with proper connection management,
    error handling, and resource cleanup.

    Attributes:
        conn (Optional[Connection]): The database connection object.
        host (str): Database host address.
        dbname (str): Database name.
        user (str): Database user.
        password (str): Database password.
        port (str): Database port.
    """

    def __init__(self) -> None:
        """Initialize the DatabaseHandler with connection parameters from environment variables."""
        self.conn: Optional[Connection] = None
        self.host: str = os.getenv("DB_HOST", "localhost")
        self.dbname: str = os.getenv("DB_NAME", "")
        self.user: str = os.getenv("DB_USER", "")
        self.password: str = os.getenv("DB_PASSWORD", "")
        self.port: str = os.getenv("DB_PORT", "5432")

        if not all([self.dbname, self.user, self.password, self.port]):
            raise ValueError("Missing required database configuration")

    def _get_connection_string(self) -> str:
        """Generate the connection string from instance attributes.

        Returns:
            str: Formatted connection string for database connection.
        """
        return (
            f"host={self.host} "
            f"dbname={self.dbname} "
            f"user={self.user} "
            f"password={self.password} "
            f"port={self.port}"
        )

    def connect(self) -> None:
        """Establish a connection to the database.

        Raises:
            OperationalError: If connection cannot be established.
            ValueError: If required configuration is missing.
        """
        try:
            if not self.conn or self.conn.closed:
                logger.info("Establishing database connection...")
                self.conn = psycopg.connect(
                    self._get_connection_string(), row_factory=dict_row
                )
                logger.info("Database connection established successfully")
        except Exception as e:
            logger.error(f"Failed to connect to database: {str(e)}")
            raise OperationalError(f"Database connection failed: {str(e)}")

    def disconnect(self) -> None:
        """Close the database connection if it exists."""
        if self.conn and not self.conn.closed:
            logger.info("Closing database connection...")
            self.conn.close()
            self.conn = None
            logger.info("Database connection closed")

    @contextmanager
    def get_cursor(self) -> Generator[Cursor, None, None]:
        """Get a database cursor using context management.

        Yields:
            Cursor: Database cursor object.

        Raises:
            OperationalError: If connection issues occur.
            ProgrammingError: If cursor creation fails due to programming errors.
        """
        if not self.conn:
            self.connect()

        try:
            cursor = self.conn.cursor()
            yield cursor
        except Exception as e:
            logger.error(f"Error while getting cursor: {str(e)}")
            if isinstance(e, Error):
                raise e
            raise ProgrammingError(f"Cursor operation failed: {str(e)}")
        finally:
            if "cursor" in locals():
                cursor.close()

    def execute_query(
        self, query: str, parameters: Optional[tuple] = None, fetch: bool = True
    ) -> Optional[List[Dict[str, Any]]]:
        """Execute a SQL query and optionally return results.

        Args:
            query (str): SQL query to execute.
            parameters (Optional[tuple]): Query parameters.
            fetch (bool): Whether to return results.

        Returns:
            Optional[List[Dict[str, Any]]]: Query results if fetch is True, None otherwise.

        Raises:
            OperationalError: If connection issues occur.
            ProgrammingError: If query syntax is invalid or execution fails.
            DataError: If data type mismatches occur.
            IntegrityError: If database constraints are violated.
        """
        try:
            with self.get_cursor() as cursor:
                cursor.execute(query, parameters)

                if fetch:
                    results = cursor.fetchall()
                    self.conn.commit()
                    return results

                self.conn.commit()
                return None

        except Exception as e:
            if self.conn:
                self.conn.rollback()
            logger.error(f"Query execution failed: {str(e)}")
            if isinstance(e, Error):
                raise e
            raise ProgrammingError(f"Query execution failed: {str(e)}")

    @contextmanager
    def transaction(self) -> Generator[None, None, None]:
        """Context manager for database transactions.

        Yields:
            None

        Raises:
            OperationalError: If connection issues occur.
            ProgrammingError: If transaction operations fail due to programming errors.
            IntegrityError: If database constraints are violated.
        """
        if not self.conn:
            self.connect()

        try:
            logger.debug("Starting transaction...")
            yield
            self.conn.commit()
            logger.debug("Transaction committed")
        except Exception as e:
            logger.error(f"Transaction failed: {str(e)}")
            self.conn.rollback()
            logger.debug("Transaction rolled back")
            if isinstance(e, Error):
                raise e
            raise ProgrammingError(f"Transaction failed: {str(e)}")

    def __enter__(self) -> "DatabaseHandler":
        """Enter context manager and establish connection.

        Returns:
            DatabaseHandler: Self reference for context management.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager and cleanup resources."""
        self.disconnect()

    def __del__(self) -> None:
        """Destructor to ensure connection cleanup."""
        self.disconnect()


if __name__ == "__main__":
    # Example usage
    try:
        with DatabaseHandler() as db:
            # Example query
            results = db.execute_query("SELECT * FROM table_name LIMIT 5")
            print(results)

            # Example transaction
            with db.transaction():
                db.execute_query(
                    "INSERT INTO table_name (name) VALUES (%s)",
                    parameters=("value",),
                    fetch=False,
                )
    except Error as e:
        print(f"Database error occurred: {str(e)}")
