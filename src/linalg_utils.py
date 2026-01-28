import numpy as np

def center_data(X):
    mean = np.mean(X, axis=0)
    return X - mean, mean

def covariance_matrix(X):
    n = X.shape[0]
    return (X.T @ X) / n
