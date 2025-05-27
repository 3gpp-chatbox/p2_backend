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
        # Generate a unique run ID for this execution
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        load_dotenv(override=True)
        setup_logger()
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
                        f"Graph already exists for '{entity}' side of procedure '{procedure}'"
                    )
                    raise ValueError(
                        f"Graph already exists for '{entity}' side of procedure '{procedure}'"
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

        # -------------------------- Step 5: Store the extraction result with its metadata in the database --------------------------

        async with db_handler.get_connection() as conn:
            await store_graph(
                name=procedure,
                document_id=selected_document.id,
                graph_data=main_extraction.graph,
                accuracy=main_extraction.accuracy,
                db_conn=conn,
                model=main_extraction.model_name,
                extraction_method=main_extraction.method.value,
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
