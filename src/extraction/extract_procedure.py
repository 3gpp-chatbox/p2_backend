"""
This module handles the extraction of procedural information from documents using LLMs.

It implements a multi-step extraction process:
1. Document retrieval from database
2. Context gathering for the target procedure
3. Multi-stage LLM prompting with different models and temperatures
4. Accuracy validation of extracted procedures
5. Storage of the best extraction result

The module uses multiple LLM models and prompting strategies to ensure high-quality
extraction results, comparing different approaches and selecting the most accurate one.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from sentence_transformers import SentenceTransformer

from src.accuracy.compare_datasets import compare_datasets
from src.db.db_handler import DatabaseHandler
from src.db.document import get_document_by_name
from src.extraction.store_graphs import store_graph
from src.prompts.prompt_manager import PromptManager
from src.retrieval.get_context import get_context
from src.schemas.procedure_graph import Graph

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)


def main() -> None:
    """
    Execute the main procedure extraction pipeline.

    This function orchestrates the entire extraction process:
    1. Loads environment variables and configurations
    2. Sets up LLM models with different parameters
    3. Retrieves document and context
    4. Runs multi-stage prompting chain
    5. Validates and compares different extraction results
    6. Stores the best extraction in the database

    The function uses multiple approaches for extraction:
    - Main extraction with primary model
    - Modified extraction with primary model
    - Alternative extraction with secondary model

    Raises:
        ValueError: If required environment variables are missing or if document is not found
        Exception: For any other unexpected errors during execution
    """
    try:
        load_dotenv(override=True)
        # Load environment variables with default values where appropriate
        # --- Document Configuration ---
        DOCUMENT_NAME = os.getenv("DOCUMENT_NAME")
        PROCEDURE_TO_EXTRACT = os.getenv("PROCEDURE_TO_EXTRACT")
        # --- LLM Configuration ---
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

        # Initialize SBERT model once at module level for reuse across comparisons
        sbert_model = SentenceTransformer("all-MiniLM-L6-v2")

        # Initialize LLM models with specified configurations
        main_model = GeminiModel(
            model_name=MAIN_MODEL, provider="google-gla"
        )  # Primary model for main extraction pipeline

        alt_model = GeminiModel(
            model_name=ALTERNATIVE_MODEL, provider="google-gla"
        )  # Secondary model for validation

        # Initialize database connection
        db_handler = DatabaseHandler()

        # Instantiate prompt manager
        prompt_manager = PromptManager()

        # Initialize primary agent with main model
        main_agent: Agent = Agent(
            model=main_model,
            model_settings={"temperature": MAIN_MODEL_TEMPERATURE},
        )

        # Initialize secondary agent with alternative model for validation
        alt_agent: Agent = Agent(
            model=alt_model,
            model_settings={"temperature": ALTERNATIVE_MODEL_TEMPERATURE},
        )

        # Step 1: Retrieve the target document from database
        document = get_document_by_name(doc_name=DOCUMENT_NAME, db_handler=db_handler)

        if not document:
            logger.error(f"Document '{DOCUMENT_NAME}' not found in the database.")
            raise ValueError(f"Document '{DOCUMENT_NAME}' not found in the database.")

        # Check if the graph already exists in the database for the given document
        check_query = """
        SELECT id FROM graph 
        WHERE document_id = %s AND name = %s
        """
        check_params = (document["id"], PROCEDURE_TO_EXTRACT)
        existing_graph = db_handler.execute_query(check_query, check_params)

        if existing_graph:
            logger.warning(
                f"Graph '{PROCEDURE_TO_EXTRACT}' already exists for document '{DOCUMENT_NAME}'"
            )
            raise ValueError(
                f"Graph '{PROCEDURE_TO_EXTRACT}' already exists for document '{DOCUMENT_NAME}'"
            )

        # Step 2: Retrieve relevant context for the procedure extraction
        context = get_context(
            doc_name=DOCUMENT_NAME,
            procedure_name=PROCEDURE_TO_EXTRACT,
            db_handler=db_handler,
        )

        # Step 3: Execute multi-stage prompting chain for procedure extraction
        # Stage 1: Initial extraction of procedure information

        # Call agent for prompt_1
        prompt_1 = prompt_manager.render_prompt(
            template_name="v1-step1", section_name=PROCEDURE_TO_EXTRACT, text=context
        )

        result_1 = main_agent.run_sync(
            user_prompt=prompt_1,
        ).output

        # Stage 2: Evaluate and validate initial extraction
        prompt_2 = prompt_manager.render_prompt(
            template_name="v1-step2-evaluate",
            original_content=context,
            result_1=result_1,
            section_name=PROCEDURE_TO_EXTRACT,
        )

        result_2 = main_agent.run_sync(
            user_prompt=prompt_2,
        ).output

        # Stage 3: Apply corrections based on evaluation
        prompt_3 = prompt_manager.render_prompt(
            template_name="v1-step3-correct",
            result_1=result_1,
            result_2=result_2,
            section_name=PROCEDURE_TO_EXTRACT,
        )

        result_3 = main_agent.run_sync(user_prompt=prompt_3).output

        # Stage 4: Enrich the corrected extraction with additional details
        # Try multiple approaches for better accuracy
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

        # Execute final extraction with type validation using Graph schema
        result_4: Graph = main_agent.run_sync(
            user_prompt=prompt_4, output_type=Graph
        ).output

        # Execute modified approach for comparison
        result_4_modified: Graph = main_agent.run_sync(
            user_prompt=prompt_4_modified, output_type=Graph
        ).output

        # Execute alternative model extraction for validation
        result_4_alt: Graph = alt_agent.run_sync(
            user_prompt=prompt_4, output_type=Graph
        ).output

        # Step 4: Compare and validate different extraction approaches

        # Calculate accuracy scores by comparing each extraction against the others
        result_4_accuracy: float = compare_datasets(
            target_dataset=result_4,
            comparison_datasets=[result_4_modified, result_4_alt],
            procedure_name=PROCEDURE_TO_EXTRACT,
            model=sbert_model,
            fixed_threshold=0.8,
        )

        result_4_accuracy_modified: float = compare_datasets(
            target_dataset=result_4_modified,
            comparison_datasets=[result_4, result_4_alt],
            procedure_name=PROCEDURE_TO_EXTRACT,
            model=sbert_model,
            fixed_threshold=0.8,
        )

        result_4_accuracy_alt: float = compare_datasets(
            target_dataset=result_4_alt,
            comparison_datasets=[result_4, result_4_modified],
            procedure_name=PROCEDURE_TO_EXTRACT,
            model=sbert_model,
            fixed_threshold=0.8,
        )

        # Log combined accuracy and model information
        logger.info(
            f"Extraction accuracy comparison - "
            f"Main ({MAIN_MODEL}): {result_4_accuracy:.2f}, "
            f"Modified ({MAIN_MODEL}): {result_4_accuracy_modified:.2f}, "
            f"Alternative ({ALTERNATIVE_MODEL}): {result_4_accuracy_alt:.2f}"
        )

        # Select the best extraction based on accuracy scores and extraction method
        # Priority order: main -> modified -> alternative when accuracies are equal
        best_extraction: dict | None = None
        best_extraction_accuracy: float = 0.0
        best_model: str
        extraction_method: str

        # If accuracies are equal, prioritize in order: main -> modified -> alt
        if (
            result_4_accuracy >= result_4_accuracy_modified
            and result_4_accuracy >= result_4_accuracy_alt
        ):
            best_extraction = result_4
            best_extraction_accuracy = result_4_accuracy
            best_model = MAIN_MODEL
            extraction_method = "main"
        elif result_4_accuracy_modified >= result_4_accuracy_alt:
            best_extraction = result_4_modified
            best_extraction_accuracy = result_4_accuracy_modified
            best_model = MAIN_MODEL
            extraction_method = "modified"
        else:
            best_extraction = result_4_alt
            best_extraction_accuracy = result_4_accuracy_alt
            best_model = ALTERNATIVE_MODEL
            extraction_method = "alternative"

        # Log the best extraction result
        logger.info(f"Best result model: {best_model}")
        logger.info(f"Best result extraction method: {extraction_method}")
        logger.info(f"Best result accuracy: {best_extraction_accuracy:.2f}")

        # Step 5: Store the best extraction result with its metadata in the database

        store_graph(
            name=PROCEDURE_TO_EXTRACT,
            document_name=DOCUMENT_NAME,
            graph_data=best_extraction,
            accuracy=best_extraction_accuracy,
            db=db_handler,
            model=best_model,
            extraction_method=extraction_method,
        )

    except Exception as e:
        logger.error(
            f"Error in `main`: An error occurred when extracting procedure: {e}.",
            exc_info=True,
        )
        raise ValueError(f"Error in procedure extraction pipeline: {e}")


if __name__ == "__main__":
    try:
        main()

    except Exception:
        sys.exit(1)
