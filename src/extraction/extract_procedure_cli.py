#!/usr/bin/env python3
"""
POC for an interactive CLI tool to extract procedures.

This script demonstrates a simple CLI flow that:
1. Prompts the user for the procedure to extract.
2. Prompts the user for the entity (converted to uppercase).
3. Displays an interactive, searchable selection for available documents.
4. Prints out the entered details.

This POC does not connect to any database and uses a static list of documents.
"""

import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import List

from InquirerPy import inquirer
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from sentence_transformers import SentenceTransformer

from src.accuracy.compare_datasets import compare_datasets
from src.db.db_ahandler import AsyncDatabaseHandler
from src.db.document import get_documents
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
from src.schemas.models.document import SQLDocument

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

# Set up logging
logger = get_logger(__name__)

# Initialize Rich console
console = Console()


def print_header() -> None:
    """Display a styled header for the application."""
    header = Text("Procedure Extraction", style="bold gold3")
    centered_header = Align.center(header)
    console.print(Panel(centered_header, border_style="gold3"))


def print_instructions() -> None:
    """Display styled instructions for document selection."""
    instructions = Text()
    instructions.append("\nDocument Selection Instructions:\n\n")
    instructions.append("• Use ", style="white")
    instructions.append("↑↓ arrows", style="gold3")
    instructions.append(" to navigate\n", style="white")
    instructions.append("• Start ", style="white")
    instructions.append("typing", style="gold3")
    instructions.append(" to filter the document list\n", style="white")
    instructions.append("• Press ", style="white")
    instructions.append("Enter", style="gold3")
    instructions.append(" to select\n", style="white")

    console.print(instructions)
    console.print()


def get_procedure_from_user() -> str:
    """Prompt the user to input the procedure to extract.

    Returns:
        str: The procedure entered by the user.
    """
    console.print("[bold gold3]Procedure Input[/]")
    procedure = input(
        "Enter the procedure to extract (e.g., 'Initial Registration'): "
    ).strip()
    console.print()
    return procedure


def get_entity_from_user() -> str:
    """Prompt the user to input the entity.

    Returns:
        str: The entity entered by the user, converted to uppercase.
    """
    console.print("[bold gold3]Entity Input[/]")
    entity = input("Enter the entity (e.g., 'UE'): ").strip().upper()
    console.print()
    return entity


async def choose_document(documents: List[str]) -> str:
    """Interactively display a searchable list of documents and allow the user to select one.

    By default, displays all available documents. Users can:
    - Navigate through choices with arrow keys
    - Type to filter/search through documents
    - Press Enter to select the highlighted document

    Args:
        documents (List[str]): A list containing document names.

    Returns:
        str: The document name selected by the user.
    """
    console.print("[bold gold3]Document Selection[/]")
    result = await inquirer.fuzzy(
        message="Select a document:",
        choices=documents,
        instruction="(Use ↑↓ arrows to navigate, type to filter, Enter to select)",
        mandatory=True,
        validate=lambda x: x in documents,
        invalid_message="Please select a valid document",
        border=True,
        cycle=True,
    ).execute_async()
    console.print()
    return result


def print_results(procedure: str, entity: str, document: str) -> None:
    """Display the final results in a styled panel.

    Args:
        procedure: The selected procedure
        entity: The selected entity
        document: The selected document
    """
    results = Text.assemble(
        ("Selected Details\n\n", "bold gold3"),
        ("Procedure: ", "bold gold3"),
        (f"{procedure}\n", "white"),
        ("Entity: ", "bold gold3"),
        (f"{entity}\n", "white"),
        ("Document: ", "bold gold3"),
        (f"{document}\n", "white"),
    )
    console.print(Panel(results, border_style="gold3"))


async def main() -> None:
    try:
        # Generate a unique run ID for this execution
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        # -------------------------- Step 1: Load environment variables --------------------------

        # --- Load .env LLM Configuration ---
        MAIN_MODEL = os.getenv("MAIN_MODEL")
        ALTERNATIVE_MODEL = os.getenv("ALTERNATIVE_MODEL")
        ALTERNATIVE_MODEL_2 = os.getenv("ALTERNATIVE_MODEL_2", None)

        MODEL_TEMPERATURE = float(os.getenv("MODEL_TEMPERATURE", 0.0))

        if not MAIN_MODEL or not ALTERNATIVE_MODEL:
            raise ValueError(
                "MAIN_MODEL and ALTERNATIVE_MODEL must be set in the environment variables."
            )

        if MAIN_MODEL == ALTERNATIVE_MODEL:
            raise ValueError("MAIN_MODEL and ALTERNATIVE_MODEL must be different.")

        # --- Set fixed values for version, status and commit directly ---
        GRAPH_VERSION = "1"
        EXTRACTION_STATUS = "new"
        COMMIT_TITLE = "Initial extraction"
        COMMIT_MESSAGE = "Auto-generated from LLM"

        # ------- Setup models and Agents -------

        # Initialize SBERT model
        sbert_model = SentenceTransformer("all-MiniLM-L6-v2")

        main_model = GeminiModel(
            model_name=MAIN_MODEL, provider="google-gla"
        )  # Primary model for main extraction pipeline

        # Initialize primary agent with main model
        main_agent: Agent = Agent(
            model=main_model,
            model_settings={"temperature": MODEL_TEMPERATURE},
        )

        alt_model = GeminiModel(
            model_name=ALTERNATIVE_MODEL, provider="google-gla"
        )  # Secondary model for validation

        # Initialize secondary agent with alternative model for validation
        alt_agent: Agent = Agent(
            model=alt_model,
            model_settings={"temperature": MODEL_TEMPERATURE},
        )

        # Initialize alternative model 2 if specified
        if ALTERNATIVE_MODEL_2:
            alt_model_2 = GeminiModel(
                model_name=ALTERNATIVE_MODEL_2, provider="google-gla"
            )

            alt_agent_2: Agent = Agent(
                model=alt_model_2,
                model_settings={"temperature": MODEL_TEMPERATURE},
            )

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

                console.print()
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
                model_name=MAIN_MODEL,
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
                model_name=ALTERNATIVE_MODEL,
                entity=entity,
            )

            # Execute either modified extraction or alternative_2 based on configuration
            # When ALTERNATIVE_MODEL_2 is set, it replaces the modified approach entirely
            # and its results are stored as "alternative" in the database
            if ALTERNATIVE_MODEL_2:
                # Use alternative_2 model instead of modified approach
                alt_2_extraction: ExtractionResult = await prompt_chain(
                    agent=alt_agent_2,
                    prompt_manager=prompt_manager,
                    context=context,
                    procedure_name=procedure,
                    run_id=run_id,
                    modified_prompt=False,
                    method=ExtractionMethod.ALTERNATIVE_2,  # Maps to "alternative" in DB
                    model_name=ALTERNATIVE_MODEL_2,
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
                    model_name=MAIN_MODEL,
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
                    f"Main ({MAIN_MODEL}): {main_extraction.accuracy:.2f}, "
                    f"Alternative ({ALTERNATIVE_MODEL}): {alt_extraction.accuracy:.2f} "
                    f"Alternative_2 ({ALTERNATIVE_MODEL_2}): {alt_2_extraction.accuracy:.2f}, "
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
                    f"Main ({MAIN_MODEL}): {main_extraction.accuracy:.2f}, "
                    f"Alternative ({ALTERNATIVE_MODEL}): {alt_extraction.accuracy:.2f}, "
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
