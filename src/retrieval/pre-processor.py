import os
import sys
import re
from docx import Document

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.lib.logger import get_logger

logger = get_logger(__name__)


def clean_heading(text):
    """
    Clean a heading by removing leading numbers and spaces.

    Args:
        text (str): The heading text.

    Returns:
        str: Cleaned heading text in lowercase.
    """
    return re.sub(r"^\d+(\.\d+)*\s*", "", text).strip().lower()


def is_excluded_heading(text, exclude_sections):
    """
    Check if a heading should be excluded based on predefined sections.

    Args:
        text (str): The heading text.
        exclude_sections (set): Set of section names to exclude.

    Returns:
        bool: True if the heading matches an excluded section, otherwise False.
    """
    cleaned = clean_heading(text)
    return any(cleaned.startswith(section.lower()) for section in exclude_sections)


def extract_paragraphs(doc):
    """
    Extract paragraphs from the document with their styles.

    Args:
        doc (Document): The loaded document object.

    Returns:
        List[Dict]: List of paragraphs, each containing:
            - text (str): The paragraph text.
            - style (str): The paragraph style name.
            - level (int): The heading level (if applicable).
    """
    paragraphs = []
    inside_contents_section = False  # Track if we're inside "Contents"

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue

        style = para.style.name
        level = (
            int(style[-1])
            if style.startswith("Heading") and style[-1].isdigit()
            else None
        )

        # If "Contents" appears (not a heading), start skipping lines
        if text.lower() == "contents":
            inside_contents_section = True
            logger.info("Skipping 'Contents' section")
            continue

        # If a heading appears, stop skipping "Contents"
        if style.startswith("Heading") and inside_contents_section:
            inside_contents_section = False

        # Skip all paragraphs under "Contents"
        if inside_contents_section:
            continue

        paragraphs.append({"text": text, "style": style, "level": level})

    return paragraphs


def extract_filtered_content(paragraphs, exclude_sections):
    """
    Extracts main content, excluding predefined sections.

    Args:
        paragraphs (list): List of paragraph dictionaries.
        exclude_sections (set): Sections to be excluded.

    Returns:
        list: Filtered content.
    """
    filtered_content = []
    exclude_section = False

    for para in paragraphs:
        text = para["text"]
        is_heading = para["style"].startswith("Heading")

        if is_heading and is_excluded_heading(text, exclude_sections):
            exclude_section = True
            continue

        if is_heading and not is_excluded_heading(text, exclude_sections):
            exclude_section = False

        if not exclude_section:
            if is_heading:
                level = para["level"] or 2
                filtered_content.append(f"{'#' * level} {text}")
            else:
                filtered_content.append(text)

    return filtered_content


def extract_excluded_content(paragraphs, exclude_sections):
    """
    Extracts content from excluded sections.

    Args:
        paragraphs (list): List of paragraph dictionaries.
        exclude_sections (set): Sections to be excluded.

    Returns:
        list: Excluded content.
    """
    excluded_content = []
    exclude_section = False

    for para in paragraphs:
        text = para["text"]
        is_heading = para["style"].startswith("Heading")

        if is_heading and is_excluded_heading(text, exclude_sections):
            exclude_section = True

        if exclude_section:
            excluded_content.append(text)

    return excluded_content


def extract_toc(paragraphs):
    """
    Extracts the table of contents based on headings.

    Args:
        paragraphs (list): List of paragraph dictionaries.

    Returns:
        list: TOC content.
    """
    toc_content = []
    for para in paragraphs:
        if para["style"].startswith("Heading"):
            level = para["level"] or 2
            toc_content.append(f"{'  ' * (level - 1)}- {para['text']}")

    return toc_content


def save_markdown_files(main_content, excluded_content, toc_content, output_folder):
    """
    Save extracted content into separate Markdown files.

    Args:
        main_content (list): Filtered content.
        excluded_content (list): Excluded content.
        toc_content (list): Table of contents.
        output_folder (str): Directory to save files.
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
    file_path, save_markdown=False, output_folder="../../data/markdown"
):
    """
    Main function to process DOCX file and extract structured content.

    Args:
        file_path (str): Path to the DOCX file.
        save_markdown (bool): Whether to save the output.
        output_folder (str): Directory to save Markdown files.

    Returns:
        str: Filtered markdown content.
    """
    try:
        logger.info(f"Processing file: {file_path}")
        doc = Document(file_path)
        paragraphs = extract_paragraphs(doc)

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

        filtered_content = extract_filtered_content(paragraphs, exclude_sections)
        excluded_content = extract_excluded_content(paragraphs, exclude_sections)
        toc_content = extract_toc(paragraphs)

        if save_markdown:
            save_markdown_files(
                filtered_content, excluded_content, toc_content, output_folder
            )

        return "\n\n".join(filtered_content)
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")
        return ""


# Example usage
if __name__ == "__main__":
    markdown_text = docx_to_markdown(
        "../../data/raw/24501-j11.docx", save_markdown=True
    )
