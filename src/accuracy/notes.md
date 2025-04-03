ACCURACY METRICS CURRENTLY IMPLEMENTED:

1. Nodes and edges descriptions matching using SBERT 
    Semantic matching of node and edge descriptions
    Method: Uses cosine similarity between sentence embeddings
    Threshold: Uses a fixed threshold (default 0.7) to determine matches
    Output: Returns matched pairs and unmatched items
    

2. Dataset comparison using Jaccard similarity 
    Purpose: Compare the similarity between two datasets (v1 and v2, v1 and v3, v1 and v4, v2 and v3, v2 and v4, v3 and v4)
    Method: Uses Jaccard similarity between sets of nodes and edges
    Threshold: Uses a fixed threshold (default 0.7) to determine matches
    Output: Returns matched pairs and unmatched items

3. Majority voting technique to determine validity of the extracted data 
    Purpose: Determine the validity of the extracted data
    Method: Uses majority voting to determine the validity of the extracted data
    Threshold: Uses a fixed threshold (default 0.7) to determine matches
    Output: Returns the validity of the extracted data

4. Ground truth comparison with metrics (precision, recall, F1 score) 
    Purpose: Compare the extracted data with the ground truth data
    Method: Uses precision, recall, and F1 score to compare the extracted data with the ground truth data
    Threshold: Uses a fixed threshold (default 0.7) to determine matches
    Output: Returns the precision, recall, and F1 score of the extracted data

       
        1. Node and Edge Metrics (Precision, Recall, F1 Score):
        Precision = 1.0: This means that every node or edge that was identified as matching in the extracted data is indeed correct. There were no false positives.

        Recall = 1.0: This means that the extracted data captured all the relevant nodes and edges in the ground truth data. There were no false negatives, meaning no valid nodes or edges were missed.

        F1 Score = 1.0: This is the harmonic mean of precision and recall. An F1 score of 1.0 indicates perfect balance between precision and recall, confirming that the matching process for both nodes and edges was flawless.

        These results suggest that the matching between the data extracted from the different versions and the ground truth is accurate and complete at the node and edge level.

        2. Validity:
        Despite the perfect precision, recall, and F1 scores, the validity of the datasets (v2, v3, and v4) is flagged as invalid. This is due to unmatched nodes and edges exceeding a predefined threshold.

        3. Explanation of Invalid Validity:
        Unmatched Nodes Exceed the Threshold:

        For each version, the percentage of unmatched nodes is greater than the threshold of 5% (0.05), which leads to the invalid validity flag.

        v2: 38% unmatched nodes (0.38 > 0.05)

        v3: 31% unmatched nodes (0.31 > 0.05)

        v4: 19% unmatched nodes (0.19 > 0.05)

        Unmatched Edges Exceed the Threshold:

        Similarly, the percentage of unmatched edges also exceeds the threshold of 5% (0.05) for all versions.

        v2: 94% unmatched edges (0.94 > 0.05)

        v3: 53% unmatched edges (0.53 > 0.05)

        v4: 29% unmatched edges (0.29 > 0.05)

        4. Why is the Validity Flag Invalid?
        Even though the individual node and edge matches are perfect (precision, recall, F1), the unmatched nodes and edges are so significant that they exceed the defined threshold, causing the validity to be flagged as invalid.

        Thresholds for unmatched nodes and edges (set at 5%) serve as a measure of how well the extracted data corresponds to the ground truth in terms of completeness. In this case, there is a considerable mismatch, particularly with the edges, which is why the data is considered invalid for all versions.

        5. Possible Reasons for High Unmatched Nodes/Edges:
        Extraction Process Incompleteness: The extraction process may not be capturing all nodes or edges as required, potentially due to limitations in the algorithm, noise in the input data, or insufficient parsing of the specification.

        Threshold Setting: The threshold of 5% might be too strict. If the unmatched nodes/edges are relatively minor or inconsequential, you might consider adjusting the threshold to a higher value to accommodate minor discrepancies.

        Data Complexity: The data might be inherently complex or noisy, resulting in higher numbers of unmatched nodes or edges despite accurate matching at the surface level (as shown by the metrics).

        6. Next Steps:
        Adjust Thresholds: Consider increasing the threshold for unmatched nodes and edges to reduce the likelihood of invalidity flags if minor mismatches are acceptable in your context.

        Investigate Extraction Process: Review the extraction algorithms or methods to see if there's an issue in how certain nodes or edges are being missed. This could include revisiting the way data is parsed or improving the granularity of the extraction.

        Analyze Data for Patterns: Look at the types of nodes and edges that are unmatched and identify patterns or inconsistencies. There might be specific categories of data that are more prone to being missed or incorrectly matched.

        Revisit Ground Truth: If the ground truth data itself has some issues, it could be helpful to validate it and ensure it aligns well with the extracted datasets.