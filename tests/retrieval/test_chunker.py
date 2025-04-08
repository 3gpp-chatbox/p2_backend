"""Unit tests for document parser's extract_chunks function."""

from pathlib import Path

import pytest

from src.retrieval.chunker import extract_chunks


@pytest.fixture
def sample_markdown_file(tmp_path) -> Path:
    """Create a sample markdown file for testing.

    Args:
        tmp_path: pytest fixture that provides a temporary directory unique to each test

    Returns:
        Path: Path object pointing to the created markdown file
    """
    content = """# First Heading
This is content under first heading.

## Second Heading
This is content under second heading.
With multiple lines.

# Third Heading
Final content section."""

    file_path = tmp_path / "test-document.md"
    file_path.write_text(content)
    return file_path


# Test successful extraction
def test_extract_chunks_successful(sample_markdown_file: Path) -> None:
    """Test successful extraction of chunks from a markdown file."""
    # Act
    result = extract_chunks(sample_markdown_file)

    # Assert
    assert isinstance(
        result, dict
    )  # ExtractedDocument is a TypedDict, check if it's a dict
    assert set(result.keys()) == {"doc_name", "chunks"}  # Verify structure
    assert result["doc_name"] == "test"
    assert len(result["chunks"]) == 3

    # Verify first chunk
    assert result["chunks"][0]["heading"] == "First Heading"
    assert result["chunks"][0]["level"] == 1
    assert "content under first heading" in result["chunks"][0]["content"]

    # Verify nested chunk
    assert result["chunks"][1]["heading"] == "Second Heading"
    assert result["chunks"][1]["level"] == 2
    assert "multiple lines" in result["chunks"][1]["content"]


# Test empty file
def test_extract_chunks_empty_file(tmp_path: Path) -> None:
    """Test extraction from an empty markdown file."""
    # Arrange
    empty_file = tmp_path / "empty-doc.md"
    empty_file.write_text("")

    # Act
    result = extract_chunks(empty_file)

    # Assert
    assert isinstance(
        result, dict
    )  # ExtractedDocument is a TypedDict, check if it's a dict
    assert set(result.keys()) == {"doc_name", "chunks"}  # Verify structure
    assert result["doc_name"] == "empty"
    assert len(result["chunks"]) == 0


# Test file not found
def test_extract_chunks_file_not_found() -> None:
    """Test handling of non-existent file."""
    # Act & Assert
    with pytest.raises(FileNotFoundError) as exc:
        extract_chunks("nonexistent-file.md")
    assert "File not found" in str(exc.value)


# Test directory path
def test_extract_chunks_directory_path(tmp_path: Path) -> None:
    """Test handling of directory path instead of file."""
    # Act & Assert
    with pytest.raises(ValueError) as exc:
        extract_chunks(tmp_path)
    assert "Path is not a file" in str(exc.value)


# Test string path input
def test_extract_chunks_string_path(sample_markdown_file: Path) -> None:
    """Test extraction using string path input."""
    # Act
    result = extract_chunks(str(sample_markdown_file))

    # Assert
    assert isinstance(
        result, dict
    )  # ExtractedDocument is a TypedDict, check if it's a dict
    assert set(result.keys()) == {"doc_name", "chunks"}  # Verify structure
    assert len(result["chunks"]) == 3


# Test markdown without headings
def test_extract_chunks_no_headings(tmp_path: Path) -> None:
    """Test extraction from markdown file without any headings."""
    # Arrange
    content = """This is just regular content.
No headings here.
Just plain text."""
    file_path = tmp_path / "no-headings-doc.md"
    file_path.write_text(content)

    # Act
    result = extract_chunks(file_path)

    # Assert
    assert isinstance(
        result, dict
    )  # ExtractedDocument is a TypedDict, check if it's a dict
    assert set(result.keys()) == {"doc_name", "chunks"}  # Verify structure
    assert result["doc_name"] == "no"
    assert len(result["chunks"]) == 0


def test_extract_chunks_io_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test handling of IO errors during file reading."""

    # Arrange
    def mock_read_text(*args, **kwargs):
        raise IOError("Simulated IO error")

    file_path = tmp_path / "error-doc.md"
    file_path.touch()
    monkeypatch.setattr(Path, "read_text", mock_read_text)

    # Act & Assert
    with pytest.raises(IOError) as exc:
        extract_chunks(file_path)
    assert "Simulated IO error" in str(exc.value)
