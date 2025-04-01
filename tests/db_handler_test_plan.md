# Database Handler Test Plan

This document outlines the testing strategy for the `src/db/db_handler.py` module. The plan follows a comprehensive approach to ensure the database handler's functionality, reliability, and error handling capabilities are thoroughly tested.

## Testing Philosophy
- Each test should have clear success, failure, and edge cases
- Tests should be isolated and not depend on each other
- Use mocking to avoid actual database connections where possible
- Use parametrized tests for multiple similar test cases

## General Setup

- [x] **Environment Setup:**
  - [x] Create `tests/conftest.py` with pytest fixtures for:
    - [x] Mock environment variables using `monkeypatch`
    - [x] Mock psycopg connection using `pytest-mock`
    - [x] Test database configuration with test-specific values
  - [x] Set up logging capture using `caplog` fixture
  - [x] Implement cleanup fixtures to reset state after each test

✓ **Milestone Complete:** General setup has been implemented. Created conftest.py with all required fixtures including environment variables mocking, database connection mocking, test configuration, and logging capture. All fixtures follow best practices with proper documentation and type hints.

## Tests for Initialization (`test_initialization.py`)

- [x] **Configuration Validity:**
  - [x] Test that `ValueError` is raised when:
    - [x] All environment variables are missing
    - [x] Each required variable is missing individually (DB_NAME, DB_USER, DB_PASSWORD)
    - [x] Various combinations of missing variables
  - [x] Test successful initialization with:
    - [x] All environment variables set
    - [x] Default values for optional parameters (host="localhost", port="5432")

✓ **Milestone Complete:** Initialization tests have been implemented. Created test_initialization.py covering all configuration scenarios including missing variables, empty values, and successful initialization cases. Tests use parameterization for efficiency and include proper error message validation.

## Tests for Connection Management (`test_connection.py`)

- [x] **Successful Connection:**
  - [x] Test successful connection with valid credentials
  - [x] Verify connection state attributes (closed=False)
  - [x] Test connection string formatting
  - [x] Verify logging messages for successful connection
- [x] **Connection Failure:**
  - [x] Test connection with invalid host
  - [x] Test connection with invalid credentials
  - [x] Test connection timeout
  - [x] Verify proper error logging and exception propagation
- [x] **Disconnect:**
  - [x] Test disconnection of active connection
  - [x] Test disconnection when already disconnected
  - [x] Verify connection cleanup
  - [x] Test auto-reconnection on subsequent operations

✓ **Milestone Complete:** Connection management tests have been implemented and verified. Created test_connection.py covering all connection scenarios including successful connections, failure cases (invalid credentials, timeouts), and disconnection handling. Tests verify proper logging, error propagation, and automatic reconnection functionality.

## Tests for Query Execution (`test_query.py`)

- [ ] **Basic Query Execution:**
  - [ ] Test SELECT query with fetch=True returns list of dictionaries
  - [ ] Test INSERT/UPDATE query with fetch=False returns None
  - [ ] Test empty result set handling
  - [ ] Test query timeout handling
- [ ] **Query Parameters:**
  - [ ] Test with different parameter types (str, int, bool, None)
  - [ ] Test with single and multiple parameters
  - [ ] Test with invalid parameter types
  - [ ] Test SQL injection prevention
- [ ] **Commit and Rollback:**
  - [ ] Test automatic commit after successful query
  - [ ] Test automatic rollback after failed query
  - [ ] Test explicit transaction handling
  - [ ] Verify proper cleanup after rollback
    
## Tests for Cursor Management (`test_cursor.py`)

- [ ] **Cursor Context Manager:**
  - [ ] Test cursor acquisition and automatic closure
  - [ ] Verify cursor attributes and methods are accessible
  - [ ] Test cursor closure on normal execution
  - [ ] Test cursor closure after exceptions
  - [ ] Verify cursor state through context manager lifecycle

- [ ] **Cursor Error Scenarios:**
  - [ ] Test cursor creation with closed connection
  - [ ] Test cursor operations after connection loss
  - [ ] Verify error propagation in cursor operations
  - [ ] Test cursor cleanup after various error conditions
  - [ ] Verify logging of cursor-related errors

## Tests for Transaction Management (`test_transaction.py`)

- [ ] **Transaction Context Manager:**
  - [ ] Test successful transaction commit
  - [ ] Test transaction rollback on exceptions
  - [ ] Verify connection state during transaction
  - [ ] Test transaction isolation levels
  - [ ] Verify proper cleanup after transaction

- [ ] **Complex Transaction Scenarios:**
  - [ ] Test nested transactions behavior
  - [ ] Test concurrent transactions
  - [ ] Test transaction timeouts
  - [ ] Verify savepoint handling
  - [ ] Test partial rollbacks

- [ ] **Edge Cases:**
  - [ ] Test transaction with connection loss
  - [ ] Test extremely large transactions
  - [ ] Test rapid transaction creation/completion
  - [ ] Verify dead transaction handling

## Tests for Context Manager & Resource Cleanup (`test_lifecycle.py`)

- [ ] **Database Handler Context Management:**
  - [ ] Test context manager entry/exit
  - [ ] Verify resource acquisition and release
  - [ ] Test with nested context managers
  - [ ] Verify state after context exit
  - [ ] Test error handling in context manager

- [ ] **Resource Cleanup:**
  - [ ] Test `__del__` method behavior
  - [ ] Verify connection cleanup on deletion
  - [ ] Test cleanup with active transactions
  - [ ] Test cleanup with active cursors
  - [ ] Verify memory cleanup

## Tests for Logging and Error Handling (`test_logging.py`)

- [ ] **Logging Verification:**
  - [ ] Test log messages for all major operations
  - [ ] Verify log levels are appropriate
  - [ ] Test log formatting and content
  - [ ] Verify error stack traces in logs
  - [ ] Test log handling during concurrent operations

- [ ] **Exception Handling:**
  - [ ] Test all custom exception types
  - [ ] Verify exception inheritance chain
  - [ ] Test exception message formatting
  - [ ] Verify cleanup after exceptions
  - [ ] Test exception context preservation

## Best Practices and Conventions

- **File Organization:**
  - Group related tests in separate files (e.g., `test_initialization.py`, `test_connection.py`)
  - Use `conftest.py` for shared fixtures
  - Keep test files organized in `tests/db/` directory

- **Test Structure:**
  - Follow Arrange-Act-Assert pattern
  - Use descriptive test names: `test_should_[expected_behavior]_when_[condition]`
  - Document complex test scenarios with docstrings
  - Use type hints in test functions

- **Mocking Guidelines:**
  - Mock external dependencies (psycopg, environment variables)
  - Use context managers for temporary state changes
  - Properly clean up mocked resources

- **Test Data:**
  - Use factories or fixtures for test data
  - Avoid hardcoding test values
  - Use meaningful test data that represents real scenarios

- **Error Handling:**
  - Test both expected and unexpected error cases
  - Verify error messages and logging
  - Ensure proper resource cleanup after errors

- **Documentation:**
  - Update this test plan as new test cases are identified
  - Mark completed tests with checkmarks
  - Document any testing gotchas or special considerations
