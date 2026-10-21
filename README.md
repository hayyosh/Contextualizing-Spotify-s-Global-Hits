# Spotify Global Trend Analysis

Python analysis of 178 trending Spotify tracks: statistical tests on genre, artist, and country vs. virality, plus an SVM model predicting song longevity.

Completed for *Intermediate Data Programming* at the University of Washington, with Twisha Santra.

**[Read the full report (PDF)](report.pdf)**

## Project Overview
This project analyzes the Spotify Global Trends dataset to explore how genre, artist consistency, and country of origin relate to virality and viral duration across 178 trending tracks.

## Key Findings
- Kruskal-Wallis and chi-squared tests indicate that genre, rather than virality, drives streaming momentum.
- A linear SVM (scikit-learn) trained on genre, viral score, and stream change classifies song longevity with 82% accuracy on a held-out 20% test set.

## Dataset
`spotify_global_trends.csv` (178 trending tracks) is included in this repo. It was originally obtained from Kaggle, but the original listing is no longer available.

## Installation
Requires Python 3. Install the dependencies:

```
pip install pandas matplotlib seaborn scikit-learn scipy
```

## Files
- `eda.py`: Exploratory data analysis, including unique values for categorical variables and a seven-number summary for quantitative variables. Cleans the data based on any inconsistencies found.
- `eda_testing.py`: Tests for the EDA and the filtering strategies used in our plots.
- `statistical_testing.py`: Statistical tests on the cleaned data.
- `result_visualization.py`: Visualizations built with Seaborn and Matplotlib.
- `machine_learning.py`: Trains and evaluates the SVM model on the cleaned data.
- `spotify_global_trends.csv`: Data file.
- `report.pdf`: Full written report.

## How to Run
1. Clone or download this repository.
2. In a terminal, navigate to the project directory: `cd path/to/project`
3. Run the scripts in this order:

```
python eda.py
python result_visualization.py
python statistical_testing.py
python machine_learning.py
```

## Running Tests
To run the tests and verify the EDA and filtering results:
`python eda_testing.py`
