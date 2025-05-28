import re
from typing import List

import numpy as np
from docx import Document

from src.lib.logger import logger
from src.retrieval.pre_processor import _extract_paragraphs, _extract_toc


def is_descendant(section: str, potential_parent: str) -> bool:
    """
    Check if a section is a descendant of another section.

    Args:
        section (str): Section number to check
        potential_parent (str): Potential parent section

    Returns:
        bool: True if section is a descendant of potential_parent
    """
    if not section or not potential_parent:
        return False

    section_parts = section.split(".")
    parent_parts = potential_parent.split(".")

    return len(section_parts) > len(parent_parts) and section.startswith(
        potential_parent + "."
    )


def extract_section_number(line: str) -> str:
    """
    Extract section number from a TOC line.

    Args:
        line (str): Line from TOC

    Returns:
        str: Section number or empty string if not found
    """
    match = re.match(r"^[\s-]*(\d+(?:\.\d+)*)", line.strip())
    return match.group(1) if match else ""


def find_procedure_section_lines(
    toc_lines: List[str], procedure_name: str
) -> List[str]:
    """
    Find all sections in TOC that mention the procedure name.

    Args:
        toc_lines (List[str]): List of TOC lines.
        procedure_name (str): Procedure name to search for.

    Returns:
        List[str]: List of all relevant sections.
    """
    sections = []
    procedure_lower = procedure_name.lower()

    for line in toc_lines:
        line_lower = line.lower()
        if procedure_lower == line_lower:  # Exact match
            sections.append(line)
        elif procedure_lower in line_lower:  # Partial match
            sections.append(line)

    return sections


def get_top_level_sections(section_lines: List[str]) -> np.ndarray:
    """
    Given a list of section lines, return only top-level section numbers (no descendants).

    Args:
        section_lines (List[str]): List of TOC lines matching the procedure.

    Returns:
        np.ndarray: Numpy array of top-level section numbers.
    """
    # Extract the section numbers and convert to a NumPy array
    section_numbers = np.array(
        [
            extract_section_number(line)
            for line in section_lines
            if extract_section_number(line)
        ]
    )

    # Sort the section numbers to ensure parents come before children
    section_numbers = np.sort(section_numbers)

    top_level_sections = []

    for section in section_numbers:
        # If section is not a descendant of any already accepted top-level section
        if not any(is_descendant(section, parent) for parent in top_level_sections):
            top_level_sections.append(section)

    # Return as NumPy array
    return np.array(top_level_sections)


# Example usage
if __name__ == "__main__":
    try:
        logger.info("Loading document...")
        file_path = "data/raw/24501-j11.docx"
        doc = Document(file_path)
        paragraphs = _extract_paragraphs(doc)

        logger.info("Extracting table of contents...")
        toc_content = _extract_toc(paragraphs)

        procedure_name = "initial registration"
        logger.info(f"Searching for sections related to '{procedure_name}'")

        # Step 1: Find relevant TOC lines
        procedure_lines = find_procedure_section_lines(toc_content, procedure_name)

        # Step 2: Get top-level sections from those lines
        result = get_top_level_sections(procedure_lines)

        if not result:
            logger.warning(f"No sections found for '{procedure_name}'.")
        else:
            logger.info(f"Found top-level sections: {result}")
    except Exception as e:
        logger.error(f"Error loading document: {e}", exc_info=True)
