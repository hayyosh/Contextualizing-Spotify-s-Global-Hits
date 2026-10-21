"""
Twisha Santra, Hayley Yoshikawa
CSE 163
This program conducts exploratory data analysis on the Spotify
Global Trends dataset.
"""

import pandas as pd

FILE_PATH = "spotify_global_trends.csv"


def unique_values_categorical(spot_data: pd.DataFrame,
                              categorical_variables: list[str]) -> dict[
                                    str, list[str]]:
    """
    Given the Spotify Global Trends data and a list of categorical
    variables of interest, this function displays unique values
    and counts each unique value for every categorical
    variable of interest. A dictionary that maps the column names
    to unique values in that column is returned.
    """
    result = {}
    for col in categorical_variables:
        unique_values = list(spot_data[col].unique())
        print(f"Unique Values in {col}: \n {unique_values}")
        print(f"Number of Unique Values in {col}: {len(unique_values)}")
        print("-----------------------------------------------")
        result[col] = unique_values
    return result


def clean_data(spot_data: pd.DataFrame, value_dict: dict[
                                    str, list[str]]) -> pd.DataFrame:
    """
    Given uncleaned Spotify Global Trends data and a dictionary mapping
    all variables to their unique values, cleans the data with reference
    to odd genre and country values found. A DataFrame with
    the cleaned data is returned.
    """
    # Clean Genres
    genres = value_dict["genre"]
    not_genre = ["Offizielle Charts", "Billboard Hot 100", "Dolby Atmos",
                 "Toronto", "Special Purpose Artist", "Falcom"]
    for to_remove in not_genre:
        genres.remove(to_remove)

    mask = []
    for genre in spot_data["genre"]:
        if genre not in genres:
            mask.append(False)
        else:
            mask.append(True)

    cleaned_spot_data = spot_data[mask]

    # Clean Countries
    country_replacement = {
        "England": "GB",
        "Florida": "US",
        "Culiacán": "MX",
        "Monterrey": "MX"
    }

    cleaned_countries = []
    for country in cleaned_spot_data["country"]:
        if country in country_replacement:
            cleaned_countries.append(country_replacement[country])
        else:
            cleaned_countries.append(country)
    cleaned_spot_data["country"] = cleaned_countries
    return cleaned_spot_data


def main():
    spot_data = pd.read_csv(FILE_PATH)

    # NaN Values per colummn
    print(spot_data.isna().sum())

    # Number of Rows
    num_rows = len(spot_data)
    print(f"Number of Rows: {num_rows}")

    # Number of Columns
    num_cols = len(spot_data.loc[0])
    print(f"Number of Columns: {num_cols}")

    # Quantitative Variables of Interest
    seven_num_sum = spot_data.describe()
    print(seven_num_sum)

    # Categorical Variables of Interest
    categorical_variables = ["track_name", "artist_name", "genre", "country",
                             "trend", "popularity_category", "longevity"]

    output = unique_values_categorical(spot_data, categorical_variables)

    # Clean Data
    spot_clean_data = clean_data(spot_data, output)
    unique_values_categorical(spot_clean_data, categorical_variables)


if __name__ == '__main__':
    main()
