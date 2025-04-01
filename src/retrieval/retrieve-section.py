import re
from typing import List, Set

def is_descendant(section: str, potential_parent: str) -> bool:
    """
    Check if a section is a descendant of another section.
    
    Args:
        section (str): Section number to check (e.g., "3.2.1.4")
        potential_parent (str): Potential parent section (e.g., "3.2.1")
        
    Returns:
        bool: True if section is a descendant of potential_parent
    """
    # Handle non-numeric section identifiers
    if not section or not potential_parent:
        return False
        
    # Split sections into numeric parts
    section_parts = section.split('.')
    parent_parts = potential_parent.split('.')
    
    # Check if section is longer and starts with parent
    if len(section_parts) <= len(parent_parts):
        return False
        
    return section.startswith(potential_parent + '.')

def extract_section_number(line: str) -> str:
    """
    Extract section number from a TOC line.
    
    Args:
        line (str): Line from TOC (e.g., "3.2.1 Registration procedure")
        
    Returns:
        str: Section number or empty string if not found
    """
    match = re.match(r'^[\s-]*(\d+(?:\.\d+)*)', line)
    return match.group(1) if match else ''

def find_procedure_sections(toc_lines: List[str], procedure_name: str) -> List[str]:
    """
    Find all sections in TOC that mention the procedure name.
    
    Args:
        toc_lines (List[str]): Lines from table of contents
        procedure_name (str): Name of procedure to search for
        
    Returns:
        List[str]: List of section numbers mentioning the procedure
    """
    sections = []
    procedure_lower = procedure_name.lower()
    
    for line in toc_lines:
        if procedure_lower in line.lower():
            section_num = extract_section_number(line)
            if section_num:
                sections.append(section_num)
                
    return sections

def filter_top_level_sections(sections: List[str]) -> List[str]:
    """
    Filter out descendant sections, keeping only top-level ones.
    
    Args:
        sections (List[str]): List of section numbers (e.g., ["3.2.1", "3.2.1.4", "3.2.1.2"])
        
    Returns:
        List[str]: List of top-level section numbers (e.g., ["3.2.1"])
    """
    top_level_sections = []
    
    # Sort sections to ensure proper comparison
    sorted_sections = sorted(sections)
    
    for i, section in enumerate(sorted_sections):
        is_top_level = True
        
        # Check if this section is a descendant of any previous section
        for potential_parent in sorted_sections[:i]:
            if is_descendant(section, potential_parent):
                is_top_level = False
                break
                
        if is_top_level:
            top_level_sections.append(section)
            
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
        # Split TOC into lines
        toc_lines = toc_content.split('\n')
        
        # Find all sections mentioning the procedure
        all_sections = find_procedure_sections(toc_lines, procedure_name)
        
        # Filter to get only top-level sections
        top_level_sections = filter_top_level_sections(all_sections)
        
        return top_level_sections
        
    except Exception as e:
        print(f"Error processing TOC for procedure '{procedure_name}': {e}")
        return []

# Example usage
if __name__ == "__main__":
    sample_toc = """
    3.2 Mobility Management procedures
    3.2.1 Registration procedure
    3.2.1.1 General
    3.2.1.2 Initial Registration
    3.2.1.4 Registration procedure steps
    3.4 Other procedures
    """
    
    result = get_procedure_sections(sample_toc, "Registration")
    print(f"Top-level sections: {result}")  # Should print: ['3.2.1']