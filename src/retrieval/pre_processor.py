import os
import re
import sys
from pathlib import Path
from typing import List

from docx import Document

from src.schemas.types.document import MarkdownOutput, ParaDict

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.lib.logger import get_logger

logger = get_logger(__name__)


def _normalize_whitespace(text: str) -> str:
    """
    Normalize whitespace in text by replacing non-breaking spaces and tabs with regular spaces,
    and reducing multiple consecutive spaces to a single space.

    Args:
        text (str): The input text to normalize.

    Returns:
        str: Text with normalized whitespace.
    """
    # Replace non-breaking spaces and tabs with regular spaces
    text = text.replace("\u00a0", " ").replace("\t", " ")
    # Replace multiple consecutive spaces with a single space
    return re.sub(r"\s+", " ", text)


def _clean_heading(text: str) -> str:
    """
    Clean a heading by removing leading numbers and spaces.

    Args:
        text (str): The heading text.

    Returns:
        str: Cleaned heading text in lowercase.
    """
    return re.sub(r"^\d+(\.\d+)*\s*", "", text).strip().lower()


def _is_excluded_heading(text: str, exclude_sections: list[str]) -> bool:
    """
    Check if a heading should be excluded based on predefined sections.

    Args:
        text (str): The heading text to check
        exclude_sections (list[str]): List of section names to check against

    Returns:
        bool: True if the heading matches one of the excluded sections, False otherwise
    """
    cleaned = _clean_heading(text)
    return any(cleaned.startswith(section.lower()) for section in exclude_sections)


def _extract_paragraphs(doc: Document) -> List[ParaDict]:
    """
    Extract paragraphs and tables from the document in their natural order.

    Args:
        doc (Document): The Word document to extract content from.

    Returns:
        List[ParaDict]: List of paragraphs where each paragraph is a dictionary containing:
            - text (str): The paragraph text content
            - style (str): The paragraph style name
            - level (Optional[int]): The heading level if applicable
    """
    paragraphs = []
    inside_contents_section = False

    for para in doc.paragraphs:
        text = _normalize_whitespace(para.text.strip())

        # Handle Contents section
        if text.lower() == "contents":
            inside_contents_section = True
            continue
        if inside_contents_section and para.style.name.startswith("Heading"):
            inside_contents_section = False
        if inside_contents_section:
            continue

        # Get paragraph style and level
        style = para.style.name
        level = (
            int(style[-1])
            if style.startswith("Heading") and style[-1].isdigit()
            else None
        )

        # Check for table after this paragraph
        if hasattr(para._element, "getnext") and para._element.getnext() is not None:
            next_elem = para._element.getnext()
            if next_elem.tag.endswith("tbl"):
                # Convert table to markdown directly using the table element
                markdown_table = []
                for row in next_elem.tr_lst:  # Access table rows
                    cells = []
                    for cell in row.tc_lst:  # Access cells in each row
                        # Get text content from cell
                        cell_text = "".join(
                            t.text.strip() for t in cell.xpath(".//w:t")
                        )
                        cells.append(cell_text.replace("\n", " "))
                    markdown_table.append("| " + " | ".join(cells) + " |")
                    if len(markdown_table) == 1:  # After header row
                        markdown_table.append(
                            "|" + "|".join(["---" for _ in cells]) + "|"
                        )

                # Add paragraph if not empty
                if text:
                    paragraphs.append({"text": text, "style": style, "level": level})
                # Add table
                paragraphs.append(
                    {"text": "\n".join(markdown_table), "style": "Table", "level": None}
                )
                continue

        # Add regular paragraph if not empty
        if text:
            paragraphs.append({"text": text, "style": style, "level": level})

    return paragraphs


def _extract_filtered_content(
    paragraphs: List[ParaDict], exclude_sections: list[str]
) -> List[str]:
    """
    Extracts main content with tables in their natural position.

    Args:
        paragraphs (List[ParaDict]): List of paragraph dictionaries
        exclude_sections (list[str]): List of section names to exclude

    Returns:
        List[str]: List of markdown-formatted content lines
    """
    filtered_content = []
    exclude_section = False
    found_first_heading = False

    for para in paragraphs:
        text = para["text"]
        is_heading = para["style"].startswith("Heading")

        # Mark first heading found
        if is_heading:
            found_first_heading = True

        # Skip content until we find first heading
        if not found_first_heading:
            continue

        if is_heading and _is_excluded_heading(text, exclude_sections):
            exclude_section = True
            continue

        if is_heading and not _is_excluded_heading(text, exclude_sections):
            exclude_section = False

        if not exclude_section:
            if is_heading:
                level = para["level"] or 2
                filtered_content.append(f"{'#' * level} {text}")
            else:
                filtered_content.append(text)

    return filtered_content


def _extract_excluded_content(
    paragraphs: List[ParaDict], exclude_sections: list[str]
) -> List[str]:
    """
    Extracts content from excluded sections, maintaining proper heading formatting.
    Captures all excluded content from the start of the document.

    Args:
        paragraphs (List[ParaDict]): List of paragraph dictionaries
        exclude_sections (list[str]): List of section names to exclude

    Returns:
        List[str]: List of markdown-formatted content lines from excluded sections
    """
    excluded_content = []
    exclude_section = True
    current_section = []
    found_first_heading = False

    for para in paragraphs:
        text = para["text"]
        is_heading = para["style"].startswith("Heading")

        # Handle first heading case
        if is_heading and not found_first_heading:
            found_first_heading = True
            # If first heading is not excluded, add previous content and stop excluding
            if not _is_excluded_heading(text, exclude_sections):
                if current_section:
                    excluded_content.extend(current_section)
                    current_section = []
                exclude_section = False
                continue

        # Handle excluded section start
        if is_heading and _is_excluded_heading(text, exclude_sections):
            # Add previous section if exists
            if current_section:
                excluded_content.extend(current_section)
            exclude_section = True
            # Format heading with proper level
            level = para["level"] or 2
            current_section = [f"{'#' * level} {text}"]
            continue

        # Handle non-excluded heading
        if is_heading and not _is_excluded_heading(text, exclude_sections):
            if exclude_section and current_section:
                excluded_content.extend(current_section)
                current_section = []
            exclude_section = False
            continue

        # Collect content while in excluded section
        if exclude_section:
            if para["style"] == "Table":
                current_section.append(text)  # Tables are already formatted
            else:
                current_section.append(text)

    # Add any remaining excluded content
    if current_section:
        excluded_content.extend(current_section)

    return excluded_content


def _extract_toc(paragraphs: List[ParaDict]) -> List[str]:
    """
    Extracts the table of contents based on headings.

    Args:
        paragraphs (List[ParaDict]): List of paragraph dictionaries containing:
            - text (str): The paragraph text content
            - style (str): The paragraph style name
            - level (Optional[int]): The heading level if applicable

    Returns:
        List[str]: List of markdown-formatted table of contents entries
    """
    toc_content = []
    for para in paragraphs:
        if para["style"].startswith("Heading"):
            level = para["level"] or 2
            toc_content.append(f"{'  ' * (level - 1)}- {para['text']}")

    return toc_content


def _save_markdown_files(
    main_content: List[str],
    excluded_content: List[str],
    toc_content: List[str],
    output_folder: str,
) -> None:
    """
    Save extracted content into separate Markdown files.

    Args:
        main_content (List[str]): List of markdown-formatted main content lines
        excluded_content (List[str]): List of markdown-formatted excluded content lines
        toc_content (List[str]): List of markdown-formatted table of contents lines
        output_folder (str): Directory path where markdown files will be saved

    Note:
        Creates three files in the output directory:
        - 24501-filtered.md: Contains the main content
        - 24501-excluded.md: Contains the excluded sections
        - 24501-toc.md: Contains the table of contents
    """
    os.makedirs(output_folder, exist_ok=True)

    files = {
        "24501-filtered.md": main_content,
        "24501-excluded.md": excluded_content,
        "24501-toc.md": toc_content,
    }

    for filename, content in files.items():
        try:
            file_path = os.path.join(output_folder, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n\n".join(content))
            logger.info(f"Saved {filename} to {output_folder}")
        except Exception as e:
            logger.error(f"Error saving {filename}: {e}")


def docx_to_markdown(
    file_path: str, save_markdown: bool = False, output_folder: str = "data/markdown"
) -> MarkdownOutput:
    """
    Main function to process DOCX file and extract structured content.

    Args:
        file_path (str): Path to the DOCX file.
        save_markdown (bool): Whether to save the output.
        output_folder (str): Directory to save Markdown files.

    Returns:
        MarkdownOutput: A dictionary with:
            - content (str): Filtered markdown content
            - toc (str): Table of contents in markdown format
            - doc_name (str): Name/title of the document
    """
    try:
        logger.info(f"Processing file: {file_path}")
        doc = Document(file_path)
        # Get doc name from core properties or fallback to file name without extension
        doc_name = doc.core_properties.title
        if not doc_name:
            doc_name = Path(file_path).stem
        paragraphs = _extract_paragraphs(doc)

        exclude_sections = {
            "annex",
            "void",
            "foreword",
            "scope",
            "references",
            "definitions and abbreviations",
            "definitions",
            "abbreviations",
        }

        filtered_content = _extract_filtered_content(paragraphs, exclude_sections)
        excluded_content = _extract_excluded_content(paragraphs, exclude_sections)
        toc_content = _extract_toc(paragraphs)

        if save_markdown:
            _save_markdown_files(
                filtered_content, excluded_content, toc_content, output_folder
            )

        return {
            "content": "\n\n".join(filtered_content),
            "toc": "\n\n".join(toc_content),
            "doc_name": doc_name,
        }
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")
        raise ValueError(f"Failed to convert file: {file_path} to Markdown.")


# Example usage
if __name__ == "__main__":
    file_path = "data/raw/24501-j11.docx"
    result = docx_to_markdown(file_path, save_markdown=True)
    print("Content length:", len(result["content"]))
    print("Table of contents length:", len(result["toc"]))
