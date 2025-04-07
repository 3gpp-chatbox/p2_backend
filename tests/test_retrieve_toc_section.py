import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1].resolve()))
from src.retrieval.toc_retrieval import (
    find_procedure_section_lines,
    get_top_level_sections,
)


@pytest.fixture
def sample_toc_data():
    """
    Fixture that provides sample TOC data for testing.
    """
    return [
        "5.5.1.2 Registration procedure for initial registration",
        "5.5.1.2.1 General",
        "5.5.1.2.2 Initial registration initiation",
        "5.5.1.2.3 5GMM common procedure initiation",
        "5.5.1.2.4 Initial registration accepted by the network",
    ]


def test_find_procedure_section_lines(sample_toc_data):
    procedure_name = "initial registration"
    matches = find_procedure_section_lines(sample_toc_data, procedure_name)
    assert matches == [
        "5.5.1.2 Registration procedure for initial registration",
        "5.5.1.2.2 Initial registration initiation",
        "5.5.1.2.4 Initial registration accepted by the network",
    ]


def test_get_top_level_sections(sample_toc_data):
    top_sections = get_top_level_sections(sample_toc_data)
    assert top_sections == ["5.5.1.2"]
