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
from src.schemas.procedure_graph import Graph

# Set up logging
logger = get_logger(__name__)


def prompt_chain(
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
            template_name="v1-step1-modified",
            procedure_name=procedure_name,
            context=context,
            entity=entity,
        )
    else:
        prompt_1 = prompt_manager.render_prompt(
            template_name="v1-step1",
            procedure_name=procedure_name,
            context=context,
            entity=entity,
        )

    result_1_response = agent.run_sync(user_prompt=prompt_1)
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
        template_name="v1-step2-evaluate",
        original_context=context,
        result_1=result_1,
        section_name=procedure_name,
        entity=entity,
    )

    result_2_response = agent.run_sync(
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
        template_name="v1-step3-correct",
        result_1=result_1,
        result_2=result_2,
        section_name=procedure_name,
        entity=entity,
    )

    result_3_response = agent.run_sync(user_prompt=prompt_3)
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
        template_name="v1-step4-enrich",
        original_context=context,
        result_3=result_3,
        section_name=procedure_name,
        entity=entity,
    )

    # Execute final extraction with type validation using Graph schema
    result_4_response = agent.run_sync(user_prompt=prompt_4, output_type=Graph)
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
