"""
Twisha Santra, Hayley Yoshikawa
CSE 163
This program generates visualizations for the Spotify Global
Trends dataset using Seaborns and Matplotlib.
"""

import eda
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()


def viral_genre_plot(spot_data: pd.DataFrame) -> None:
    """
    Given cleaned Spotify Global Trends data, this function
    plots and displays a bar plot of average viral scores
    by genre. None is returned.
    """
    sns.catplot(
        data=spot_data,
        x="genre",
        y="viral_score",
        hue="genre",
        kind="bar",
        aspect=4.5
    )

    plt.xlabel("Genre")
    plt.ylabel("Average Viral Score")
    plt.title("Average Viral Score by Genre")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.show()


def virality_score_by_artist(spot_data: pd.DataFrame) -> pd.DataFrame:
    """
    Given cleaned Spotify Global Trends data, this function plots
    and shows a box plot of viral scores by artist. To be
    considered, the artist at hand must appear more
    than once in the dataset. A DataFrame of the filtered
    artists are returned.
    """
    artist_counts = spot_data["artist_name"].value_counts().reset_index()

    # Artists with more than 1 viral song
    multiple_appearances = artist_counts[artist_counts["count"] > 1]
    filtered = spot_data.merge(multiple_appearances,
                               left_on="artist_name",
                               right_on="artist_name")

    sns.catplot(x="artist_name",
                y="viral_score",
                kind="box",
                hue="artist_name",
                data=filtered,
                aspect=3)
    plt.xlabel("Artist Name")
    plt.ylabel("Viral Score")
    plt.title("Viral Score By Artist")
    plt.xticks(rotation=55)

    plt.show()

    filtered = filtered[["artist_name"]]
    return filtered


def country_viral_run_plot(cleaned_spot_data: pd.DataFrame) -> None:
    """
    Given cleaned Spotify Global Trends data, this function plots
    and shows a heat map of countries in the data set against the
    different longevity values. Each box is shaded based on the
    average trending days of the songs within the intersection of
    a country and a longevity category. None is returned.
    """
    country_pop_songs = (
        cleaned_spot_data
        .groupby(["country", "longevity"])["days"]
        .mean()
        .reset_index()
        .pivot(index="country", columns="longevity", values="days")
    )

    fig, ax = plt.subplots()
    sns.heatmap(country_pop_songs, annot=True, cmap="gnuplot",
                fmt="0.1f", linewidths=.5, ax=ax)
    ax.set_title("Average Days Trending by Country and Longevity")
    plt.show()


def main():
    spot_data = pd.read_csv(eda.FILE_PATH)

    # Categorical Variables of Interest
    categorical_variables = ["track_name", "artist_name", "genre", "country",
                             "trend", "popularity_category", "longevity"]

    output = eda.unique_values_categorical(spot_data, categorical_variables)

    # Clean Data
    cleaned_spot_data = eda.clean_data(spot_data, output)

    # Visualization 1
    viral_genre_plot(cleaned_spot_data)

    # Visualization 2
    virality_score_by_artist(cleaned_spot_data)

    # Visualization 3
    country_viral_run_plot(cleaned_spot_data)

    # Verifying Assumptions for ANOVA Test
    # Research Questions 1 & 2
    # Histogram of viral_score
    sns.histplot(cleaned_spot_data["viral_score"])
    plt.xlabel("Viral Score")
    plt.ylabel("Frequency")
    plt.title("Distibution of Viral Score")
    plt.show()
    print()

    # Research Question 3
    # Histogram of days
    sns.histplot(cleaned_spot_data["days"])
    plt.xlabel("Days Trending")
    plt.ylabel("Frequency")
    plt.title("Distibution of Days Trending")
    plt.show()


if __name__ == '__main__':
    main()
