"""Interactive CLI tool for procedure extraction from technical documents.

This module provides a command-line interface for extracting structured procedure
information from technical documents. It implements a multi-stage extraction pipeline
using multiple LLM models for validation and accuracy comparison.

Key Features:
    - Interactive document selection with fuzzy search
    - Multi-model extraction pipeline for accuracy
    - Automated context retrieval and processing
    - Accuracy comparison between different extraction methods
    - Database integration for result storage
    - Support for multiple extraction methods (main, alternative, modified)

Example:
    To run the procedure extraction tool:

    ```bash
    python extract_procedure_cli.py
    ```

    The tool will guide you through:
    1. Entering the procedure name
    2. Specifying the entity (automatically converted to uppercase)
    3. Selecting the target document
    4. Viewing the extraction results

Note:
    Requires appropriate environment variables to be set for model configuration.
    See README.md for setup instructions.
"""

import asyncio
import os
import sys
from datetime import datetime
from typing import List

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from src.accuracy.compare_datasets import compare_datasets
from src.db.db_ahandler import AsyncDatabaseHandler
from src.db.document import get_documents
from src.extraction.prompt_chain import prompt_chain
from src.extraction.store_graphs import store_graph
from src.lib.agents import AgentManager
from src.lib.cli_utils import (
    choose_document,
    get_entity_from_user,
    get_procedure_from_user,
    print_header,
    print_instructions,
    print_results,
)
from src.lib.file_utils import save_result
from src.lib.logger import logger, setup_logger
from src.prompts.prompt_manager import PromptManager
from src.retrieval.get_context import get_context
from src.schemas.extraction_types import (
    ExtractionMethod,
    ExtractionResult,
    ExtractionResults,
)
from src.schemas.models.agent import AgentCollection
from src.schemas.models.document import SQLDocument


async def main() -> None:
    """Execute the main procedure extraction workflow.

    This function orchestrates the entire procedure extraction process:
    1. Loads environment variables and initializes models
    2. Sets up database connection
    3. Gathers user inputs (procedure, entity, document)
    4. Retrieves relevant document context
    5. Executes multi-stage extraction pipeline with different models
    6. Compares and validates extraction results
    7. Stores the best result in the database

    The function supports two extraction approaches:
    - Standard: Uses main model with modified prompt
    - Alternative: Uses three different models for comparison

    Returns:
        None

    Raises:
        ValueError: If required environment variables are missing or invalid,
            no documents are found in the database, or if a graph already exists
            for the given procedure/entity combination.
        Exception: For any other errors during execution, which are logged
            and result in program termination with exit code 1.

    Note:
        Requires appropriate environment variables to be set:
        - MAIN_MODEL
        - ALTERNATIVE_MODEL
        - ALTERNATIVE_MODEL_2 (optional)
        - MODEL_TEMPERATURE
    """
    try:
        setup_logger()
        # Load environment variables from .env file
        load_dotenv(override=True)
        # Generate a unique run ID for this execution
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        # -------------------------- Step 1: Load environment variables --------------------------

        # --- Load .env LLM Configuration ---

        # --- Set fixed values for version, status and commit directly ---
        GRAPH_VERSION = "1"
        EXTRACTION_STATUS = "new"
        COMMIT_TITLE = "Initial extraction"
        COMMIT_MESSAGE = "Auto-generated from LLM"

        # ------- Setup models and Agents -------

        agent_manager = AgentManager()

        MODEL_TYPE = os.getenv("MODEL_TYPE")
        if not MODEL_TYPE or MODEL_TYPE not in ["openai", "gemini"]:
            raise ValueError(
                "MODEL_TYPE environment variable must be set to 'openai' or 'gemini'."
            )

        if MODEL_TYPE == "openai":
            agents: AgentCollection = agent_manager.get_openai_agents()
        elif MODEL_TYPE == "gemini":
            agents: AgentCollection = agent_manager.get_gemini_agents()

        main_agent = agents.main_agent

        alt_agent = agents.alt_agent

        alt_agent_2 = agents.alt_agent_2

        # Initialize SBERT model
        sbert_model = SentenceTransformer("all-MiniLM-L6-v2")

        # Instantiate prompt manager
        prompt_manager = PromptManager()

        # -------------------------- Step 2: Get User Inputs --------------------------
        # Initialize database connection
        async with AsyncDatabaseHandler() as db_handler:
            async with db_handler.get_connection() as conn:
                # Fetch documents from the database
                documents_result: List[SQLDocument] = await get_documents(conn)

                if not documents_result:
                    raise ValueError("No documents found in the database.")

                # Create a dictionary of documents with their spec and version
                doc_choices_dict = {
                    f"{doc.spec} V{doc.version}": doc for doc in documents_result
                }

                # Display the header and instructions
                print_header()
                print_instructions()

                # Prompt user for procedure and entity
                procedure = get_procedure_from_user()
                entity = get_entity_from_user()

                # Prompt user to select a document
                document_key = await choose_document(doc_choices_dict.keys())

                if document_key is None:
                    raise ValueError("No document selected")

                selected_document = doc_choices_dict[document_key]

                print_results(procedure, entity, document_key)

                # Check if the graph already exists in the database for the given document, procedure and entity
                check_graph_existence_query = """
                SELECT g.id
                FROM graph g
                JOIN procedure p ON g.procedure_id = p.id
                WHERE p.document_id = %s AND p.name = %s AND g.entity = %s
                """
                check_params = (selected_document.id, procedure, entity)
                cur = await conn.execute(
                    query=check_graph_existence_query,
                    params=check_params,
                )

                existing_graph = await cur.fetchone()

                if existing_graph:
                    logger.info(
                        f"Graph already exists for '{entity}' side of procedure '{procedure}' "
                    )
                    raise ValueError(
                        f"Graph already exists for '{entity}' side of procedure '{procedure}' "
                    )

                # -------------------------- Step 3: Get contextual data (Document sections) for the extraction --------------------------

                # Retrieve relevant context for the procedure extraction
                document_context = await get_context(
                    doc_id=selected_document.id,
                    procedure_name=procedure,
                    db_conn=conn,
                )

                context = document_context.context
                top_level_sections = document_context.top_level_sections

                # Save the retrieved context
                save_result(
                    result=f"# Context for {procedure}\n\n{context}",
                    step="original_context",  # More descriptive step name
                    procedure_name=procedure,
                    run_id=run_id,
                    method="context",  # Add method for context extraction
                )

            # -------------------------- Step 4: Execute the multi-stage prompting chain for procedure extraction --------------------------
            # The extraction order is important:
            # 1. Main extraction (always runs)
            # 2. Alternative extraction (always runs)
            # 3. Modified or Alternative_2 extraction (configuration dependent)

            # Execute main extraction first (baseline for comparison)
            main_extraction: ExtractionResult = await prompt_chain(
                agent=main_agent,
                prompt_manager=prompt_manager,
                context=context,
                procedure_name=procedure,
                run_id=run_id,
                modified_prompt=False,
                method=ExtractionMethod.MAIN,
                model_name=main_agent.model.model_name,
                entity=entity,
            )

            # Execute alternative model extraction (used in all scenarios)
            alt_extraction: ExtractionResult = await prompt_chain(
                agent=alt_agent,
                prompt_manager=prompt_manager,
                context=context,
                procedure_name=procedure,
                run_id=run_id,
                modified_prompt=False,
                method=ExtractionMethod.ALTERNATIVE,
                model_name=alt_agent.model.model_name,
                entity=entity,
            )

            # Execute either modified extraction or alternative_2 based on configuration
            # When ALTERNATIVE_MODEL_2 is set, it replaces the modified approach entirely
            # and its results are stored as "alternative" in the database
            if alt_agent_2:
                # Use alternative_2 model instead of modified approach
                alt_2_extraction: ExtractionResult = await prompt_chain(
                    agent=alt_agent_2,
                    prompt_manager=prompt_manager,
                    context=context,
                    procedure_name=procedure,
                    run_id=run_id,
                    modified_prompt=False,
                    method=ExtractionMethod.ALTERNATIVE_2,  # Maps to "alternative" in DB
                    model_name=alt_agent_2.model.model_name,
                    entity=entity,
                )

                extraction_results = ExtractionResults(
                    main=main_extraction,
                    alternative=alt_extraction,  # Use modified_extraction as alternative when ALTERNATIVE_MODEL_2 is present
                    alternative_2=alt_2_extraction,  # Store it in alternative_2 slot as well
                )
            else:
                modified_extraction: ExtractionResult = await prompt_chain(
                    agent=main_agent,
                    prompt_manager=prompt_manager,
                    context=context,
                    procedure_name=procedure,
                    run_id=run_id,
                    modified_prompt=True,
                    method=ExtractionMethod.MODIFIED,
                    model_name=main_agent.model.model_name,
                    entity=entity,
                )

                extraction_results = ExtractionResults(
                    main=main_extraction,
                    modified=modified_extraction,
                    alternative=alt_extraction,
                )

            # -------------------------- Step 5: Compare and validate different extraction approaches --------------------------
            # Each extraction is compared against the other two to calculate its accuracy
            # The comparison logic differs based on whether we're using alternative_2 or modified

            # Calculate and update accuracy scores
            if alt_agent_2:
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
                    procedure_name=procedure,
                    model=sbert_model,
                    fixed_threshold=0.8,
                )

                alt_extraction.accuracy = compare_datasets(
                    target_dataset=alt_extraction.graph,
                    comparison_datasets=[
                        main_extraction.graph,
                        alt_2_extraction.graph,
                    ],
                    procedure_name=procedure,
                    model=sbert_model,
                    fixed_threshold=0.8,
                )

                alt_2_extraction.accuracy = compare_datasets(
                    target_dataset=alt_2_extraction.graph,
                    comparison_datasets=[
                        main_extraction.graph,
                        alt_extraction.graph,
                    ],
                    procedure_name=procedure,
                    model=sbert_model,
                    fixed_threshold=0.8,
                )

                # Log accuracy comparison with alternative_2
                logger.info(
                    f"Extraction accuracy comparison - "
                    f"Main ({main_agent.model.model_name}): {main_extraction.accuracy:.2f}, "
                    f"Alternative ({alt_agent.model.model_name}): {alt_extraction.accuracy:.2f}, "
                    f"Alternative_2 ({alt_agent_2.model.model_name}): {alt_2_extraction.accuracy:.2f}, "
                )
            else:
                # Regular comparison with modified approach
                main_extraction.accuracy = compare_datasets(
                    target_dataset=main_extraction.graph,
                    comparison_datasets=[
                        modified_extraction.graph,
                        alt_extraction.graph,
                    ],
                    procedure_name=procedure,
                    model=sbert_model,
                    fixed_threshold=0.8,
                )

                modified_extraction.accuracy = compare_datasets(
                    target_dataset=modified_extraction.graph,
                    comparison_datasets=[
                        main_extraction.graph,
                        alt_extraction.graph,
                    ],
                    procedure_name=procedure,
                    model=sbert_model,
                    fixed_threshold=0.8,
                )

                alt_extraction.accuracy = compare_datasets(
                    target_dataset=alt_extraction.graph,
                    comparison_datasets=[
                        main_extraction.graph,
                        modified_extraction.graph,
                    ],
                    procedure_name=procedure,
                    model=sbert_model,
                    fixed_threshold=0.8,
                )

                # Log accuracy comparison for regular approach
                logger.info(
                    f"Extraction accuracy comparison - "
                    f"Main ({main_agent.model.model_name}): {main_extraction.accuracy:.2f}, "
                    f"Alternative ({alt_agent.model.model_name}): {alt_extraction.accuracy:.2f}, "
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

        # -------------------------- Step 6: Store the best extraction result with its metadata in the database --------------------------

        async with db_handler.get_connection() as conn:
            await store_graph(
                name=procedure,
                document_id=selected_document.id,
                graph_data=best_result.graph,
                accuracy=best_result.accuracy,
                db_conn=conn,
                model=best_result.model_name,
                extraction_method=best_result.method.value,
                entity=entity,
                top_level_sections=top_level_sections,
                commit_title=COMMIT_TITLE,
                commit_message=COMMIT_MESSAGE,
                version=GRAPH_VERSION,
                status=EXTRACTION_STATUS,
            )

    except Exception as e:
        logger.error(
            f"Error in `main`: An error occurred when extracting procedure: {e}.",
            exc_info=True,
        )
        sys.exit(1)


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
