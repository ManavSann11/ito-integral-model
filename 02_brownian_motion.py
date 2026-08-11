"""
Itó Integral Numerical Verification - Day 2: Itó Integral Verification Computes the Itó sum and
compares it to the theoretical right-hand side. 
"""

import numpy as np

# Simulation parameters
T = 1.0                # Total time for horizon
n_steps = 10000        # Number of time steps
n_paths = 5            # Number of paths to simulate

# Discretization setup
dt = T / n_steps

# Generate Brownian Increments and paths
increments = np.sqrt(dt) * np.random.randn(n_paths, n_steps)
W = np.cumsum(increments, axis = 1)
W = np.hstack9[np.zeros((n_paths, 1)), W])

#Compute increments and left-point values
dW = W[:, 1:] - W[:, :-1]          # Brownian increments ΔW_i = W_{t_{i+1}} - W_{t_i}
W_left = W[:, :-1]                 # W at the left endpoint of each interval

# Left-point Riemann sum approximation of the Itó Integral 
# ∑ W_{t_i} * ΔW_i
ito_sum = np.sum(W_left * dW, axis = 1)

#Theoretical value: ½(W_T² - T)
W_T = W[:, -1]               # Value of Brownian motion at time T
rhs = 0.5 * (W_T ** 2 - T)   # Right-hand side of the Itó identity

# Compare the numerical and theoretical values for each path
for i in range(n_paths):
  print(f"Path {i + 1}:")
  print(f" Ito Sum (LHS): {ito_sum[i]:.6f}")
  print(f" Formula (RHS): {rhs[i]:.6f}")
  print(f" Error:         {ito_sum[i] - rhs[i]:.6f}")

# Summary statistics
print("Mean error across paths:", np.mean(ito_sum - rhs))
