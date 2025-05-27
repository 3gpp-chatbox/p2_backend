"""Database initialization script.

This script handles the initialization and cleaning of the database schema by executing
SQL migration files in the correct order. It utilizes the DatabaseHandler for
connection management and SQL execution.
"""

from pathlib import Path

from dotenv import load_dotenv

from src.db.db_handler import DatabaseHandler
from src.lib.logger import logger, setup_logger


def read_sql_file(file_path: Path) -> str:
    """Read the content of a SQL file.

    Args:
        file_path: Path to the SQL file.

    Returns:
        str: Content of the SQL file.

    Raises:
        FileNotFoundError: If the SQL file does not exist.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"SQL file not found: {file_path}")
        raise
    except IOError as e:
        logger.error(f"Error reading SQL file {file_path}: {str(e)}")
        raise


def initialize_database(db_handler: DatabaseHandler, migrations_path: Path) -> None:
    """Initialize the database by executing migration files.

    This function executes the SQL migration files in the correct order:
    1. Drops existing tables and objects
    2. Creates new tables and objects

    Args:
        db_handler: Instance of DatabaseHandler for database operations.
        migrations_path: Path to the migrations directory.

    Raises:
        ValueError: If required migration files are missing.
        Exception: If there's an error executing SQL statements.
    """
    migration_files = [
        ("drop_table.sql", "Schema cleanup"),
        ("table.sql", "Schema creation"),
    ]

    try:
        for filename, description in migration_files:
            file_path = migrations_path / filename
            logger.info(f"Executing {description} from {filename}")

            sql_content = read_sql_file(file_path)
            db_handler.execute_query(sql_content, fetch=False)

            logger.info(f"Successfully completed {description}")

    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise


def main() -> None:
    """Main function to initialize the database."""
    load_dotenv(override=True)
    setup_logger()  # Set up logging configuration

    # Get the migrations directory path
    migrations_path = Path(__file__).parent / "migrations"

    if not migrations_path.exists():
        raise ValueError(f"Migrations directory not found at {migrations_path}")

    logger.info("Starting database initialization")

    try:
        with DatabaseHandler() as db:
            initialize_database(db, migrations_path)
            logger.info("Database initialization completed successfully")

    except Exception as e:
        logger.error(f"Failed to initialize database: {str(e)}")
        raise


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Database initialization script failed: {str(e)}")
        raise
