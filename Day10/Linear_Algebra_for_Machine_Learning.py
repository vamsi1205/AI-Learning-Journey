import numpy as np

v1 = np.array([2, 4, 6])
v2 = np.array([1, 3, 5])

# Basic operations
print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Dot Product:", np.dot(v1, v2))
print("Scalar Multiplication:", 3 * v1)
print("Magnitude of v1:", np.linalg.norm(v1))


A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

print("Matrix Addition:\n", A + B)
print("Matrix Transpose:\n", A.T)
print("Matrix Shape:", A.shape)


X = np.array([[2, 3], [4, 5], [6, 7]])  # 3 samples × 2 features
W = np.array([[0.2, 0.4], [0.6, 0.8]])  # weights (2 × 2)

result = np.dot(X, W)
print("Result of X·W =\n", result)

M = np.array([[2, 5], [1, 3]])

det = np.linalg.det(M)
inv = np.linalg.inv(M)

print("Determinant:", det)
print("Inverse:\n", inv)


vals, vecs = np.linalg.eig(M)
print("Eigenvalues:", vals)
print("Eigenvectors:\n", vecs)
