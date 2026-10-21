"""
Twisha Santra, Hayley Yoshikawa
CSE 163
This program tests our exploratory data analysis on the Spotify
Global Trends dataset.
"""

import eda
import result_visualization
import pandas as pd

TEST_DATA = pd.DataFrame({
        "track_name": ["Opalite", "Homewrecker", "Yellow",
                       "Si Antes Te Hubiera Conocido", "12 to 12"],
        "artist_name": ["Taylor Swift", "sombr", "Coldplay",
                        "KAROL G", "sombr"],
        "genre": ["UK Garage", "Pop", "Country", "Pop", "Pop"],
        "country": ["US", "GB", "AU", "MX", "US"],
        "trend": ["Falling", "Falling", "Rising", "Falling", "Rising"],
        "popularity_category": ["Trending", "Average", "Trending",
                                "Average", "Trending"],
        "longevity": ["New", "Stable Hit", "Stable Hit", "New", "Stable Hit"],
        "viral_score": [1.5e7, 1.24e7, 2.98e7, 3.89e7, 0.9e7]
    })


def test_vars_cat() -> None:
    """
    Tests the unique_values_categorical() method
    """
    categorical_variables = ["track_name", "artist_name", "genre", "country",
                             "trend", "popularity_category", "longevity"]
    result = eda.unique_values_categorical(TEST_DATA, categorical_variables)
    assert len(result["track_name"]) == 5
    assert len(result["artist_name"]) == 4
    assert len(result["genre"]) == 3
    assert len(result["country"]) == 4
    assert len(result["trend"]) == 2
    assert len(result["popularity_category"]) == 2
    assert len(result["longevity"]) == 2
    print("All tests pass successfully :)")


def test_filtering_visualization2() -> None:
    """
    Tests the virality_score_by_artist() method
    """
    result = result_visualization.virality_score_by_artist(TEST_DATA)
    assert "sombr" in result["artist_name"].values
    assert "Taylor Swift" not in result["artist_name"].values
    assert "Coldplay" not in result["artist_name"].values
    assert "KAROL G" not in result["artist_name"].values
    print("All tests pass successfully :)")


def main():
    test_vars_cat()
    test_filtering_visualization2()


if __name__ == '__main__':
    main()
