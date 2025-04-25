# 3GPP Phase 2 Backend Application

A Python FastAPI backend application for processing and managing 3GPP procedures. The application provides APIs for data extraction, validation, and management of 3GPP specifications.

## Project Structure

```
p2_backend/
├── src/
│   ├── schemas/       # Data validation schemas
│   ├── prompts/       # AI prompt templates
│   ├── lib/          # Utility functions
│   ├── extraction/   # Data extraction logic
│   ├── retrieval/    # Data retrieval services
│   ├── db/          # Database operations
│   ├── accuracy/    # Accuracy validation
│   └── API/        # API endpoints
├── tests/           # Test suite
│   ├── test_schema_validation.py
│   ├── test_retrieve_toc_section.py
│   ├── test_prompt_manager.py
│   ├── test_jsontomermaid.py
│   ├── test_accuracy_validation.py
│   ├── confitest.py
│   ├── retrieval/
│   └── db/
├── data/            # Data files and resources
├── docs/            # Documentation
└── requirements.txt # Python dependencies
```

## Tech Stack

- Python FastAPI for API development
- PostgreSQL for data storage
- Google GenAI API for AI-powered features
- Pydantic for data validation
- Sentence Transformers for embedding similarity comparisons. 
- LangGraph for AI agent orchestration
- Pytest for testing
- Ruff for linting and formatting

## Key Features

- Data extraction from 3GPP specifications
- Schema validation for procedure data
- AI-powered prompt management
- Database integration for procedure storage
- Accuracy validation for extracted data
- API endpoints for data retrieval and management
- Comprehensive test suite

## Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Google GenAI API credentials

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd p2_backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   GOOGLE_GENAI_API_KEY=your_api_key
   ```

5. Initialize the database:
   ```bash
   # Add database initialization commands here
   ```

6. Start the development server:
   ```bash
   uvicorn src.main:app --reload
   ```

## Development Guidelines

- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings for all modules, classes, and functions
- Add tests for new features
- Use pre-commit hooks for code quality checks
- Document complex logic with comments

## Testing

The application has a comprehensive test suite using pytest. Tests are located in the `tests` directory and include:

- Schema validation tests (`test_schema_validation.py`)
- TOC section retrieval tests (`test_retrieve_toc_section.py`)
- Prompt management tests (`test_prompt_manager.py`)
- JSON to Mermaid conversion tests (`test_jsontomermaid.py`)
- Accuracy validation tests (`test_accuracy_validation.py`)
- Database tests (in `tests/db/` directory)
- Retrieval tests (in `tests/retrieval/` directory)
- Configuration tests (`confitest.py`)

To run all tests:
```bash
pytest
```

To run specific test files:
```bash
pytest tests/test_schema_validation.py
```

To run tests with coverage:
```bash
pytest --cov=src tests/
```

## API Documentation

The API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
