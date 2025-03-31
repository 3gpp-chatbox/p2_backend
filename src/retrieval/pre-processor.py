import os
import sys
import re
from docx import Document
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.lib.logger import get_logger

logger = get_logger(__name__)

def clean_heading(text):
    """Remove leading numbers and spaces from headings."""
    return re.sub(r'^\d+(\.\d+)*\s*', '', text).strip().lower()

def is_excluded_heading(text, exclude_sections):
    """Check if a heading should be excluded."""
    cleaned = clean_heading(text)
    return any(cleaned.startswith(section.lower()) for section in exclude_sections)

def extract_tables(table):
    """
    Convert a DOCX table into Markdown format.

    Args:
        table (Table): A table object from python-docx.

    Returns:
        str: Table formatted in Markdown.
    """
    md_table = []
    
    for i, row in enumerate(table.rows):
        cells = [cell.text.strip() for cell in row.cells]
        md_table.append("| " + " | ".join(cells) + " |")  # Markdown row
        
        # Add header separator after the first row
        if i == 0:
            md_table.append("|" + " --- |" * len(cells))

    return "\n".join(md_table) if md_table else ""

def extract_paragraphs_and_tables(doc):
    """
    Extract paragraphs and tables from the document in order.

    Args:
        doc (Document): The loaded DOCX document.

    Returns:
        List[Dict]: Ordered content containing:
            - type (str): "paragraph" or "table".
            - text (str) or (list): Content of the paragraph/table.
            - style (str, optional): Style of the paragraph.
            - level (int, optional): Heading level if applicable.
    """
    content = []
    inside_contents_section = False  

    for element in doc.element.body:
        if element.tag.endswith('p'):  # Paragraph
            para = next(p for p in doc.paragraphs if p._element == element)
            text = para.text.strip()
            if not text:
                continue

            style = para.style.name
            level = int(style[-1]) if style.startswith("Heading") and style[-1].isdigit() else None

            # Skip "Contents" section
            if text.lower() == "contents":
                inside_contents_section = True
                logger.info("Skipping 'Contents' section")
                continue

            # Stop skipping when a heading appears
            if style.startswith("Heading") and inside_contents_section:
                inside_contents_section = False

            if inside_contents_section:
                continue

            content.append({
                "type": "paragraph",
                "text": text,
                "style": style,
                "level": level
            })

        elif element.tag.endswith('tbl'):  # Table
            table = next(t for t in doc.tables if t._element == element)
            table_md = extract_tables(table)
            if table_md:
                content.append({"type": "table", "text": table_md})

    return content

def extract_filtered_content(content, exclude_sections):
    """
    Extract main content, including tables, while filtering excluded sections.

    Args:
        content (list): List of content dictionaries (paragraphs and tables).
        exclude_sections (set): Sections to be excluded.

    Returns:
        list: Filtered Markdown content.
    """
    filtered_content = []
    exclude_section = False

    for item in content:
        if item["type"] == "paragraph":
            text = item["text"]
            is_heading = item["style"].startswith("Heading")

            if is_heading and is_excluded_heading(text, exclude_sections):
                exclude_section = True
                continue

            if is_heading and not is_excluded_heading(text, exclude_sections):
                exclude_section = False

            if not exclude_section:
                if is_heading:
                    level = item["level"] or 2
                    filtered_content.append(f"{'#' * level} {text}")
                else:
                    filtered_content.append(text)

        elif item["type"] == "table" and not exclude_section:
            filtered_content.append(item["text"])

    return filtered_content

def extract_excluded_content(content, exclude_sections):
    """
    Extracts content from excluded sections, including tables.

    Args:
        content (list): List of content dictionaries.
        exclude_sections (set): Sections to be excluded.

    Returns:
        list: Excluded content.
    """
    excluded_content = []
    exclude_section = False

    for item in content:
        if item["type"] == "paragraph":
            text = item["text"]
            is_heading = item["style"].startswith("Heading")

            if is_heading and is_excluded_heading(text, exclude_sections):
                exclude_section = True

            if exclude_section:
                excluded_content.append(text)

        elif item["type"] == "table" and exclude_section:
            excluded_content.append(item["text"])

    return excluded_content

def extract_toc(content):
    """
    Extracts the table of contents based on headings.

    Args:
        content (list): List of content dictionaries.

    Returns:
        list: TOC content.
    """
    toc_content = []
    for item in content:
        if item["type"] == "paragraph" and item["style"].startswith("Heading"):
            level = item["level"] or 2
            toc_content.append(f"{'  ' * (level-1)}- {item['text']}")

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
        "24501-toc.md": toc_content
    }

    for filename, content in files.items():
        try:
            file_path = os.path.join(output_folder, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n\n".join(content))
            logger.info(f"Saved {filename} to {output_folder}")
        except Exception as e:
            logger.error(f"Error saving {filename}: {e}")

def docx_to_markdown(file_path, save_markdown=False, output_folder="../../data/markdown"):
    """
    Convert DOCX to Markdown while keeping tables.

    Args:
        file_path (str): Path to the DOCX file.
        save_markdown (bool): Whether to save Markdown.
        output_folder (str): Folder to save output.

    Returns:
        str: Filtered Markdown content.
    """
    try:
        logger.info(f"Processing file: {file_path}")
        doc = Document(file_path)
        content = extract_paragraphs_and_tables(doc)

        exclude_sections = {
            "annex", "void", "foreword", "scope", 
            "references", "definitions and abbreviations",
            "definitions", "abbreviations"
        }

        filtered_content = extract_filtered_content(content, exclude_sections)
        excluded_content = extract_excluded_content(content, exclude_sections)
        toc_content = extract_toc(content)

        if save_markdown:
            save_markdown_files(filtered_content, excluded_content, toc_content, output_folder)

        return "\n\n".join(filtered_content)
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")
        return ""

# Example usage
if __name__ == "__main__":
    markdown_text = docx_to_markdown("../../data/raw/24501-j11.docx", save_markdown=True)
