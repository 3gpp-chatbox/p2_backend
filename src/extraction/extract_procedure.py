import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

from src.accuracy.compare_datasets import compare_datasets
from src.db.db_handler import DatabaseHandler
from src.db.document import get_document_by_name
from src.extraction.store_graphs import store_graph
from src.prompts.prompt_manager import PromptManager
from src.retrieval.get_context import get_context
from src.schema_validation import Graph

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)


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
        ).output

        # Call agent for prompt_2
        prompt_2 = prompt_manager.render_prompt(
            template_name="v1-step2-evaluate",
            original_content=context,
            result_1=result_1,
            section_name=PROCEDURE_TO_EXTRACT,
        )

        result_2 = main_agent.run_sync(
            user_prompt=prompt_2,
        ).output

        prompt_3 = prompt_manager.render_prompt(
            template_name="v1-step3-correct",
            result_1=result_1,
            result_2=result_2,
            section_name=PROCEDURE_TO_EXTRACT,
        )

        result_3 = main_agent.run_sync(user_prompt=prompt_3).output

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

        result_4 = main_agent.run_sync(user_prompt=prompt_4, output_type=Graph).output

        result_4_modified = main_agent.run_sync(
            user_prompt=prompt_4_modified, output_type=Graph
        ).output

        result_4_alt = alt_agent.run_sync(
            user_prompt=prompt_4, output_type=Graph
        ).output

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
            extraction_method = "alternative"

        # Log all results model/method/accuracy
        logger.info(
            f"Main extraction model: {MAIN_MODEL}, Main extraction accuracy: {result_4_accuracy:.2f}"
        )
        logger.info(
            f"Modified extraction model: {MAIN_MODEL}, Modified extraction accuracy: {result_4_accuracy_modified:.2f}"
        )
        logger.info(
            f"Alternative extraction model: {ALTERNATIVE_MODEL}, Alternative extraction accuracy: {result_4_accuracy_alt:.2f}"
        )

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
