"""Unit tests for the PromptManager class.

This module contains tests that verify the functionality of the PromptManager class,
including template loading, parameter extraction, prompt rendering, and error handling.
"""

import pytest

from src.prompts.prompt_manager import PromptManager


def test_prompt_manager_initialization():
    """Test PromptManager initialization with default templates directory.

    Verifies that:
        - Manager is instantiated correctly
        - Default templates directory exists and is valid
        - Test template is loaded successfully
    """
    manager = PromptManager()
    assert isinstance(manager, PromptManager)
    assert manager.templates_dir.exists()
    assert manager.templates_dir.is_dir()
    assert "test_prompt" in manager.templates


def test_get_available_prompts():
    """Test retrieval of available prompt templates.

    Verifies that:
        - All templates are listed
        - List is sorted alphabetically
        - Known test template is included
    """
    manager = PromptManager()
    templates = manager.get_available_prompts()
    assert isinstance(templates, list)
    assert "test_prompt" in templates
    assert templates == sorted(templates)  # Verify alphabetical sorting


def test_list_parameters():
    """Test parameter extraction from test prompt.

    Verifies that:
        - All required parameters are extracted
        - Parameters are returned in sorted order
        - No duplicate parameters are included
    """
    manager = PromptManager()
    params = manager.list_parameters("test_prompt")
    assert sorted(params) == sorted(["name", "project_name", "role"])


def test_render_prompt_success():
    """Test successful prompt rendering with valid parameters.

    Verifies that:
        - Template renders correctly with valid parameters
        - All parameter values are included in output
        - Output contains expected text fragments
    """
    manager = PromptManager()
    rendered = manager.render_prompt(
        "test_prompt", name="Alice", project_name="Test Project", role="Developer"
    )
    assert "Hello Alice!" in rendered
    assert "Welcome to Test Project" in rendered
    assert "Your assigned role is: Developer" in rendered


def test_render_prompt_invalid_template_name_type():
    """Test prompt rendering fails with invalid template name type.

    Verifies that:
        - TypeError is raised for non-string template names
        - Error message includes the invalid type
    """
    manager = PromptManager()
    with pytest.raises(TypeError) as exc_info:
        manager.render_prompt(123)  # Pass integer instead of string
    assert "must be a string" in str(exc_info.value)


def test_render_prompt_empty_template_name():
    """Test prompt rendering fails with empty template name.

    Verifies that:
        - ValueError is raised for empty template name
        - Error message indicates empty name issue
    """
    manager = PromptManager()
    with pytest.raises(ValueError) as exc_info:
        manager.render_prompt("")
    assert "cannot be empty" in str(exc_info.value)


def test_render_prompt_missing_params():
    """Test prompt rendering fails with missing parameters.

    Verifies that:
        - ValueError is raised when required parameters are missing
        - Error message includes name of missing parameter
    """
    manager = PromptManager()
    with pytest.raises(ValueError) as exc_info:
        manager.render_prompt(
            "test_prompt", name="Alice"
        )  # Missing project_name and role
    error_msg = str(exc_info.value).lower()
    assert "project_name" in error_msg  # Checks for the missing parameter name


def test_render_prompt_invalid_template():
    """Test prompt rendering fails with invalid template name.

    Verifies that:
        - KeyError is raised for non-existent template
        - Error message indicates template not found
    """
    manager = PromptManager()
    with pytest.raises(KeyError) as exc_info:
        manager.render_prompt("nonexistent_template")
    assert "not found" in str(exc_info.value)
