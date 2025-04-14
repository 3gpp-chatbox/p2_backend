import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

from src.accuracy.sbert_simple import compare_two_datasets
from src.db.db_handler import DatabaseHandler
from src.prompts.prompt_manager import PromptManager
from src.retrieval.sections_content_retrieval import get_sections_content
from src.retrieval.toc_retrieval import (
    find_procedure_section_lines,
    get_top_level_sections,
)
from src.schema_validation import Graph

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)


def get_document_by_name(doc_name: str, db_handler: DatabaseHandler) -> str | None:
    try:
        # Check if the document exists in the database
        query = "SELECT * FROM document WHERE name = %s"
        result = db_handler.execute_query(
            query=query, parameters=(doc_name,), fetch=True
        )
        doc = result[0] if result else None
        if not doc:
            return None

        return doc

    except Exception as e:
        logger.error(
            f"Error in `get_document_by_name`: Exception encountered while retrieving document '{doc_name}'. Error: {e}",
            exc_info=True,
        )
        raise ValueError(f"Error retrieving document: {e}")


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


def main() -> None:
    try:
        load_dotenv(override=True)
        DOCUMENT_NAME = os.getenv("DOCUMENT_NAME")
        MAIN_MODEL = os.getenv("MAIN_MODEL", "gemini-2.0-flash-exp")
        ALTERNATIVE_MODEL = os.getenv("ALTERNATIVE_MODEL", MAIN_MODEL)
        MAIN_MODEL_TEMPERATURE = float(os.getenv("MAIN_MODEL_TEMPERATURE", 0.0))
        ALTERNATIVE_MODEL_TEMPERATURE = float(
            os.getenv("ALTERNATIVE_MODEL_TEMPERATURE", 0.0)
        )
        PROCEDURE_TO_EXTRACT = os.getenv("PROCEDURE_TO_EXTRACT")

        if not PROCEDURE_TO_EXTRACT or not DOCUMENT_NAME:
            raise ValueError(
                "PROCEDURE_TO_EXTRACT and DOCUMENT_NAME must be set in the environment variables."
            )

        # Define the LLM models
        main_model = GeminiModel(model_name=MAIN_MODEL, provider="google-gla")
        alt_model = GeminiModel(model_name=ALTERNATIVE_MODEL, provider="google-gla")

        # instatiate the database handler
        db_handler = DatabaseHandler()

        # Instantiate prompt manager
        prompt_manager = PromptManager()

        # Define the Agent
        main_agent: Agent = Agent(
            model=main_model,
            model_settings={"temperature": MAIN_MODEL_TEMPERATURE},
        )

        # Define the Agent
        alt_agent: Agent = Agent(
            model=alt_model,
            model_settings={"temperature": ALTERNATIVE_MODEL_TEMPERATURE},
            result_type=Graph,
        )

        # Step 1. Get the document
        document = get_document_by_name(doc_name=DOCUMENT_NAME, db_handler=db_handler)

        if not document:
            logger.error(f"Document '{DOCUMENT_NAME}' not found in the database.")
            raise ValueError(f"Document '{DOCUMENT_NAME}' not found in the database.")

        # Step 2: Get the context
        context = get_context(
            doc_name=DOCUMENT_NAME,
            procedure_name=PROCEDURE_TO_EXTRACT,
            db_handler=db_handler,
        )

        # Step 3: Prompt the model to extract the procedure (Prompt Chain)

        # v1-step1
        # Parameters: ['section_name', 'text']

        # v1-step2-evaluate
        # Parameters: ['original_content', 'result_1', 'section_name']

        # v1-step3-correct
        # Parameters: ['result_1', 'result_2', 'section_name']

        # v1-step4-enrich
        # Parameters: ['original_content', 'result_3', 'section_name']

        # Call agent for prompt_1
        prompt_1 = prompt_manager.render_prompt(
            template_name="v1-step1", section_name=PROCEDURE_TO_EXTRACT, text=context
        )

        result_1 = main_agent.run_sync(
            user_prompt=prompt_1,
        ).data

        # Call agent for prompt_2
        prompt_2 = prompt_manager.render_prompt(
            template_name="v1-step2-evaluate",
            original_content=context,
            result_1=result_1,
            section_name=PROCEDURE_TO_EXTRACT,
        )

        result_2 = main_agent.run_sync(
            user_prompt=prompt_2,
        ).data

        prompt_3 = prompt_manager.render_prompt(
            template_name="v1-step3-correct",
            result_1=result_1,
            result_2=result_2,
            section_name=PROCEDURE_TO_EXTRACT,
        )

        result_3 = main_agent.run_sync(user_prompt=prompt_3).data

        prompt_4 = prompt_manager.render_prompt(
            template_name="v1-step4-enrich",
            original_content=context,
            result_3=result_3,
            section_name=PROCEDURE_TO_EXTRACT,
        )

        result_4 = main_agent.run_sync(user_prompt=prompt_4, result_type=Graph).data

        result_4_alt = alt_agent.run_sync(user_prompt=prompt_4, result_type=Graph).data

        # TODO: Step 4:  Validate procedures
        result_4_dict = result_4.model_dump()
        result_4_alt_dict = result_4_alt.model_dump()

        accuracy_result = compare_two_datasets(
            dataset_1=result_4_dict,
            dataset_2=result_4_alt_dict,
            dataset_1_name=PROCEDURE_TO_EXTRACT,
            dataset_2_name=PROCEDURE_TO_EXTRACT,
            fixed_threshold=0.8,
        )

        accuracy_overall_metric = accuracy_result["summary"]["overall_match_percentage"]

        print(accuracy_overall_metric)

        # TODO: Step 5: save to database

        # Convert Graph data to dict
        # store_graph(
        #     name=PROCEDURE_TO_EXTRACT,
        #     document_name=DOCUMENT_NAME,
        #     graph_data=result_4_dict,
        #     accuracy=0.5,
        #     db=db_handler,
        # )

    except Exception as e:
        logger.error(
            f"Error in `main`: An error occurred when extracting procedure: {e}.",
            exc_info=True,
        )
        raise ValueError(f"Error in `main`: {e}")


if __name__ == "__main__":
    try:
        main()

    except Exception:
        # raise ValueError(f"Error in `__main__`: {e}")
        sys.exit(1)
