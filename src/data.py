import numpy as np
import pandas as pd


def load_data(path):
    # Load data from CSV file
    df = pd.read_csv(path)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    return X, y


def preprocess_data(X, y):
    # Preprocess data here
    # This could include scaling, normalization, encoding, etc.
    return X, y
