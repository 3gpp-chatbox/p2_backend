"""
This module provides utility functions for file operations.
"""

from datetime import datetime
from pathlib import Path
from typing import Union

from pydantic import BaseModel

from src.lib.logger import logger
from src.schemas.procedure_graph import Graph


def save_result(
    result: Union[str, dict, Graph],
    step: str,
    procedure_name: str,
    run_id: str,
    method: str,
) -> None:
    """Save the extraction result to a file.

    Args:
        result: The result to save (can be string, dict or Graph)
        step: The step name (e.g., 'step1', 'step2')
        procedure_name: Name of the procedure being extracted
        run_id: Unique identifier for the current execution run
        method: The extraction method used
    """
    # Create run-specific output directory if it doesn't exist
    output_dir = Path("data/output") / run_id
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get timestamp for file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Handle different result types
    if isinstance(result, BaseModel):
        # Save Graph objects as JSON using model_dump_json directly
        filename = output_dir / f"{procedure_name}_{step}_{method}_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(result.model_dump_json(indent=2))
    else:
        # Save string results as Markdown
        filename = output_dir / f"{procedure_name}_{step}_{method}_{timestamp}.md"
        content = str(result)  # Convert to string if it's not already
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    logger.info(f"Saved {step} result to {filename}")
