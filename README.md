# 3GPP Document Processor

A backend application for processing and analyzing 3GPP specification documents. This tool can ingest .docx specification files, extract procedures state machines, and store structured data in PostgreSQL for further analysis.

## Project Overview

The application consists of several key components:

- **Document ingestion and preprocessing**: Handles the initial parsing of .docx files
- **Procedure state machine extraction**: Analyzes document content to identify and extract state machines
- **Database storage and retrieval**: Manages persistent storage of extracted data
- **API endpoints**: Provides RESTful access to the processed data

## Requirements

- Python 3.8 or higher
- PostgreSQL database
- Required Python packages (listed in `requirements.txt`)
- 3GPP specification documents in .docx format
- Google Gemini API key

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Configure the `.env` file with your settings:
   - Database connection details
   - Google Gemini API credentials
   - Document processing paths

## Database Setup

Initialize the database schema:

```bash
python -m src.db.init_db
```

## Usage

### 1. Document Processing

To process a 3GPP document:

1. Place your .docx file in the project directory
2. Update the document path in `.env`
3. Run the document processor:
   ```bash
   python -m src.retrieval.document_processor
   ```

#### Document Processing Output

The document processor generates several markdown files in `data/markdown/` for debugging and review:

- **doc-excluded.md**: Contains document content that is filtered out and not stored in the database
- **doc-filtered.md**: Contains the processed content that will be stored in the database
- **doc-toc.md**: Contains the extracted table of contents that will be used for document structure

### 2. Procedure Extraction

Extract procedures from the processed document:

```bash
python -m src.extraction.extract_procedure
```

#### Extraction Output

The extraction process stores detailed information in `data/output/`:
- Complete prompt contexts used for extraction
- Results from each extraction step
- Intermediate processing data
- Validation and accuracy metrics

### 3. API Server

Start the API server with:

```bash
uvicorn src.API.main:app --reload
```

#### API Endpoints

Base URL: `/procedures`

##### Available Endpoints

1. `GET /procedures/`
   - Lists all available procedures with their IDs and names

2. `GET /procedures/{procedure_id}`
   - Returns detailed procedure information including graphs, metrics, and metadata

3. `PUT /procedures/{procedure_id}`
   - Updates a procedure's graph data and metadata

## Project Structure

```
src/
├── API/            # REST API implementation and routes
├── db/             # Database models and migrations
├── extraction/     # Procedure extraction algorithms
├── retrieval/      # Document processing and content extraction
├── lib/            # Shared utilities and helpers
└── schemas/        # Data models and validation

tests/              # Comprehensive test suite
docs/               # Additional documentation

data/               # Generated data and output files
├── markdown/       # Processed document content
├── output/         # Extraction results and metrics
└── raw/           # Original source documents
```


