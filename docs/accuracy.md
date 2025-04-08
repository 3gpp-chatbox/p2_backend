Joona suggested evaluating the number of nodes from various runs without any changes in the prompt to validate consistency.

Wenbo suggested picking one of the results as a ground truth and evaluate others against it to determine the accuracy.

---

## Stability Across Runs

Idea: If the LLM extracts the same state machine consistently, it’s more likely to be reliable.

Approach:
Run the extraction multiple times (e.g., 3-5 runs) on the same document with slight prompt variations or random seeds.

Compare the outputs:
Node Stability: Percentage of nodes appearing in all runs.

Edge Stability: Percentage of edges appearing in all runs.

Formula: Stability = (Elements consistent across runs) / (Total unique elements across runs).

This tests the LLM’s robustness without needing a reference.

_example:_

Let’s walk through how the "Stability Across Runs" metric would work in practice by setting up a concrete scenario. I’ll simulate a small state machine extraction task, run it multiple times, and show you how to calculate the stability metrics step-by-step. This will give you a clear picture of what the numbers look like and how to interpret them.

### Scenario Setup

Imagine you’re extracting a state machine from a short document describing a simple process, like a coffee-making workflow. The document might say:

- "Start by turning on the coffee machine. Then add water. Next, insert a coffee pod. Finally, press the brew button to finish."

Your LLM is tasked with extracting nodes (states) and edges (transitions) from this text. Since LLMs can be inconsistent, we’ll simulate three runs with slight variations (e.g., due to prompt tweaks or randomness).

#### Simulated Extraction Runs

- **Run 1**:

  - Nodes: {Start, Add Water, Insert Pod, Brew, Finish}
  - Edges: {Start → Add Water, Add Water → Insert Pod, Insert Pod → Brew, Brew → Finish}

- **Run 2**:

  - Nodes: {Start, Add Water, Insert Coffee, Brew, Done}
  - Edges: {Start → Add Water, Add Water → Insert Coffee, Insert Coffee → Brew, Brew → Done}

- **Run 3**:
  - Nodes: {Start, Add Water, Insert Pod, Press Brew, Finish}
  - Edges: {Start → Add Water, Add Water → Insert Pod, Insert Pod → Press Brew, Press Brew → Finish}

Notice the variations: "Insert Pod" vs. "Insert Coffee," "Brew" vs. "Press Brew," "Finish" vs. "Done." These mimic how an LLM might interpret the same text differently across runs.

### Step 1: Identify Consistent Elements

- **Nodes Consistent Across All Runs**:

  - Look for nodes present in all three outputs:
    - Run 1: {Start, Add Water, Insert Pod, Brew, Finish}
    - Run 2: {Start, Add Water, Insert Coffee, Brew, Done}
    - Run 3: {Start, Add Water, Insert Pod, Press Brew, Finish}
  - Consistent nodes: {Start, Add Water} (only these two appear in all runs with exact matches).
  - Note: "Insert Pod" and "Insert Coffee" might be semantically similar, but for stability, we count exact matches unless you preprocess to normalize them.

- **Edges Consistent Across All Runs**:
  - Run 1: {Start → Add Water, Add Water → Insert Pod, Insert Pod → Brew, Brew → Finish}
  - Run 2: {Start → Add Water, Add Water → Insert Coffee, Insert Coffee → Brew, Brew → Done}
  - Run 3: {Start → Add Water, Add Water → Insert Pod, Insert Pod → Press Brew, Press Brew → Finish}
  - Consistent edges: {Start → Add Water} (only this transition is identical across all runs).

### Step 2: Count Total Unique Elements

- **Total Unique Nodes**:

  - Combine all nodes across runs, removing duplicates:
    - {Start, Add Water, Insert Pod, Insert Coffee, Brew, Press Brew, Finish, Done}
  - Total: 8 unique nodes.

- **Total Unique Edges**:
  - Combine all edges across runs:
    - {Start → Add Water, Add Water → Insert Pod, Add Water → Insert Coffee, Insert Pod → Brew, Insert Coffee → Brew, Insert Pod → Press Brew, Brew → Finish, Brew → Done, Press Brew → Finish}
  - Total: 9 unique edges.

### Step 3: Calculate Stability

- **Node Stability**:

  - Formula: _Node Stability = (Nodes consistent across runs) / (Total unique nodes)_
  - Calculation: _2 / 8 = 0.25_ (25%)
  - Interpretation: Only 25% of the nodes are consistently extracted across all runs.

- **Edge Stability**:

  - Formula: _Edge Stability = (Edges consistent across runs) / (Total unique edges)_
  - Calculation: _1 / 9 = 0.111_ (11.1%)
  - Interpretation: Only 11.1% of the edges are consistently extracted.

- **Overall Stability**:
  - Formula: _Stability = (Consistent elements) / (Total unique elements)_
  - Total consistent elements (nodes + edges): 2 + 1 = 3
  - Total unique elements: 8 + 9 = 17
  - Calculation: _3 / 17 = 0.176_ (17.6%)
  - Interpretation: The overall stability of the extraction is 17.6%, suggesting the LLM is quite inconsistent.

### What This Looks Like in Practice

- **Metric Output**:
  - Node Stability: 25%
  - Edge Stability: 11.1%
  - Overall Stability: 17.6%
- **Insight**: These low scores indicate the LLM struggles to produce the same state machine reliably. You might see:
  - Different wording (e.g., "Insert Pod" vs. "Insert Coffee").
  - Structural variation (e.g., "Brew" vs. "Press Brew" as separate states).

### Tweaking the Scenario

If you preprocess to normalize similar terms (e.g., treat "Insert Pod" and "Insert Coffee" as the same node), stability improves:

- **Adjusted Consistent Nodes**: {Start, Add Water, Insert Pod/Insert Coffee, Brew/Press Brew, Finish/Done} → 5 consistent nodes.
- **Adjusted Node Stability**: _5 / 8 = 0.625_ (62.5%).
- **Adjusted Edges**: More edges might align (e.g., "Insert Pod → Brew" and "Insert Coffee → Brew"), bumping edge stability too.

### How to Use This

- **Threshold**: You could set a target (e.g., 70% stability) and tweak your LLM prompts or extraction logic until you hit it.
- **Automation**: Write a script to:
  1. Run the LLM 3-5 times.
  2. Compare node/edge sets (exact match or with normalization).
  3. Output the stability percentages.
