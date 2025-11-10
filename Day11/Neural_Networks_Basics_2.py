import numpy as np

# Inputs
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Weights and biases
W1 = np.array([[0.2, 0.4], [0.3, 0.7]])
b1 = np.array([0.1, 0.2])

W2 = np.array([[0.6], [0.9]])
b2 = np.array([0.3])


# Forward pass
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Hidden layer
hidden = sigmoid(np.dot(X, W1) + b1)


# Output layer
output = sigmoid(np.dot(hidden, W2) + b2)

print("Final Output:\n", output)

# print(
#     sigmoid(
#         np.dot(
#             [
#                 [0.52497919, 0.549834],
#                 [0.59868766, 0.7109495],
#                 [0.57444252, 0.64565631],
#                 [0.64565631, 0.78583498],
#             ],
#             W2,
#         )
#         + b2
#     )
# )
