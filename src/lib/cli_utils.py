from typing import List

from InquirerPy import inquirer
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Initialize Rich console
console = Console()


def print_header() -> None:
    """Display a styled header for the application.

    This function uses Rich library to create a centered, gold-colored header
    with a panel border.

    Returns:
        None
    """
    header = Text("Procedure Extraction", style="bold gold3")
    centered_header = Align.center(header)
    console.print(Panel(centered_header, border_style="gold3"))


def print_instructions() -> None:
    """Display styled instructions for document selection.

    Prints formatted instructions explaining how to:
    - Navigate through document list using arrow keys
    - Filter documents by typing
    - Select a document using Enter key

    The instructions are styled using Rich text formatting with gold accents
    for key actions.

    Returns:
        None
    """
    instructions = Text()
    instructions.append("\nDocument Selection Instructions:\n\n")
    instructions.append("• Use ", style="white")
    instructions.append("↑↓ arrows", style="gold3")
    instructions.append(" to navigate\n", style="white")
    instructions.append("• Start ", style="white")
    instructions.append("typing", style="gold3")
    instructions.append(" to filter the document list\n", style="white")
    instructions.append("• Press ", style="white")
    instructions.append("Enter", style="gold3")
    instructions.append(" to select\n", style="white")

    console.print(instructions)
    console.print()


def get_procedure_from_user() -> str:
    """Prompt the user to input the procedure to extract.

    Displays a gold-colored prompt asking the user to enter a procedure name.
    The input is stripped of leading/trailing whitespace.

    Returns:
        str: The procedure name entered by the user.
    """
    console.print("[bold gold3]Procedure Input[/]")
    procedure = input(
        "Enter the procedure to extract (e.g., 'Initial Registration'): "
    ).strip()
    console.print()
    return procedure


def get_entity_from_user() -> str:
    """Prompt the user to input the entity.

    Displays a gold-colored prompt asking the user to enter an entity name.
    The input is stripped of whitespace and converted to uppercase.

    Returns:
        str: The entity name in uppercase.
    """
    console.print("[bold gold3]Entity Input[/]")
    entity = input("Enter the entity (e.g., 'UE'): ").strip().upper()
    console.print()
    return entity


async def choose_document(documents: List[str]) -> str:
    """Interactively display a searchable list of documents and allow the user to select one.

    Presents an interactive fuzzy search interface where users can:
    - Navigate through choices with arrow keys
    - Type to filter/search through documents
    - Press Enter to select the highlighted document

    Args:
        documents: List of document names to choose from.

    Returns:
        str: The selected document name.

    Raises:
        ValueError: If the selected document is not in the provided list.
    """
    console.print("[bold gold3]Document Selection[/]")
    result = await inquirer.fuzzy(
        message="Select a document:",
        choices=documents,
        instruction="(Use ↑↓ arrows to navigate, type to filter, Enter to select)",
        mandatory=True,
        validate=lambda x: x in documents,
        invalid_message="Please select a valid document",
        border=True,
        cycle=True,
    ).execute_async()
    console.print()
    return result


def print_results(procedure: str, entity: str, document: str) -> None:
    """Display the final results in a styled panel.

    Creates a formatted panel using Rich library to display the selected:
    - Procedure name
    - Entity
    - Document

    Args:
        procedure: The name of the procedure to be extracted.
        entity: The entity name (in uppercase).
        document: The selected document identifier.

    Returns:
        None
    """
    results = Text.assemble(
        ("Selected Details\n\n", "bold gold3"),
        ("Procedure: ", "bold gold3"),
        (f"{procedure}\n", "white"),
        ("Entity: ", "bold gold3"),
        (f"{entity}\n", "white"),
        ("Document: ", "bold gold3"),
        (f"{document}\n", "white"),
    )
    console.print(Panel(results, border_style="gold3"))
