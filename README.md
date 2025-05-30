# 3GPP Document Processor

A backend application for processing and analyzing 3GPP specification documents. This tool can ingest .docx specification files, extract procedures state machines, and store structured data in PostgreSQL.

## Project Overview

The application consists of several key components:

- **Document ingestion and preprocessing**: Handles the initial parsing of .docx files
- **Procedure state machine extraction**: Analyzes document content to identify and extract state machines
- **Database storage and retrieval**: Manages persistent storage of extracted data

## Requirements

- Python 3.12
- uv
- PostgreSQL database
- 3GPP specification documents in .docx format
- Google Gemini or OpenAI API key

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Configure the `.env` file with your settings:
   - Database connection details
   - Google Gemini/OpenAI API credentials
   - Document processing paths

## Database Setup

Initialize the database schema (⚠️This is only done once running it again will reset the tables!):

```bash
uv run python -m src.db.init_db
```

## Usage

### 1. Document Processing

To process a 3GPP document:

1. Place your .docx file in the project directory
2. Update the document path in `.env`
3. Run the document processor:
   ```bash
   uv run python -m src.retrieval.document_processor
   ```

#### Document Processing Pipeline

The document processor performs a sophisticated multi-stage pipeline:

1. **DOCX to Markdown Conversion:**

   - Processes the DOCX file to extract structured content
   - Normalizes whitespace and cleans headings
   - Preserves tables and their formatting
   - Extracts document metadata (spec number, version, release)

2. **Content Filtering and Organization:**

   - Filters out excluded sections (e.g., annexes, forewords, abbreviations)
   - Maintains document hierarchy and heading levels
   - Generates three output files in `data/markdown/`:
     - **doc-filtered.md**: Main content for database storage
     - **doc-excluded.md**: Filtered-out content for review
     - **doc-toc.md**: Extracted table of contents structure

3. **Content Chunking:**

   - Splits content into manageable chunks based on headings
   - Preserves hierarchical relationships between sections
   - Extracts metadata for each chunk (heading, level, content)
   - Maintains document structure integrity

4. **Database Storage:**
   - Stores document metadata (spec, version, release)
   - Creates hierarchical section relationships using LTREE paths
   - Encodes section headings to ensure database compatibility
   - Preserves parent-child relationships between sections

### 2. Procedure Extraction

Extract procedures from the processed document:

```bash
uv run python -m src.extraction.extract_procedure_cli
```

#### Extraction Output

The extraction process follows a sophisticated multi-stage workflow:

1. **Context Retrieval:**

   - Fetches relevant context for the specified procedure from the chosen document
   - Saves the retrieved context for debugging and validation

2. **Prompt Chain Execution:**
   The process uses a 4-stage prompting chain:

   - **Initial Extraction:** Generates the base procedure graph
   - **Evaluation:** Validates the initial extraction against the original context
   - **Correction:** Applies fixes based on the evaluation feedback
   - **Enrichment:** Enhances the graph with additional details and metadata

3. **Multi-Model Extraction:**
   The prompt chain is executed three times:

   - **Main Extraction:** Using the primary model
   - **Alternative Extraction:** Using a secondary model
   - **Modified/Alternative_2 Extraction:** Either uses a modified prompt with the main model or a third alternative model

4. **Accuracy Comparison:**

   - Uses SBERT (Sentence-BERT) embeddings to compute semantic similarity
   - Performs node-by-node and edge-by-edge matching using cosine similarity
   - Applies a fixed threshold (0.8) for valid matches
   - Calculates match percentages for nodes and edges separately
   - Determines overall graph similarity scores
   - Logs detailed accuracy metrics for each extraction method

5. **Result Selection and Storage:**
   - Selects the best result using `get_best_result()` based on accuracy scores and method priority
   - Stores the selected result in the database with comprehensive metadata:
     - Extraction method
     - Model name
     - Accuracy score
     - Graph version and status

## Project Structure

```
src/
├── accuracy/     # Accuracy validation and comparison scripts
├── db/           # Database models, handlers, migrations, and dummy data
├── extraction/   # Procedure extraction algorithms and CLI tools
├── lib/          # Shared utilities and helper modules
├── prompts/      # Prompt templates for LLM-based extraction
├── retrieval/    # Document processing, chunking, and content extraction
└── schemas/      # Data models and validation
```
