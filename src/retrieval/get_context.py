import sys
from pathlib import Path

from src.db.db_handler import DatabaseHandler
from src.db.document import get_document_by_name
from src.retrieval.sections_content_retrieval import get_sections_content
from src.retrieval.toc_retrieval import (
    find_procedure_section_lines,
    get_top_level_sections,
)

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)


def get_context(doc_name: str, procedure_name: str, db_handler: DatabaseHandler) -> str:
    try:
        # Get document
        doc = get_document_by_name(doc_name, db_handler)
        if not doc:
            logger.error(f"Document '{doc_name}' not found in the database.")
            raise ValueError(f"Document '{doc_name}' not found in the database.")

        # Get relevant sections
        section_lines = find_procedure_section_lines(
            toc_lines=doc["toc"].splitlines(), procedure_name=procedure_name
        )

        logger.info(
            f"Found {len(section_lines)} section candidates for '{procedure_name}' in document '{doc_name}'."
        )

        if not section_lines:
            logger.error(
                f"No section lines found for '{procedure_name}' in document '{doc_name}'."
            )
            raise ValueError(
                f"Required section lines found for '{procedure_name}' not found in document '{doc_name}'."
            )

        top_level_sections = get_top_level_sections(section_lines=section_lines)

        if top_level_sections.size == 0:
            logger.error(
                f"No top lkevel sections found for '{procedure_name}' in document '{doc_name}'."
            )
            raise ValueError(
                f"Required top level sections for '{procedure_name}' not found in document '{doc_name}'."
            )

        logger.info(
            f"Found {top_level_sections} top-level sections for '{procedure_name}' in document '{doc_name}'."
        )

        # Get sections content
        context = get_sections_content(
            db_handler=db_handler,
            doc_name=doc_name,
            section_list=list(top_level_sections),
        )

        return context

    except Exception as e:
        logger.error(
            f"Error in `get_context`: Exception encountered while processing document '{doc_name}'. Error: {e}",
            exc_info=True,
        )
        raise ValueError(f"Error retrieving context: {e}")
