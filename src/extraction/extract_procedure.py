import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

from src.accuracy.sbert_simple import compare_two_datasets
from src.db.db_handler import DatabaseHandler
from src.extraction.store_graphs import store_graph
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


def compare_datasets(
    target_dataset: dict,
    comparison_datasets: list[dict],
    procedure_name: str,
    fixed_threshold: float = 0.8,
) -> float:
    """Compare a target dataset against multiple comparison datasets and compute average accuracy.

    This function compares a target dataset against multiple comparison datasets using
    `compare_two_datasets`. It calculates the average accuracy across all comparisons,
    providing a single overall accuracy score. This is useful when you want to assess
    how well a reference dataset aligns with multiple variations.

    Args:
        target_dataset (dict): The reference dataset to compare against others.
        comparison_datasets (list[dict]): List of datasets to compare against the target.
        procedure_name (str): Name of the procedure used in comparisons.
        fixed_threshold (float, optional): Threshold value for comparisons. Defaults to 0.8.

    Returns:
        float: The average accuracy score across all comparisons.

    Raises:
        ValueError: If no comparison datasets are provided.

    Example:
        >>> main_result = {...}  # Your reference/main extraction
        >>> variations = [modified_result, alt_result]  # Other extractions
        >>> accuracy = compare_datasets(main_result, variations, "ExtractionProcedure")
        >>> print(f"Average accuracy: {accuracy}")
    """
    if not comparison_datasets:
        raise ValueError("Provide at least one comparison dataset.")

    total_accuracy = 0.0

    # Compare target against each comparison dataset
    for i, comparison_dataset in enumerate(comparison_datasets):
        accuracy_result = compare_two_datasets(
            dataset_1=target_dataset,
            dataset_2=comparison_dataset,
            dataset_1_name=f"{procedure_name}",
            dataset_2_name=f"{procedure_name}",
            fixed_threshold=fixed_threshold,
        )
        comparison_accuracy = accuracy_result["summary"]["overall_match_percentage"]
        total_accuracy += comparison_accuracy

    overall_accuracy = (
        total_accuracy / len(comparison_datasets) if comparison_datasets else 0.0
    )

    return overall_accuracy


def main() -> None:
    try:
        load_dotenv(override=True)
        # Load environment variables
        # Procedure to extract
        DOCUMENT_NAME = os.getenv("DOCUMENT_NAME")
        PROCEDURE_TO_EXTRACT = os.getenv("PROCEDURE_TO_EXTRACT")
        # LLM config
        MAIN_MODEL = os.getenv("MAIN_MODEL", "gemini-2.0-flash-exp")
        MAIN_MODEL_TEMPERATURE = float(os.getenv("MAIN_MODEL_TEMPERATURE", 0.0))
        ALTERNATIVE_MODEL = os.getenv("ALTERNATIVE_MODEL", MAIN_MODEL)
        ALTERNATIVE_MODEL_TEMPERATURE = float(
            os.getenv("ALTERNATIVE_MODEL_TEMPERATURE", 0.0)
        )

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

        prompt_4_modified = prompt_manager.render_prompt(
            template_name="v1-step4-enrich-modified",
            original_content=context,
            result_3=result_3,
            section_name=PROCEDURE_TO_EXTRACT,
        )

        result_4 = main_agent.run_sync(user_prompt=prompt_4, result_type=Graph).data

        result_4_modified = main_agent.run_sync(
            user_prompt=prompt_4_modified, result_type=Graph
        ).data

        result_4_alt = alt_agent.run_sync(user_prompt=prompt_4, result_type=Graph).data

        # Step 4:  Validate procedures
        result_4_dict = result_4.model_dump()
        result_4_modified_dict = result_4_modified.model_dump()
        result_4_alt_dict = result_4_alt.model_dump()

        result_4_accuracy = compare_datasets(
            target_dataset=result_4_dict,
            comparison_datasets=[result_4_modified_dict, result_4_alt_dict],
            procedure_name=PROCEDURE_TO_EXTRACT,
            fixed_threshold=0.8,
        )

        result_4_accuracy_modified = compare_datasets(
            target_dataset=result_4_modified_dict,
            comparison_datasets=[result_4_dict, result_4_alt_dict],
            procedure_name=PROCEDURE_TO_EXTRACT,
            fixed_threshold=0.8,
        )

        result_4_accuracy_alt = compare_datasets(
            target_dataset=result_4_alt_dict,
            comparison_datasets=[result_4_dict, result_4_modified_dict],
            procedure_name=PROCEDURE_TO_EXTRACT,
            fixed_threshold=0.8,
        )

        logger.info(
            f"Main extraction accuracy: {result_4_accuracy:.2f}, Modified extraction accuracy: {result_4_accuracy_modified:.2f}, Alternative extraction accuracy: {result_4_accuracy_alt:.2f}"
        )

        # Pick the best extraction based on accuracy
        best_extraction = None
        best_extraction_accuracy = 0.0

        # If accuracies are equal, prioritize in order: main -> modified -> alt
        if (
            result_4_accuracy >= result_4_accuracy_modified
            and result_4_accuracy >= result_4_accuracy_alt
        ):
            best_extraction = result_4_dict
            best_extraction_accuracy = result_4_accuracy
            best_model = MAIN_MODEL
            extraction_method = "main"
        elif result_4_accuracy_modified >= result_4_accuracy_alt:
            best_extraction = result_4_modified_dict
            best_extraction_accuracy = result_4_accuracy_modified
            best_model = MAIN_MODEL
            extraction_method = "modified"
        else:
            best_extraction = result_4_alt_dict
            best_extraction_accuracy = result_4_accuracy_alt
            best_model = ALTERNATIVE_MODEL
            extraction_method = "alternative model"

        # Log the best extraction result
        logger.info(f"Best result model: {best_model}")
        logger.info(f"Best result extraction method: {extraction_method}")
        logger.info(f"Best result accuracy: {best_extraction_accuracy:.2f}")

        #  Step 5: save to database

        store_graph(
            name=PROCEDURE_TO_EXTRACT,
            document_name=DOCUMENT_NAME,
            graph_data=best_extraction,
            accuracy=best_extraction_accuracy,
            db=db_handler,
        )

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
        sys.exit(1)
