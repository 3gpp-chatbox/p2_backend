"""Pydantic models for document context types.

This module defines Pydantic models for document context related data structures.
"""

from typing import List

from pydantic import BaseModel, Field


class DocumentContext(BaseModel):
    """A Pydantic model representing document context information.

    This model contains the context content and top-level sections of a document
    for a specific procedure.

    Attributes:
        context (str): The retrieved content of the sections.
        top_level_sections (List[str]): List of top-level sections found for the procedure.
    """

    context: str = Field(description="The retrieved content of the sections")
    top_level_sections: List[str] = Field(
        description="List of top-level sections found for the procedure"
    )
