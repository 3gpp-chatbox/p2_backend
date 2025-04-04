import re
import sys
from pathlib import Path
from typing import List
from docx import Document
from pre_processor import extract_paragraphs, extract_toc
from src.lib.logger import get_logger

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

logger = get_logger(__name__)

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
        
    section_parts = section.split('.')
    parent_parts = potential_parent.split('.')
    
    return len(section_parts) > len(parent_parts) and section.startswith(potential_parent + '.')

def extract_section_number(line: str) -> str:
    """
    Extract section number from a TOC line.
    
    Args:
        line (str): Line from TOC 
        
    Returns:
        str: Section number or empty string if not found
    """
    match = re.match(r'^[\s-]*(\d+(?:\.\d+)*)', line.strip())
    return match.group(1) if match else ''

def find_procedure_sections(toc_lines: List[str], procedure_name: str) -> List[tuple]:
    """
    Find all sections in TOC that mention the procedure name and rank them.
    
    Args:
        toc_lines (List[str]): TOC lines
        procedure_name (str): Procedure name to search for
        
    Returns:
        List[tuple]: List of (section_number, score) tuples
    """
    sections = []
    procedure_lower = procedure_name.lower()
    
    for line in toc_lines:
        line_lower = line.lower()
        section_num = extract_section_number(line)

        if section_num:
            if procedure_lower == line_lower.split():  # Exact match
                score = 3
            elif procedure_lower in line_lower:  # Partial match
                score = 2
            else:  # Weak match
                score = 1
            
            sections.append((section_num, score))
    
    # Sort by highest score first, then by section number order
    sections.sort(key=lambda x: (-x[1], x[0]))
    logger.info(f"Found sections with scores: {sections}")

    # Return all sections with their scores
    return sections

def filter_top_level_sections(sections: List[tuple]) -> List[tuple]:
    """
    Filter out descendant sections, keeping only top-level ones with highest scores.
    
    Args:
        sections (List[tuple]): List of (section_number, score) tuples
        
    Returns:
        List[tuple]: List of top-level (section_number, score) tuples
    """
    top_level_sections = []
    # Sort by score first (descending), then by section number
    sorted_sections = sorted(sections, key=lambda x: (-x[1], x[0]))
    
    # Get the highest score
    highest_score = sorted_sections[0][1] if sorted_sections else 0
    
    for i, (section, score) in enumerate(sorted_sections):
        # Only keep sections with the highest score
        if score < highest_score:
            break
            
        if not any(is_descendant(section, parent) for parent, _ in sorted_sections[:i]):
            top_level_sections.append((section, score))
            logger.info(f"Top-level section: {section} (score: {score})")
    
    return top_level_sections

def get_procedure_sections(toc_content: str, procedure_name: str) -> List[str]:
    """
    Main function to get top-level sections for a procedure from TOC.
    
    Args:
        toc_content (str): Table of contents text
        procedure_name (str): Name of procedure to search for
        
    Returns:
        List[str]: List of top-level section numbers related to the procedure
    """
    try:
        toc_lines = toc_content.strip().split('\n')
        
        logger.info(f"Searching for sections containing '{procedure_name}'")
        all_sections = find_procedure_sections(toc_lines, procedure_name)
        logger.debug(f"Found sections with scores: {all_sections}")
        
        top_level_sections = filter_top_level_sections(all_sections)
        logger.info(f"Identified {len(top_level_sections)} top-level sections with highest scores")
        
        # Return only section numbers
        return [section[0] for section in top_level_sections]
        
    except Exception as e:
        logger.error(f"Error processing TOC for procedure '{procedure_name}': {e}")
        return []

# Example usage
if __name__ == "__main__":
    try:
        logger.info("Loading document...")
        file_path = "data/raw/24501-j11.docx"
        doc = Document(file_path)
        paragraphs = extract_paragraphs(doc)
        
        logger.info("Extracting table of contents...")
        toc_content = extract_toc(paragraphs)
        
        procedure_name = "mobility and periodic registration update"
        logger.info(f"Searching for sections related to '{procedure_name}'")
        result = get_procedure_sections("\n".join(toc_content), procedure_name)
        
        if not result:
            logger.warning("No sections found")
        elif len(result) == 1:
            logger.info(f"Found single section: {result[0]}")
        else:
            logger.info(f"Found multiple sections: {result}")
    except Exception as e:
        logger.error(f"Error loading document: {e}", exc_info=True)
