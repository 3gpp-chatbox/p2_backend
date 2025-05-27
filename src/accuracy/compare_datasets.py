from sentence_transformers import SentenceTransformer

from src.accuracy.sbert_simple import compare_two_datasets
from src.schemas.procedure_graph import Graph


def compare_datasets(
    target_dataset: Graph,
    comparison_datasets: list[Graph],
    procedure_name: str,
    model: SentenceTransformer,
    fixed_threshold: float = 0.8,
) -> float:
    """Compare a target dataset against multiple comparison datasets and compute average accuracy.

    This function compares a target dataset against multiple comparison datasets using
    `compare_two_datasets`. It calculates the average accuracy across all comparisons,
    providing a single overall accuracy score. This is useful when you want to assess
    how well a reference dataset aligns with multiple variations.

    Args:
        target_dataset (Graph): The reference dataset to compare against others.
        comparison_datasets (list[Graph]): List of datasets to compare against the target.
        procedure_name (str): Name of the procedure used in comparisons.
        model (SentenceTransformer, optional): Pre-initialized SBERT model for computing embeddings.
            Defaults to module-level model.
        fixed_threshold (float, optional): Threshold value for comparisons. Defaults to 0.8.

    Returns:
        float: The average accuracy score across all comparisons.

    Raises:
        ValueError: If no comparison datasets are provided.

    Example:
        >>> main_result = Graph(...)  # Your reference/main extraction
        >>> variations = [modified_result, alt_result]  # Other extractions
        >>> accuracy = compare_datasets(main_result, variations, "ExtractionProcedure")
        >>> print(f"Average accuracy: {accuracy}")
    """
    if not comparison_datasets:
        raise ValueError("Provide at least one comparison dataset.")

    total_accuracy = 0.0

    # Compare target against each comparison dataset
    for i, comparison_dataset in enumerate(comparison_datasets):
        accuracy_result = compare_two_datasets(
            dataset_1=target_dataset,
            dataset_2=comparison_dataset,
            dataset_1_name=f"{procedure_name}",
            dataset_2_name=f"{procedure_name}",
            model=model,
            fixed_threshold=fixed_threshold,
        )
        comparison_accuracy = accuracy_result["summary"]["overall_match_percentage"]
        total_accuracy += comparison_accuracy

    overall_accuracy = (
        total_accuracy / len(comparison_datasets) if comparison_datasets else 0.0
    )

    return round(overall_accuracy, 2)
