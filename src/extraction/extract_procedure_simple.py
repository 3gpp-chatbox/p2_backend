"""
Simplified version of procedure extraction without accuracy checking.
Uses single model extraction and direct storage.
"""

import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

from src.db.db_ahandler import AsyncDatabaseHandler
from src.db.document import get_document_by_name
from src.extraction.prompt_chain import prompt_chain
from src.extraction.store_graphs import store_graph
from src.lib.file_utils import save_result
from src.prompts.prompt_manager import PromptManager
from src.retrieval.get_context import get_context
from src.schemas.extraction_types import ExtractionMethod, ExtractionResult

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

logger = get_logger(__name__)

async def main() -> None:
    try:
        # Generate run_id
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Load environment variables
        load_dotenv(override=True)
        
        # Basic required configurations
        DOCUMENT_NAME = os.getenv("DOCUMENT_NAME")
        PROCEDURE_TO_EXTRACT = os.getenv("PROCEDURE_TO_EXTRACT")
        ENTITY = os.getenv("ENTITY")
        MAIN_MODEL = os.getenv("MAIN_MODEL")
        MODEL_TEMPERATURE = float(os.getenv("MODEL_TEMPERATURE", 0.0))

        # Validate required variables
        if not all([DOCUMENT_NAME, PROCEDURE_TO_EXTRACT, ENTITY, MAIN_MODEL]):
            raise ValueError("Required environment variables missing")

        ENTITY = ENTITY.upper()  # Ensure ENTITY is uppercase

        # Initialize main model
        main_model = GeminiModel(model_name=MAIN_MODEL, provider="google-gla")
        main_agent = Agent(
            model=main_model,
            model_settings={"temperature": MODEL_TEMPERATURE},
        )

        # --- Set fixed values for version, status and commit directly ---
        GRAPH_VERSION = "1"
        EXTRACTION_STATUS = "new"
        COMMIT_TITLE = "Initial extraction"
        COMMIT_MESSAGE = "Auto-generated from LLM"
        ACCURACY=0.0

        # Initialize prompt manager
        prompt_manager = PromptManager()

        # Database operations
        async with AsyncDatabaseHandler() as db_handler:
            async with db_handler.get_connection() as conn:
                # Get document and context
                document = await get_document_by_name(
                    doc_name=DOCUMENT_NAME,
                    db_conn=conn,
                )

                if not document:
                    raise ValueError(f"Document '{DOCUMENT_NAME}' not found")

                # Check for existing graph
                check_query = """
                SELECT g.id 
                FROM graph g
                JOIN procedure p ON g.procedure_id = p.id
                WHERE p.document_id = %s AND p.name = %s AND g.entity = %s
                """
                check_params = (document["id"], PROCEDURE_TO_EXTRACT, ENTITY)
                cur = await conn.execute(query=check_query, params=check_params)
                existing_graph = await cur.fetchone()

                if existing_graph:
                    raise ValueError(
                        f"Graph already exists for '{ENTITY}' side of procedure '{PROCEDURE_TO_EXTRACT}'"
                    )

                # Get context
                document_context = await get_context(
                    doc_name=DOCUMENT_NAME,
                    procedure_name=PROCEDURE_TO_EXTRACT,
                    db_conn=conn,
                )

                context = document_context.context
                top_level_sections = document_context.top_level_sections

                # Save context
                save_result(
                    result=f"# Context for {PROCEDURE_TO_EXTRACT}\n\n{context}",
                    step="original_context",
                    procedure_name=PROCEDURE_TO_EXTRACT,
                    run_id=run_id,
                    method="context",
                )

                # Single extraction
                extraction_result = await prompt_chain(
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

                # Store result 
                graph_id = await store_graph(
                    name=PROCEDURE_TO_EXTRACT,
                    document_name=DOCUMENT_NAME,
                    graph_data=extraction_result.graph,
                    accuracy=ACCURACY,  # Default accuracy value instead of None
                    model=MAIN_MODEL,
                    extraction_method=ExtractionMethod.MAIN.value,
                    entity=ENTITY,
                    top_level_sections=top_level_sections,
                    commit_title=COMMIT_TITLE,
                    commit_message=COMMIT_MESSAGE,
                    version=GRAPH_VERSION,
                    status=EXTRACTION_STATUS,
                    db_conn=conn,
                )

                logger.info(f"Successfully stored graph with ID: {graph_id}")

    except Exception as e:
        logger.error(f"Error in extraction: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())