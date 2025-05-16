"""
This module contains the prompt chain function for executing a complete sequence of prompts
for procedure extraction. The function handles multiple stages of extraction, evaluation,
correction and enrichment using different models and prompting strategies.
"""

from pydantic_ai import Agent

from src.lib.file_utils import save_result
from src.lib.logger import get_logger
from src.prompts.prompt_manager import PromptManager
from src.schemas.extraction_types import ExtractionMethod, ExtractionResult
from src.schemas.procedure_graph import BaseGraph, Graph

# Set up logging
logger = get_logger(__name__)


async def prompt_chain(
    agent: Agent,
    prompt_manager: PromptManager,
    context: str,
    procedure_name: str,
    run_id: str,
    modified_prompt: bool,
    method: ExtractionMethod,
    model_name: str,
    entity: str,
) -> ExtractionResult:
    """Execute a complete chain of prompts for procedure extraction.

    This function runs a sequence of four prompts to extract and refine procedural information:
    1. Initial extraction of procedure information
    2. Evaluation and validation of the initial extraction
    3. Application of corrections based on evaluation
    4. Enrichment of the corrected extraction with additional details

    Each step builds upon the results of previous steps, maintaining a coherent extraction chain.
    The function supports different extraction methods (main, modified, alternative) and can
    be used with different models, allowing for flexible extraction strategies.

    Args:
        agent: The LLM agent to execute the prompts
        prompt_manager: Manager for accessing and rendering prompts
        context: The document context containing the procedure information
        procedure_name: Name of the procedure being extracted
        run_id: Unique identifier for the current execution run
        modified_prompt: Whether to use the modified version of prompts (for modified extraction)
        method: Extraction method enum indicating the approach being used
        model_name: Name of the model being used for this extraction
        entity: Name of the entity for which the procedure is being extracted

    Returns:
        ExtractionResult: Contains the final graph, model info, method, and initial accuracy (0.0)
                         Accuracy will be calculated later by comparing against other extractions.

    Note:
        Results from each step are saved to files for analysis and debugging.
        The function maintains dependencies between steps, using results from
        previous steps as input for subsequent steps.
        The method parameter determines both logging and file naming through its value property.
    """
    # Call agent for prompt_1
    if modified_prompt:
        prompt_1 = prompt_manager.render_prompt(
            template_name="v3-step1-modified",
            procedure_name=procedure_name,
            context=context,
            entity=entity,
        )
    else:
        prompt_1 = prompt_manager.render_prompt(
            template_name="v3-step1",
            procedure_name=procedure_name,
            context=context,
            entity=entity,
        )

    result_1_response = await agent.run(
        user_prompt=prompt_1,
        output_type=BaseGraph,
    )

    result_1 = result_1_response.output
    logger.info(f"Step 1 token usage for {method.value}: {result_1_response.usage()}")

    save_result(
        result=result_1,
        step="step1_initial_extraction",
        procedure_name=procedure_name,
        run_id=run_id,
        method=method.value,
    )

    # Stage 2: Evaluate and validate initial extraction
    prompt_2 = prompt_manager.render_prompt(
        template_name="v3-step2-evaluate",
        original_context=context,
        result_1=result_1.model_dump_json(indent=2),  # Format it as JSON
        section_name=procedure_name,
        entity=entity,
    )

    result_2_response = await agent.run(
        user_prompt=prompt_2,
    )

    result_2 = result_2_response.output
    logger.info(f"Step 2 token usage for {method.value}: {result_2_response.usage()}")

    save_result(
        result=result_2,
        step="step2_evaluation",
        procedure_name=procedure_name,
        run_id=run_id,
        method=method.value,
    )

    # Stage 3: Apply corrections based on evaluation
    prompt_3 = prompt_manager.render_prompt(
        template_name="v3-step3-correct",
        result_1=result_1.model_dump_json(indent=2),  # Format it as JSON
        result_2=result_2,
        section_name=procedure_name,
        entity=entity,
    )

    result_3_response = await agent.run(
        user_prompt=prompt_3,
        output_type=BaseGraph,
    )

    result_3 = result_3_response.output
    logger.info(f"Step 3 token usage for {method.value}: {result_3_response.usage()}")

    save_result(
        result=result_3,
        step="step3_corrections",
        procedure_name=procedure_name,
        run_id=run_id,
        method=method.value,
    )

    # Stage 4: Enrich the corrected extraction with additional details
    prompt_4 = prompt_manager.render_prompt(
        template_name="v3-step4-enrich",
        original_context=context,
        result_3=result_3.model_dump_json(indent=2),
        section_name=procedure_name,
        entity=entity,
    )

    # Execute final extraction with type validation using Graph schema
    result_4_response = await agent.run(
        user_prompt=prompt_4,
        output_type=Graph,
    )

    result_4_graph: Graph = result_4_response.output
    logger.info(f"Step 4 token usage for {method.value}: {result_4_response.usage()}")

    save_result(
        result=result_4_graph,
        step="step4_main_enriched",
        procedure_name=procedure_name,
        run_id=run_id,
        method=method.value,
    )

    # Create and return ExtractionResult
    return ExtractionResult(
        graph=result_4_graph,
        accuracy=0.0,  # Will be calculated later when comparing results
        model_name=model_name,
        method=method,
    )


if __name__ == "__main__":
    import asyncio
    import os
    import sys

    from dotenv import load_dotenv
    from pydantic_ai.models.gemini import GeminiModel

    from src.db.db_ahandler import AsyncDatabaseHandler
    from src.db.document import get_document_by_name
    from src.retrieval.get_context import get_context

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    async def main() -> None:
        try:
            # Generate a unique run ID for this execution

            load_dotenv(override=True)
            # Load environment variables with default values where appropriate
            # --- Document Configuration ---
            DOCUMENT_NAME = os.getenv("DOCUMENT_NAME")
            PROCEDURE_TO_EXTRACT = os.getenv("PROCEDURE_TO_EXTRACT")
            ENTITY = os.getenv("ENTITY")
            # --- LLM Configuration ---
            MAIN_MODEL = os.getenv("MAIN_MODEL", "gemini-2.0-flash-exp")
            MAIN_MODEL_TEMPERATURE = float(os.getenv("MAIN_MODEL_TEMPERATURE", 0.0))

            if not PROCEDURE_TO_EXTRACT or not DOCUMENT_NAME or not ENTITY:
                raise ValueError(
                    "PROCEDURE_TO_EXTRACT, DOCUMENT_NAME and ENTITY must be set in the environment variables."
                )

            logger.info(f"Using Model: {MAIN_MODEL}")

            main_model = GeminiModel(
                model_name=MAIN_MODEL, provider="google-gla"
            )  # Primary model for main extraction pipeline

            # Initialize primary agent with main model
            main_agent: Agent = Agent(
                model=main_model,
                model_settings={"temperature": MAIN_MODEL_TEMPERATURE},
            )

            # Initialize database connection
            async with AsyncDatabaseHandler() as db_handler:
                async with db_handler.get_connection() as conn:
                    # Instantiate prompt manager
                    prompt_manager = PromptManager()

                    # Step 1: Retrieve the target document from database
                    document = await get_document_by_name(
                        doc_name=DOCUMENT_NAME,
                        db_conn=conn,
                    )

                    if not document:
                        logger.error(
                            f"Document '{DOCUMENT_NAME}' not found in the database."
                        )
                        raise ValueError(
                            f"Document '{DOCUMENT_NAME}' not found in the database."
                        )

                    context = await get_context(
                        doc_name=DOCUMENT_NAME,
                        procedure_name=PROCEDURE_TO_EXTRACT,
                        db_conn=conn,
                    )

                    save_result(
                        result=f"# Context for {PROCEDURE_TO_EXTRACT}\n\n{context}",
                        step="original_context",
                        procedure_name=PROCEDURE_TO_EXTRACT,
                        run_id="test_run",
                        method="context",
                    )

                    _main_extraction: ExtractionResult = await prompt_chain(
                        agent=main_agent,
                        prompt_manager=prompt_manager,
                        context=context,
                        procedure_name=PROCEDURE_TO_EXTRACT,
                        run_id="test_run",
                        modified_prompt=True,
                        method=ExtractionMethod.MAIN,
                        model_name=MAIN_MODEL,
                        entity=ENTITY,
                    )

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise

    asyncio.run(main())
