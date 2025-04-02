import os
import sys
import re
from docx import Document
from pathlib import Path
# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), "../.."))))

from src.library.logger import get_logger

logger = get_logger(__name__)

def clean_heading(text):
    """
    Clean a heading by removing leading numbers and spaces.
     
    Args:
        text (str): The heading text.
    
    Returns:
        str: Cleaned heading text in lowercase.
    """
    return re.sub(r'^\d+(\.\d+)*\s*', '', text).strip().lower()

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
    Extract paragraphs and tables from the document in their natural order.
    """
    paragraphs = []
    inside_contents_section = False  

    for para in doc.paragraphs:
        text = para.text.strip()
        
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
        level = int(style[-1]) if style.startswith("Heading") and style[-1].isdigit() else None

        # Check for table after this paragraph
        if hasattr(para._element, "getnext") and para._element.getnext() is not None:
            next_elem = para._element.getnext()
            if next_elem.tag.endswith('tbl'):
                # Convert table to markdown directly using the table element
                markdown_table = []
                for row in next_elem.tr_lst:  # Access table rows
                    cells = []
                    for cell in row.tc_lst:  # Access cells in each row
                        # Get text content from cell
                        cell_text = ''.join(t.text.strip() for t in cell.xpath('.//w:t'))
                        cells.append(cell_text.replace('\n', ' '))
                    markdown_table.append('| ' + ' | '.join(cells) + ' |')
                    if len(markdown_table) == 1:  # After header row
                        markdown_table.append('|' + '|'.join(['---' for _ in cells]) + '|')
                
                # Add paragraph if not empty
                if text:
                    paragraphs.append({"text": text, "style": style, "level": level})
                # Add table
                paragraphs.append({"text": '\n'.join(markdown_table), "style": "Table", "level": None})
                continue

        # Add regular paragraph if not empty
        if text:
            paragraphs.append({"text": text, "style": style, "level": level})

    return paragraphs

def extract_filtered_content(paragraphs, exclude_sections):
    """
    Extracts main content with tables in their natural position.
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
    Extracts content from excluded sections, maintaining proper heading formatting.
    Captures all excluded content from the start of the document.
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
            if not is_excluded_heading(text, exclude_sections):
                if current_section:
                    excluded_content.extend(current_section)
                    current_section = []
                exclude_section = False
                continue

        # Handle excluded section start
        if is_heading and is_excluded_heading(text, exclude_sections):
            # Add previous section if exists
            if current_section:
                excluded_content.extend(current_section)
            exclude_section = True
            # Format heading with proper level
            level = para["level"] or 2
            current_section = [f"{'#' * level} {text}"]
            continue

        # Handle non-excluded heading
        if is_heading and not is_excluded_heading(text, exclude_sections):
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
            toc_content.append(f"{'  ' * (level-1)}- {para['text']}")

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
        excluded_content = extract_excluded_content(paragraphs,exclude_sections)
        toc_content = extract_toc(paragraphs)

        if save_markdown:
            save_markdown_files(filtered_content, excluded_content, toc_content, output_folder)

        return "\n\n".join(filtered_content)
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")
        return ""

# Example usage
if __name__ == "__main__":
    markdown_text = docx_to_markdown("../../data/raw/24501-j11.docx", save_markdown=True)
