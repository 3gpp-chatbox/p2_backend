"""
This module handles the extraction of procedural information from documents using LLMs.

It implements a multi-step extraction process:
1. Document retrieval from database
2. Context gathering for the target procedure
3. Multi-stage LLM prompting with different models and temperatures
4. Accuracy validation of extracted procedures
5. Storage of the best extraction result

The module supports three main extraction methods:
- Main: Primary extraction using the main model
- Modified: Alternative approach using modified prompts with the main model
- Alternative: Secondary extraction using an alternative model

Additionally, when ALTERNATIVE_MODEL_2 is configured:
- Instead of the modified approach, it uses ALTERNATIVE_MODEL_2 for extraction
- Results are stored with method "alternative" for database compatibility
- The modified prompt path is not used in this case

The module uses multiple LLM models and prompting strategies to ensure high-quality
extraction results, comparing different approaches and selecting the most accurate one.
Each extraction result is evaluated against others to calculate accuracy scores,
with the best result being selected based on both accuracy and method priority.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from sentence_transformers import SentenceTransformer

from src.accuracy.compare_datasets import compare_datasets
from src.db.db_handler import DatabaseHandler
from src.db.document import get_document_by_name
from src.extraction.prompt_chain import prompt_chain
from src.extraction.store_graphs import store_graph
from src.lib.file_utils import save_result
from src.prompts.prompt_manager import PromptManager
from src.retrieval.get_context import get_context
from src.schemas.extraction_types import (
    ExtractionMethod,
    ExtractionResult,
    ExtractionResults,
)

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
    4. Runs multi-stage prompting chain with multiple extraction methods
    5. Validates and compares different extraction results
    6. Stores the best extraction in the database

    Extraction Methods:
    - Main: Uses the main model with standard prompts
    - Alternative: Uses a different model for validation
    - Configuration dependent:
        * If ALTERNATIVE_MODEL_2 is set:
          - Uses this model instead of the modified approach
          - Results are stored as "alternative" in the database
        * If ALTERNATIVE_MODEL_2 is not set:
          - Uses main model with modified prompts
          - Results are stored as "modified" in the database

    The function compares all extraction results to select the best one:
    1. Calculates accuracy scores by comparing each extraction against the others
    2. Uses ExtractionResults container to select best result based on:
       - Accuracy scores
       - Method priority (main > modified > alternative)
    3. Stores the winning extraction in the database with appropriate metadata

    Raises:
        ValueError: If required environment variables are missing or if document is not found
        Exception: For any other unexpected errors during execution
    """
    try:
        # Generate a unique run ID for this execution
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        load_dotenv(override=True)
        # Load environment variables with default values where appropriate
        # --- Document Configuration ---
        DOCUMENT_NAME = os.getenv("DOCUMENT_NAME")
        PROCEDURE_TO_EXTRACT = os.getenv("PROCEDURE_TO_EXTRACT")
        ENTITY = os.getenv("ENTITY")
        # --- LLM Configuration ---
        MAIN_MODEL = os.getenv("MAIN_MODEL", "gemini-2.0-flash-exp")
        MAIN_MODEL_TEMPERATURE = float(os.getenv("MAIN_MODEL_TEMPERATURE", 0.0))
        ALTERNATIVE_MODEL = os.getenv("ALTERNATIVE_MODEL", MAIN_MODEL)
        ALTERNATIVE_MODEL_TEMPERATURE = float(
            os.getenv("ALTERNATIVE_MODEL_TEMPERATURE", 0.0)
        )
        ALTERNATIVE_MODEL_2 = os.getenv("ALTERNATIVE_MODEL_2", None)
        ALTERNATIVE_MODEL_2_TEMPERATURE = float(
            os.getenv("ALTERNATIVE_MODEL_2_TEMPERATURE", 0.0)
        )

        if not PROCEDURE_TO_EXTRACT or not DOCUMENT_NAME or not ENTITY:
            raise ValueError(
                "PROCEDURE_TO_EXTRACT, DOCUMENT_NAME and ENTITY must be set in the environment variables."
            )

        # Initialize SBERT model once at module level for reuse across comparisons
        sbert_model = SentenceTransformer("all-MiniLM-L6-v2")

        main_model = GeminiModel(
            model_name=MAIN_MODEL, provider="google-gla"
        )  # Primary model for main extraction pipeline

        # Initialize primary agent with main model
        main_agent: Agent = Agent(
            model=main_model,
            model_settings={"temperature": MAIN_MODEL_TEMPERATURE},
        )

        alt_model = GeminiModel(
            model_name=ALTERNATIVE_MODEL, provider="google-gla"
        )  # Secondary model for validation

        # Initialize secondary agent with alternative model for validation
        alt_agent: Agent = Agent(
            model=alt_model,
            model_settings={"temperature": ALTERNATIVE_MODEL_TEMPERATURE},
        )

        # Initialize alternative model 2 if specified
        if ALTERNATIVE_MODEL_2:
            alt_model_2 = GeminiModel(
                model_name=ALTERNATIVE_MODEL_2, provider="google-gla"
            )

            alt_agent_2: Agent = Agent(
                model=alt_model_2,
                model_settings={"temperature": ALTERNATIVE_MODEL_2_TEMPERATURE},
            )

        # Instantiate prompt manager
        prompt_manager = PromptManager()

        # Initialize database connection
        with DatabaseHandler() as db_handler:
            # Step 1: Retrieve the target document from database
            document = get_document_by_name(
                doc_name=DOCUMENT_NAME, db_handler=db_handler
            )

            if not document:
                logger.error(f"Document '{DOCUMENT_NAME}' not found in the database.")
                raise ValueError(
                    f"Document '{DOCUMENT_NAME}' not found in the database."
                )

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

        # Save the retrieved context
        save_result(
            result=f"# Context for {PROCEDURE_TO_EXTRACT}\n\n{context}",
            step="original_context",  # More descriptive step name
            procedure_name=PROCEDURE_TO_EXTRACT,
            run_id=run_id,
            method="context",  # Add method for context extraction
        )

        # Step 3: Execute the multi-stage prompting chain for procedure extraction
        # The extraction order is important:
        # 1. Main extraction (always runs)
        # 2. Alternative extraction (always runs)
        # 3. Modified or Alternative_2 extraction (configuration dependent)

        # Execute main extraction first (baseline for comparison)
        main_extraction: ExtractionResult = prompt_chain(
            agent=main_agent,
            prompt_manager=prompt_manager,
            context=context,
            procedure_name=PROCEDURE_TO_EXTRACT,
            run_id=run_id,
            modified_prompt=False,
            method=ExtractionMethod.MAIN,
            model_name=MAIN_MODEL,
            entity=ENTITY,
        )

        # Execute alternative model extraction (used in all scenarios)
        alt_extraction: ExtractionResult = prompt_chain(
            agent=alt_agent,
            prompt_manager=prompt_manager,
            context=context,
            procedure_name=PROCEDURE_TO_EXTRACT,
            run_id=run_id,
            modified_prompt=False,
            method=ExtractionMethod.ALTERNATIVE,
            model_name=ALTERNATIVE_MODEL,
            entity=ENTITY,
        )

        # Execute either modified extraction or alternative_2 based on configuration
        # When ALTERNATIVE_MODEL_2 is set, it replaces the modified approach entirely
        # and its results are stored as "alternative" in the database
        if ALTERNATIVE_MODEL_2:
            # Use alternative_2 model instead of modified approach
            alt_2_extraction: ExtractionResult = prompt_chain(
                agent=alt_agent_2,
                prompt_manager=prompt_manager,
                context=context,
                procedure_name=PROCEDURE_TO_EXTRACT,
                run_id=run_id,
                modified_prompt=False,
                method=ExtractionMethod.ALTERNATIVE_2,  # Maps to "alternative" in DB
                model_name=ALTERNATIVE_MODEL_2,
                entity=ENTITY,
            )
            extraction_results = ExtractionResults(
                main=main_extraction,
                alternative=alt_extraction,  # Use modified_extraction as alternative when ALTERNATIVE_MODEL_2 is present
                alternative_2=alt_2_extraction,  # Store it in alternative_2 slot as well
            )
        else:
            modified_extraction: ExtractionResult = prompt_chain(
                agent=main_agent,
                prompt_manager=prompt_manager,
                context=context,
                procedure_name=PROCEDURE_TO_EXTRACT,
                run_id=run_id,
                modified_prompt=True,
                method=ExtractionMethod.MODIFIED,
                model_name=MAIN_MODEL,
                entity=ENTITY,
            )
            extraction_results = ExtractionResults(
                main=main_extraction,
                modified=modified_extraction,
                alternative=alt_extraction,
            )

        # Step 4: Compare and validate different extraction approaches
        # Each extraction is compared against the other two to calculate its accuracy
        # The comparison logic differs based on whether we're using alternative_2 or modified

        # Calculate and update accuracy scores
        if ALTERNATIVE_MODEL_2:
            # When using alternative_2:
            # - modified_extraction contains the alternative_2 results
            # - Stored as "alternative" in DB for compatibility
            # - Compared against main and alternative extractions
            main_extraction.accuracy = compare_datasets(
                target_dataset=main_extraction.graph,
                comparison_datasets=[
                    alt_2_extraction.graph,
                    alt_extraction.graph,
                ],  # modified_extraction is from alt_2
                procedure_name=PROCEDURE_TO_EXTRACT,
                model=sbert_model,
                fixed_threshold=0.8,
            )

            alt_extraction.accuracy = compare_datasets(
                target_dataset=alt_extraction.graph,
                comparison_datasets=[main_extraction.graph, alt_2_extraction.graph],
                procedure_name=PROCEDURE_TO_EXTRACT,
                model=sbert_model,
                fixed_threshold=0.8,
            )

            alt_2_extraction.accuracy = compare_datasets(
                target_dataset=alt_2_extraction.graph,
                comparison_datasets=[main_extraction.graph, alt_extraction.graph],
                procedure_name=PROCEDURE_TO_EXTRACT,
                model=sbert_model,
                fixed_threshold=0.8,
            )

            # Log accuracy comparison with alternative_2
            logger.info(
                f"Extraction accuracy comparison - "
                f"Main ({MAIN_MODEL}): {main_extraction.accuracy:.2f}, "
                f"Alternative ({ALTERNATIVE_MODEL}): {alt_extraction.accuracy:.2f}"
                f"Alternative_2 ({ALTERNATIVE_MODEL_2}): {alt_2_extraction.accuracy:.2f}, "
            )
        else:
            # Regular comparison with modified approach
            main_extraction.accuracy = compare_datasets(
                target_dataset=main_extraction.graph,
                comparison_datasets=[modified_extraction.graph, alt_extraction.graph],
                procedure_name=PROCEDURE_TO_EXTRACT,
                model=sbert_model,
                fixed_threshold=0.8,
            )

            modified_extraction.accuracy = compare_datasets(
                target_dataset=modified_extraction.graph,
                comparison_datasets=[main_extraction.graph, alt_extraction.graph],
                procedure_name=PROCEDURE_TO_EXTRACT,
                model=sbert_model,
                fixed_threshold=0.8,
            )

            alt_extraction.accuracy = compare_datasets(
                target_dataset=alt_extraction.graph,
                comparison_datasets=[main_extraction.graph, modified_extraction.graph],
                procedure_name=PROCEDURE_TO_EXTRACT,
                model=sbert_model,
                fixed_threshold=0.8,
            )

            # Log accuracy comparison for regular approach
            logger.info(
                f"Extraction accuracy comparison - "
                f"Main ({MAIN_MODEL}): {main_extraction.accuracy:.2f}, "
                f"Alternative ({ALTERNATIVE_MODEL}): {alt_extraction.accuracy:.2f}"
                f"Modified ({modified_extraction.model_name}): {modified_extraction.accuracy:.2f}, "
            )

            # Get the best result using the ExtractionResults container
            # Selection is based on both accuracy scores and method priority:
            # Priority: main > modified > alternative (when accuracies are equal)
        best_result = extraction_results.get_best_result()

        # Log the best extraction result
        logger.info(f"Best result model: {best_result.model_name}")
        logger.info(f"Best result extraction method: {best_result.method.value}")
        logger.info(f"Best result accuracy: {best_result.accuracy:.2f}")

        # Step 5: Store the best extraction result with its metadata in the database
        with DatabaseHandler() as db_handler:
            store_graph(
                name=PROCEDURE_TO_EXTRACT,
                document_name=DOCUMENT_NAME,
                graph_data=best_result.graph,
                accuracy=best_result.accuracy,
                db=db_handler,
                model=best_result.model_name,
                extraction_method=best_result.method.value,
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
