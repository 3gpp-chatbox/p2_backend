.PHONY: init_db extract process_document

init_db:  ## Initialize the database
	uv run python -m src.db.init_db

extract:  ## Run the procedure extraction CLI
	uv run python -m src.extraction.extract_procedure_cli

process_document:  ## Process documents for retrieval
	uv run python -m src.retrieval.document_processor
