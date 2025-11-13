# Run this first (only once)
# pip install torch torchvision matplotlib

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

print("PyTorch version:", torch.__version__)


import torch

# Create tensor
t = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print("Tensor:\n", t)

# Tensor operations
print("Shape:", t.shape)
print("Sum:", t.sum())
print("Mean:", t.mean())

# Convert between NumPy <-> Tensor
import numpy as np

n = np.array([[5, 6], [7, 8]])
t_from_np = torch.from_numpy(n)
print("From NumPy:\n", t_from_np)

n_back = t_from_np.numpy()
print("Back to NumPy:\n", n_back)


x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3 * x + 4
y.backward()  # Compute dy/dx
print("Gradient (dy/dx):", x.grad)
