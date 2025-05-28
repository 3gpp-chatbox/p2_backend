# Coding Guidelines

## 1. Pythonic Practices

- **Elegance and Readability:** Strive for elegant and Pythonic code that is easy to understand and maintain.
- **PEP 8 Compliance:** Adhere to PEP 8 guidelines for code style, with Ruff as the primary linter and formatter.
- **Explicit over Implicit:** Favor explicit code that clearly communicates its intent over implicit, overly concise code.
- **Zen of Python:** Keep the Zen of Python in mind when making design decisions.

## 2. Modular Design

- **Single Responsibility Principle:** Each module/file should have a well-defined, single responsibility.
- **Reusable Components:** Develop reusable functions and classes, favoring composition over inheritance.
- **Package Structure:** Organize code into logical packages and modules.

## 3. Code Quality

- **Comprehensive Type Annotations:** All functions, methods, and class members must have type annotations, using the most specific types possible.
- **Detailed Docstrings:** All functions, methods, and classes must have Google-style docstrings, thoroughly explaining their purpose, parameters, return values, and any exceptions raised. Include usage examples where helpful.
- **Thorough Unit Testing:** Aim for high test coverage (90% or higher) using `pytest`. Test both common cases and edge cases.When testing each function should have at least one success, one fail and one edge case test.
- **Robust Exception Handling:** Use specific exception types, provide informative error messages, and handle exceptions gracefully. Implement custom exception classes when needed. Avoid bare `except` clauses.
- **Logging:** Employ the `logging` module judiciously to log important events, warnings, and errors.

## 4. Performance Optimization

- **Asynchronous Programming:** Leverage `async` and `await` for I/O-bound operations to maximize concurrency.
- **Caching:** Apply `functools.lru_cache`, `@cache` (Python 3.9+), or `fastapi.Depends` caching where appropriate.
- **Resource Monitoring:** Use `psutil` or similar to monitor resource usage and identify bottlenecks.
- **Memory Efficiency:** Ensure proper release of unused resources to prevent memory leaks.
- **Concurrency:** Employ `concurrent.futures` or `asyncio` to manage concurrent tasks effectively.
- **Database Best Practices:** Design database schemas efficiently, optimize queries, and use indexes wisely.

## 5. API Development with FastAPI

- **Data Validation:** Use Pydantic models for rigorous request and response data validation.
- **Dependency Injection:** Effectively use FastAPI's dependency injection for managing dependencies.
- **Routing:** Define clear and RESTful API routes using FastAPI's `APIRouter`.
- **Background Tasks:** Utilize FastAPI's `BackgroundTasks` or integrate with Celery for background processing.
- **Security:** Implement robust authentication and authorization (e.g., OAuth 2.0, JWT).
- **Documentation:** Auto-generate API documentation using FastAPI's OpenAPI support.
- **Versioning:** Plan for API versioning from the start (e.g., using URL prefixes or headers).
- **CORS:** Configure Cross-Origin Resource Sharing (CORS) settings correctly.

# Code Example Requirements

- All functions must include type annotations.
- Must provide clear, Google-style docstrings.
- Key logic should be annotated with comments.
- Provide usage examples (e.g., as a `__main__` section).
- Include error handling.
- Use `ruff` for code formatting.
- When creating a new file **ALWAYS** check if this functionality/file already exists.
- Always use explicit parameter names when calling functions (e.g., `my_function(param1="value", param2="value")` instead of `my_function("value", "value")`).
