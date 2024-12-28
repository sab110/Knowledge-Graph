# Knowledge Graph Construction Using AI

This repository demonstrates the construction of a knowledge graph using AI techniques, including the use of Convolutional Neural Networks (CNNs) for text classification. The project incorporates data preprocessing, knowledge graph schema design, and performance comparison of six CNN variations.

## Features

- **Data Loading and Preprocessing**:

  - Loads SDG indicator data from JSON5 files.
  - Verifies and inspects data structure.
- **Knowledge Graph Schema**:

  - Extracts nodes and relationships based on attributes such as `geoAreaName`, `indicator`, `timePeriodStart`, `value`, and `units`.
- **CNN Models for Text Classification**:

  - Implements six variations of CNN architectures.
  - Each variation explores different combinations of layers, filters, and regularization techniques.
- **Performance Metrics**:

  - Evaluates CNN models using accuracy and F1-score.
  - Visualizes results to compare the effectiveness of each model variation.

## Project Structure

- `data/`: Directory containing the SDG indicator JSON5 files.
- `knowledge_graph_construction.ipynb`: Jupyter notebook implementing the knowledge graph and CNN variations.
- `README.md`: Documentation (this file).

## Getting Started

### Prerequisites

- Python 3.8 or later
- Required libraries:
  - `tensorflow`
  - `sklearn`
  - `json5`
  - `matplotlib`
  - `numpy`
  - `pandas`

Install dependencies with:

```bash
pip install -r requirements.txt
```

### Usage

1. **Prepare the Data** :

* Place JSON5 files in the `data/` directory.

1. **Run the Notebook** :

* Open `knowledge_graph_construction.ipynb` in Jupyter Notebook or Jupyter Lab.
* Follow the cells to:
  * Load and preprocess data.
  * Construct the knowledge graph.
  * Train and evaluate CNN variations.

1. **Visualize Results** :

* The notebook generates plots to compare accuracy and F1-score across CNN variations.

## CNN Variations

* **Variation 1** : Basic CNN with one Conv1D and GlobalMaxPooling1D layer.
* **Variation 2** : Adds extra Conv1D and MaxPooling layers for feature extraction.
* **Variation 3** : Introduces Dropout layers for regularization.
* **Variation 4** : Increases the number of filters in Conv1D layers.
* **Variation 5** : Deepens the architecture by stacking multiple Conv1D layers.
* **Variation 6** : Combines depth and Dropout layers for balanced regularization.

## Evaluation

* **Metrics** :
* Accuracy: Measures overall prediction correctness.
* F1-score: Balances precision and recall, particularly useful for imbalanced datasets.
* **Insights** :
* Variations 1 and 2 achieve strong overall performance.
* Variation 5 exhibits the best F1-score.
* Variation 6 requires further optimization to handle imbalanced data effectively.

## Visualization

A performance comparison plot is generated to visualize the accuracy and F1-score for all CNN variations. This aids in selecting the best-performing model for deployment.

## Future Work

* Enhance data preprocessing to handle noisy or incomplete datasets.
* Explore additional deep learning architectures, such as RNNs or transformers.
* Optimize CNN variations for better handling of imbalanced datasets.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments

Special thanks to contributors and the open-source community for their support and resources.

```
This `README.md` provides a comprehensive overview of the project, its objectives, features, and usage instructions. Let me know if you need additional details or modifications!
```
