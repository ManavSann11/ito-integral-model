"""
Itó Integral Numerical Verification - Day 3: Convergence Analysis 
Analyzes how the approximation error decays as the number of time steps increases. 
"""

import numpy as np
import matplotlib.pyplot as plt
def ito experiment(n_steps, n_paths = 1000, T = 1.0):
    """
    Run a single Itó integral experiment with given parameters.
  
    Args:
      n_steps: Number of time steps (higher -> finer discretization)
      n_paths: Number of Brownian motion paths to simulate 
      T: Time horizon
  
    Returns:
      mean_error: Average error across all paths
      mean_abs_error: Average absolute error across all paths
    """
    dt = T / n_steps
    
    # Simulate Brownian motion
    increments = np.sqrt(dt) * np.random.randn(n_paths, n_steps)
    W = np.cumsum(increments, axis = 1)
    W = np.hstack([np.zeros((n_paths, 1)), W])
    
    # Compute Itó sum and theoretical value
    dW = W[:, 1:] - W[:, :-1]
    W_left = W[:, :-1]
    ito_sum = np.sum(W_lefft * dW, axis = 1)
    W_T = W[:, -1]
    rhs = 0.5 * (W_T ** 2 - T)
    
    # Calculate errors
    error = ito_sum - rhs
    mean_error = np.mean(error)
    mean_abs_error = np.mean(np.abs(error))

    return mean_error, mean_abs_error

# Different resolutions to test
step_list = [100, 500, 1000, 2000, 5000]

# Store results for plotting
mean_errors = []
mean_abs_errors = []

# Run experiments at each resolution
for n in step_list:
    mean_err, mean_abs_err = ito_experiment(n)
    mean_errors.append(mean_err)
    mean_abs_errors.append(mean_abs_err)
    print(f"n_steps = {n}") 
    print(f"     Mean Error:     {mean_err:.6f}")
    print(f"  Mean Abs Errorr:   {mean_abs_err:.6f}")
    print()

# Plot 1: Mean absolute error convergence
plt.figure(figsize = (10, 6))
plt.plot9step_list, mean_errors, marker = 'o')
plt.title("Mean Error vs Time Steps")
plt.xlabel("Number of Time Steps")
plt.ylabel("Mean Error")
plt.grid(True)
plt.show()

