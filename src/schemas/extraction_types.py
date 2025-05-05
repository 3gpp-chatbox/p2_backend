"""
This module defines the data structures and enums used in the procedure extraction process.

The module provides three main components:
1. ExtractionMethod: Enum defining valid extraction methods
   - MAIN: Primary extraction using main model
   - MODIFIED: Uses modified prompts with main model
   - ALTERNATIVE: Uses alternative model
   - ALTERNATIVE_2: Maps to "alternative" in database, used when specified in config

2. ExtractionResult: Container for a single extraction result
   - Holds the graph, accuracy score, model info, and method
   - Used to track individual extraction attempts

3. ExtractionResults: Container managing multiple extraction results
   - Stores results from different methods (main, modified, alternative)
   - Provides logic for selecting best result based on accuracy and method priority
   - Handles special case when ALTERNATIVE_MODEL_2 is used

Note: When ALTERNATIVE_MODEL_2 is configured, it replaces the modified approach
and its results are stored as "alternative" in the database for compatibility.
The method selection prioritizes main > modified > alternative when accuracies are equal.
"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from src.schemas.procedure_graph import Graph


class ExtractionMethod(Enum):
    """
    Enumeration of possible extraction methods.

    Values:
        MAIN: Primary extraction method using the main model with standard prompts
        MODIFIED: Alternative approach using modified prompts with the main model
        ALTERNATIVE: Secondary extraction using the alternative model
        ALTERNATIVE_2: Special case that maps to "alternative" in database,
                      used when ALTERNATIVE_MODEL_2 is configured

    Note:
        ALTERNATIVE_2 intentionally has the same value as ALTERNATIVE ("alternative")
        to ensure database compatibility while maintaining distinct method tracking
        in the extraction process.
    """

    MAIN = "main"
    MODIFIED = "modified"
    ALTERNATIVE = "alternative"
    ALTERNATIVE_2 = "alternative"


class ExtractionResult(BaseModel):
    """
    Data structure to hold an extraction result and its metadata.

    Attributes:
        graph: The extracted procedure graph
        accuracy: Comparison score against other extractions (0.0 to 100.0)
        model_name: Name of the model used for this extraction
        method: ExtractionMethod enum indicating which approach was used

    The accuracy score is initially set to 0.0 and is updated later when
    comparing this extraction against others during the validation phase.
    """

    graph: Graph
    accuracy: float = Field(ge=0.0, le=100.0)
    model_name: str
    method: ExtractionMethod


class ExtractionResults(BaseModel):
    """
    Container for all extraction results from different methods.

    Attributes:
        main: Result from main model with standard prompts
        modified: Result from main model with modified prompts
                 (None when ALTERNATIVE_MODEL_2 is used)
        alternative: Result from alternative model
        alternative_2: Result from ALTERNATIVE_MODEL_2 when configured
                      (identical to alternative in this case)

    This container handles both standard extraction flows and the special case
    when ALTERNATIVE_MODEL_2 is configured. In the latter case, modified is None
    and alternative holds the ALTERNATIVE_MODEL_2 results.
    """

    main: Optional[ExtractionResult] = None
    modified: Optional[ExtractionResult] = None
    alternative: Optional[ExtractionResult] = None
    alternative_2: Optional[ExtractionResult] = None

    def get_best_result(self) -> ExtractionResult:
        """
        Determine the best extraction result based on accuracy scores and method priority.

        The selection process uses a two-tier sorting system:
        1. Primary sort: Highest accuracy score
        2. Secondary sort: Method priority when accuracies are equal
           - Priority 1: Main extraction (standard approach)
           - Priority 2: Modified extraction (when not using ALTERNATIVE_MODEL_2)
           - Priority 3: Alternative_2 (treated same as alternative in DB)
           - Priority 4: Alternative model

        In the case where ALTERNATIVE_MODEL_2 is used:
        - The modified slot will be None
        - Alternative and alternative_2 slots contain the same result
        - The result is stored as "alternative" in the database

        Returns:
            ExtractionResult: The extraction with highest accuracy, considering method
                            priority when accuracies are equal.

        Raises:
            ValueError: If no results are available in any slot.
        """
        if not any([self.main, self.modified, self.alternative, self.alternative_2]):
            raise ValueError("No extraction results available")

        # Create a list of tuples (result, priority) for non-None results
        results = []
        if self.main:
            results.append((self.main, 1))  # Highest priority - standard approach
        if self.modified:
            results.append((self.modified, 2))  # Second priority when available
        if self.alternative_2:
            results.append((self.alternative_2, 3))  # Third priority
        if self.alternative:
            results.append((self.alternative, 4))  # Lowest priority

        # Sort by accuracy (descending) and priority (ascending)
        sorted_results = sorted(results, key=lambda x: (-x[0].accuracy, x[1]))

        return sorted_results[0][0]
