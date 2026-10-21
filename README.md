# Spotify Global Trend Analysis

Python analysis of 178 trending Spotify tracks: statistical tests on genre, artist, and country vs. virality, plus an SVM model predicting song longevity.

Completed for *Intermediate Data Programming* at the University of Washington.

## Project Overview
This project analyzes the Spotify Global Trends dataset to explore how genre, artist consistency, and country of origin relate to virality and viral duration across 178 trending tracks.

## Key Findings
- Kruskal-Wallis and chi-squared tests indicate that genre, rather than virality, drives streaming momentum.
- An SVM classifier (scikit-learn) predicts song longevity and stream change with 82% accuracy on [held-out test data].

## Dataset
`spotify_global_trends.csv` (178 trending tracks) is included in this repo. It was originally obtained from Kaggle, but the original listing is no longer available. Place it in the project's root directory before running any code.

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

## How to Run
1. Clone or download this repository.
2. Place `spotify_global_trends.csv` in the root project directory.
3. In a terminal, navigate to the project directory: `cd path/to/project`
4. Run the scripts in this order:

```
python eda.py
python result_visualization.py
python statistical_testing.py
python machine_learning.py
```

## Running Tests
To run the tests and verify the EDA and filtering results:
`python eda_testing.py`
