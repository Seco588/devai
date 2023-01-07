import numpy as np


def shuffle_data(X, y):
    # Shuffle data here
    index = np.random.permutation(X.shape[0])
    X = X[index]
    y = y[index]

    return X, y


def split_data(X, y, test_size):
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size)

    return X_train, X_test, y_train, y_test
