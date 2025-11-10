import numpy as np

# Inputs (2 features)
x = np.array([0.5, 0.8])

# Weights and bias
w = np.array([0.4, 0.7])
b = 0.1

# Step 1: Weighted sum
z = np.dot(x, w) + b
# print(np.dot(x, w))
# print(z)


# Step 2: Activation (Sigmoid)
def sigmoid(x):
    # print(x)
    # print(-x)
    # print(np.exp(-x))
    return 1 / (1 + np.exp(-x))


output = sigmoid(z)

print("Neuron Output:", output)
