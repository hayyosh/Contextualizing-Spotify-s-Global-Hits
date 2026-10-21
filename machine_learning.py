"""
Twisha Santra, Hayley Yoshikawa
CSE 163
This program trains and evaluates a predictive machine
learning model for our Spotify Global Trends data.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, ConfusionMatrixDisplay)
import eda


def main():
    spot_data = pd.read_csv(eda.FILE_PATH)

    # Categorical Variables of Interest
    categorical_variables = ["track_name", "artist_name", "genre", "country",
                             "trend", "popularity_category", "longevity"]

    output = eda.unique_values_categorical(spot_data, categorical_variables)

    # Clean Data
    cleaned_spot_data = eda.clean_data(spot_data, output)

    # Features & Target
    X = cleaned_spot_data[["genre", "viral_score", "stream_change"]]
    X = pd.get_dummies(X)
    y = cleaned_spot_data["longevity"]

    # Split Data.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=42)

    # Scale Features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Training SVM Model
    svm_clf = SVC(kernel="linear", C=1.0, random_state=42)
    svm_clf.fit(X_train_scaled, y_train)

    # Model Evaluatiom
    y_pred = svm_clf.predict(X_test_scaled)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    target_names = svm_clf.classes_
    print(classification_report(y_test, y_pred,
                                target_names=target_names))

    # Visualizing SVM Model with a Confusion Matrix
    fig, ax = plt.subplots(1, 1, figsize=(20, 10))
    cm = confusion_matrix(y_test, y_pred)
    cm_display = ConfusionMatrixDisplay(cm, display_labels=target_names)
    cm_display.plot(ax=ax, cmap="gnuplot")
    plt.title("Confusion Matrix for SVM Model")
    plt.show()


if __name__ == '__main__':
    main()
