"""
Twisha Santra, Hayley Yoshikawa
CSE 163
This program conducts statistical testing on the Spotify
Global Trends dataset in an attempt to answer our various
research questions.
"""

import eda
import result_visualization
import pandas as pd
from scipy import stats


def stat_test_rq1(cleaned_spot_data: pd.DataFrame):
    """
    Given the cleaned Spotify Global Trends data, conducts the
    Kruskal-Wallis statistical test on quantitative rq1 variables of
    interest and the Chi-Squared Independence test on categorical
    variables. None is returned.
    """
    dependent_variables = ["viral_score", "streams", "stream_change"]

    for dv in dependent_variables:
        print(f" -- Kruskal-Wallis Test for {dv} by Genre -- ")
        genre_groups = cleaned_spot_data.groupby("genre")[dv]
        print()
        groups_for_stat_test = []
        for genre, data in genre_groups:
            groups_for_stat_test.append(data)
        h_stat, p_val = stats.kruskal(*groups_for_stat_test)
        print(f"The Kruskal-Wallis H statistic is {h_stat}")
        print(f"The p-value is {p_val}")

        if p_val < 0.05:
            print("We can reject the null hypothesis!")
        else:
            print("We fail to reject the null hypothesis.")

        print("-----------------------------------------------")

    crosstab = pd.crosstab(cleaned_spot_data["genre"],
                           cleaned_spot_data["longevity"])
    cs_stat, cs_p_val, dof, exp_freq = stats.chi2_contingency(crosstab)
    print(" -- Chi-Square Test of Independence for longevity by Genre")
    print()

    print(f"The Chi-Squared statistic is {cs_stat}")
    print(f"The p-value is {cs_p_val}")
    if cs_p_val < 0.05:
        print("We can reject the null hypothesis!")
    else:
        print("We fail to reject the null hypothesis.")

    # Checking Sample Size Assumption
    if exp_freq.min() < 5:
        print("Warning: some expected frequencies are below 5.")
    print("-----------------------------------------------")


def stat_test_rq2(filtered_artists: pd.DataFrame,
                  cleaned_spot_data: pd.DataFrame) -> None:
    """
    Given the cleaned Spotify Global Trends data and the filtered
    dataset that contains artists with at least two viral songs, conducts
    the Kruskal-Wallis statistical test on quantitative rq2 variables of
    interest and the Chi-Squared Independence test on categorical
    variables. None is returned.
    """
    merged = filtered_artists.merge(cleaned_spot_data,
                                    left_on="artist_name",
                                    right_on="artist_name")
    artists = merged.groupby("artist_name")["viral_score"]
    artist_groups = []
    for artist, data in artists:
        artist_groups.append(data)
    h_stat, p_val = stats.kruskal(*artist_groups)
    print(" -- Kruskal-Wallis Test for viral_score by Artist Name -- ")
    print()

    print(f"The Kruskal-Wallis H statistic is {h_stat}")
    print(f"The p-value is {p_val}")

    if p_val < 0.05:
        print("We can reject the null hypothesis!")
    else:
        print("We fail to reject the null hypothesis.")
    print()

    # Statistical Test for Categorical Variables
    crosstab = pd.crosstab(merged["artist_name"],
                           merged["popularity_category"])
    cs_stat, cs_p_val, dof, exp_freq = stats.chi2_contingency(crosstab)
    print(" -- Chi-Square Test of Independence for popularity_category "
          "by Artist Name-- ")
    print()

    print(f"The Chi-Squared statistic is {cs_stat}")
    print(f"The p-value is {cs_p_val}")
    if cs_p_val < 0.05:
        print("We can reject the null hypothesis!")
    else:
        print("We fail to reject the null hypothesis.")

    # Checking Sample Size Assumption
    if exp_freq.min() < 5:
        print("Warning: some expected frequencies are below 5.")
    print("-----------------------------------------------")


def stat_test_rq3(cleaned_spot_data: pd.DataFrame) -> None:
    """
    Given the cleaned Spotify Global Trends data, conducts the
    Kruskal-Wallis statistical test on quantitative rq3 variables of
    interest and the Chi-Squared Independence test on categorical
    variables. None is returned.
    """
    dependent_variables = ["days", "pos"]

    for dv in dependent_variables:
        print(f" -- Kruskal-Wallis Test for {dv} by Country -- ")
        genre_groups = cleaned_spot_data.groupby("country")[dv]
        print()
        groups_for_stat_test = []
        for country, data in genre_groups:
            groups_for_stat_test.append(data)
        h_stat, p_val = stats.kruskal(*groups_for_stat_test)
        print(f"The Kruskal-Wallis H statistic is {h_stat}")
        print(f"The p-value is {p_val}")

        if p_val < 0.05:
            print("We can reject the null hypothesis!")
        else:
            print("We fail to reject the null hypothesis.")

        print("-----------------------------------------------")

    # Statistical Test for Categorical Variables
    crosstab = pd.crosstab(cleaned_spot_data["country"],
                           cleaned_spot_data["longevity"])
    cs_stat, cs_p_val, dof, exp_freq = stats.chi2_contingency(crosstab)
    print(" -- Chi-Square Test of Independence for longevity by Country")
    print()

    print(f"The Chi-Squared statistic is {cs_stat}")
    print(f"The p-value is {cs_p_val}")
    if cs_p_val < 0.05:
        print("We can reject the null hypothesis!")
    else:
        print("We fail to reject the null hypothesis.")

    # Checking Sample Size Assumption
    if exp_freq.min() < 5:
        print("Warning: some expected frequencies are below 5.")
    print("-----------------------------------------------")


def main():
    spot_data = pd.read_csv(eda.FILE_PATH)

    # Categorical Variables of Interest
    categorical_variables = ["track_name", "artist_name", "genre", "country",
                             "trend", "popularity_category", "longevity"]

    output = eda.unique_values_categorical(spot_data, categorical_variables)

    # Clean Data
    cleaned_spot_data = eda.clean_data(spot_data, output)

    # Statistical Testing
    print(" ~~~ Statistical Test for Research Question 1 ~~~ ")
    print()
    stat_test_rq1(cleaned_spot_data)
    print("-----------------------------------------------")

    print(" ~~~ Statistical Testing for Research Question 2 ~~~ ")
    print()
    filtered_artists = result_visualization.virality_score_by_artist(
            cleaned_spot_data)
    stat_test_rq2(filtered_artists, cleaned_spot_data)
    print("-----------------------------------------------")

    print(" ~~~ Statistical Testing for Research Question 3 ~~~ ")
    print()
    stat_test_rq3(cleaned_spot_data)
    print("-----------------------------------------------")


if __name__ == '__main__':
    main()
