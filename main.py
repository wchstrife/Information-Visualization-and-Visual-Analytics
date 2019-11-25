import numpy as np


def PCA(X=np.array([]), no_dims=50):
    (n, d) = X.shape
    X = X - np.tile(np.mean(X, 0), (n, 1))
    (l, M) = np.linalg.eig(np.dot(X.T, X))
    print(M.shape)
    Y = np.dot(X, M[:, 0:no_dims])
    return Y

if __name__ == "__main__":
    X = np.loadtxt("mnist2500_X.txt")
    labels = np.loadtxt("mnist2500_labels.txt")
    print(X.shape)
    X = PCA(X, 50).real
    print(X.shape)
