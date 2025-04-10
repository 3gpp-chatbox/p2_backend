"""Prompt management system for loading and rendering prompt templates.

This module provides a flexible system for managing prompt templates used in
various parts of the application. It supports loading templates from files,
rendering them with parameters, and validating template parameters.

Example:
    ```python
    # Initialize the prompt manager
    manager = PromptManager("templates/")

    # Render a template with parameters
    prompt = manager.render_prompt(
        "welcome_message",
        name="Alice",
        role="Developer"
    )
    ```
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))
from src.lib.logger import get_logger

logger = get_logger(__name__)


class PromptManager:
    """Manages loading and rendering of prompt templates.

    This class handles the loading of prompt templates from text files and
    provides methods for rendering them with parameters. It supports dynamic
    parameter validation and template management.

    Attributes:
        templates_dir (Path): Directory containing the prompt template files.
        templates (Dict[str, str]): Dictionary mapping template names to their content.

    Example:
        ```python
        manager = PromptManager()
        prompt = manager.render_prompt("greeting", name="Alice")
        print(prompt)  # Outputs rendered template with "Alice" as name
        ```
    """

    def __init__(self, templates_dir: Optional[Union[str, Path]] = None) -> None:
        """Initialize the PromptManager with the specified templates directory.

        Args:
            templates_dir: Directory containing prompt templates.
                         If None, defaults to <project_root>/src/prompts/active/
                         Can be either a string path or Path object.

        Raises:
            ValueError: If templates directory does not exist or is not a directory.
                      Also raised for initialization failures like permission errors.

        Example:
            ```python
            # Use default templates directory
            manager = PromptManager()

            # Use custom templates directory
            manager = PromptManager("path/to/templates")
            ```
        """
        if templates_dir is None:
            templates_dir = Path("src/prompts/active/")

        try:
            # Convert to Path object if string was provided
            templates_dir = Path(templates_dir)
        except TypeError as e:
            logger.error(f"Invalid type for templates_dir: {type(templates_dir)}")
            raise ValueError(f"Invalid templates directory type: {str(e)}")

        try:
            if not templates_dir.exists():
                logger.error(f"Templates directory does not exist: {templates_dir}")
                raise ValueError(f"Templates directory does not exist: {templates_dir}")

            if not templates_dir.is_dir():
                logger.error(f"Templates path is not a directory: {templates_dir}")
                raise ValueError(f"Templates path is not a directory: {templates_dir}")

            logger.info(
                f"Initializing PromptManager with templates directory: {templates_dir}"
            )
            self.templates_dir = templates_dir
            self.templates: Dict[str, str] = {}
            self._load_templates()

        except PermissionError as e:
            logger.error(
                f"Permission denied accessing templates directory: {templates_dir}"
            )
            raise ValueError(
                f"Permission denied accessing templates directory: {str(e)}"
            )
        except OSError as e:
            logger.error(f"Failed to access templates directory: {templates_dir}")
            raise ValueError(f"Failed to access templates directory: {str(e)}")

    def _load_templates(self) -> None:
        """Load all prompt templates from the templates directory.

        Reads all .md files in the templates directory and loads them into
        the templates dictionary. Each template file's name (without .txt)
        becomes the key in the templates dictionary.

        Raises:
            ValueError: If template files are invalid, empty, or cannot be read.
            OSError: If there are filesystem-related errors (permissions, etc).

        Notes:
            - Template files must have .md extension
            - Template files must not be empty
            - Template files must be UTF-8 encoded
            - Template names are derived from filenames without extension
        """
        try:
            template_files = list(self.templates_dir.glob("*.md"))
            logger.info(f"Found {len(template_files)} template files in directory")

            for file_path in template_files:
                # Extract template name by removing .txt extension
                template_name = file_path.stem

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if not content.strip():
                            logger.error(f"Empty template file found: {template_name}")
                            raise ValueError(
                                f"Template file '{template_name}' is empty"
                            )
                        self.templates[template_name] = content
                        logger.debug(f"Loaded template: {template_name}")
                except (IOError, UnicodeDecodeError) as e:
                    logger.error(f"Failed to read template {template_name}: {str(e)}")
                    raise ValueError(
                        f"Failed to read template '{template_name}': {str(e)}"
                    )
        except OSError as e:
            logger.error(f"Failed to read templates directory: {str(e)}")
            raise OSError(f"Failed to read templates directory: {str(e)}")

        logger.info(f"Successfully loaded {len(self.templates)} templates")

    def render_prompt(self, template_name: str, **kwargs: str) -> str:
        """Render a prompt template by replacing placeholders with provided parameters.

        Args:
            template_name: Name of the template to render. Must exist in templates dict.
            **kwargs: Keyword arguments used to replace placeholders in the template.
                     Each key should correspond to a placeholder in the template.

        Returns:
            str: The fully rendered prompt with all placeholders replaced.

        Raises:
            KeyError: If the specified template does not exist.
            ValueError: If parameter validation or rendering fails (missing/invalid params).

        Example:
            ```python
            # Template content: "Hello {name}, welcome to {project}!"
            prompt = manager.render_prompt(
                "welcome",
                name="Alice",
                project="Python Project"
            )
            # Result: "Hello Alice, welcome to Python Project!"
            ```
        """
        if not isinstance(template_name, str):
            logger.error(f"Template name must be a string, got {type(template_name)}")
            raise TypeError(
                f"Template name must be a string, got {type(template_name)}"
            )

        if not template_name:
            logger.error("Template name cannot be empty")
            raise ValueError("Template name cannot be empty")

        if template_name not in self.templates:
            logger.error(f"Template not found: {template_name}")
            raise KeyError(f"Prompt template '{template_name}' not found")

        logger.debug(f"Rendering template {template_name} with parameters: {kwargs}")
        template = self.templates[template_name]
        try:
            rendered = template.format(**kwargs)
            logger.debug(f"Successfully rendered template {template_name}")
            return rendered
        except (KeyError, ValueError, IndexError) as e:
            logger.error(f"Error rendering template {template_name}: {str(e)}")
            raise ValueError(f"Error rendering prompt '{template_name}': {str(e)}")

    def get_available_prompts(self) -> List[str]:
        """Get a list of all available prompt template names.

        Returns:
            List[str]: Sorted list of template names (without .md extension).

        Example:
            ```python
            manager = PromptManager()
            templates = manager.get_available_prompts()
            print(templates)  # Output: ['greeting', 'help', 'welcome']
            ```
        """
        return sorted(list(self.templates.keys()))

    def list_parameters(self, template_name: str) -> List[str]:
        """List all parameters required by a prompt template.

        Analyzes the template content to find all unique parameter placeholders
        using regex pattern matching.

        Args:
            template_name: Name of the template to analyze. Must exist in templates dict.

        Returns:
            List[str]: List of unique parameter names required by the template,
                      sorted alphabetically for consistency.

        Raises:
            KeyError: If the specified template does not exist.
            ValueError: If the template syntax is malformed or invalid.

        Example:
            ```python
            # Template content: "Hello {name}, welcome to {project}!"
            params = manager.list_parameters("welcome")
            print(params)  # Output: ['name', 'project']
            ```
        """
        if template_name not in self.templates:
            logger.error(f"Template not found: {template_name}")
            raise KeyError(f"Prompt template '{template_name}' not found")

        template = self.templates[template_name]
        try:
            # Use regex to find all unique parameter names in {param_name} format
            pattern: str = r"\{(\w+)\}"
            params: List[str] = re.findall(pattern, template)
            unique_params = sorted(list(set(params)))
            logger.debug(
                f"Found parameters in template {template_name}: {unique_params}"
            )
            return unique_params
        except re.error as e:
            logger.error(f"Invalid regex pattern in template {template_name}: {str(e)}")
            raise ValueError(
                f"Template '{template_name}' contains invalid placeholder syntax"
            )
        except Exception as e:
            logger.error(f"Unexpected error parsing template {template_name}: {str(e)}")
            raise ValueError(f"Failed to analyze template '{template_name}': {str(e)}")


if __name__ == "__main__":
    # Example usage of PromptManager

    def print_separator(title: str = "") -> None:
        """Print a separator line with an optional title."""
        print(f"\n{'-' * 20} {title} {'-' * 20}\n")

    try:
        # Initialize PromptManager with default templates directory
        print_separator("Initializing PromptManager")
        manager = PromptManager()
        print("PromptManager initialized successfully")

        # List available templates
        print_separator("Available Templates")
        templates = manager.get_available_prompts()
        print(f"Found templates: {templates}")

        # Get parameters for test_prompt
        print_separator("Template Parameters")
        template_name = "test_prompt"
        try:
            params = manager.list_parameters(template_name)
            print(f"Parameters required for {template_name}: {params}")
        except KeyError as e:
            print(f"Error: {e}")

        # Successful prompt rendering
        print_separator("Successful Render")
        try:
            rendered = manager.render_prompt(
                "test_prompt", name="Alice", project_name="Project X", role="Developer"
            )
            print("Rendered prompt:")
            print(rendered)
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

        # Error case: Missing parameter
        print_separator("Error Case - Missing Parameter")
        try:
            rendered = manager.render_prompt(
                "test_prompt",
                name="Bob",
                # project_name="Project X",  # missing intentionally
                role="Manager",
            )
            print(rendered)
        except ValueError as e:
            print(f"Expected error occurred: {e}")

        # Error case: Invalid template
        print_separator("Error Case - Invalid Template")
        try:
            rendered = manager.render_prompt("non_existent_template", param1="value1")
            print(rendered)
        except KeyError as e:
            print(f"Expected error occurred: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
