"""Type definitions for document processing."""

from typing import Optional, TypedDict


class ParaDict(TypedDict):
    """Dictionary type for paragraph information.

    Attributes:
        text: The text content of the paragraph.
        style: The style name of the paragraph.
        level: The heading level (if applicable).
    """

    text: str
    style: str
    level: Optional[int]


class MarkdownOutput(TypedDict):
    """Dictionary type for docx_to_markdown output.

    Attributes:
        content: The main filtered markdown content.
        toc: The table of contents in markdown format.
        doc_name: The name/title of the document.
    """

    content: str
    toc: str
    doc_name: str
