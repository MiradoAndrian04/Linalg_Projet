import numpy as np

def pca(X, k):
    # Matrice covariance
    C = (X.T @ X) / X.shape[0]

    # Valeurs propres
    eigenvalues, eigenvectors = np.linalg.eig(C)

    # Tri décroissant
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Sélection des k composantes
    W = eigenvectors[:, :k]

    # Projection
    Z = X @ W

    return Z, eigenvalues[:k], W
