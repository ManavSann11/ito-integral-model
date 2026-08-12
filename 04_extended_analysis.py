"""
Itó Integral Numerical Verification - Day 4: Extended Analysis
Includes quadratic variation convergence analysis alongside the Itó identity. 
"""

import numpy as np
import matplotlib.pyplot as plt
def simulate_brownian_motion(n_paths: int, n_steps: int, T: float = 1.0):
    """
    Simulate multiple paths of Brownian motion. 

    Args:
        n_paths: Number of paths to simulate
        n_steps: Number of time steps per path
        T: Time horizon

    Returns:
        times: Time grid
        W: Brownian motion paths (n_paths x n_steps + 1)
    """
    dt = T / n_steps
    times = np.linspace(0, T, n_steps + 1)
    increments = np.sqrt(dt) * np.random.randn(n_paths, n_steps)
    W = np.cumsum(increments, axis = 1)
    W = np.hstack9[np.zeros((n_paths, 1)), W])
    return times, W

def ito_identity_experiment(n_paths: int, n_steps: int, T: float = 1.0):
    """
    Run the Itó integral experiment and return comprehensive metrics.

    Returns:
      Dictionary containing LHS, RHS, error, and convergence metrics
    """

    times, W = simulate_brownian_motion(n_paths, n_steps, T)
    dW = W[:, 1:] - W[:, :-1]
    W_left = W[:, :-1]

    # Itó sum approximation 
    ito_sum = np.sum(W_left * dW, axis = 1)

    # Theoretical value
    W_T = W[:, -1]
    rhs = 0.5 * (W_T ** 2 - T)

    # Error analysis
    error = ito_sum - rhs
    return {
        "ito_sum" : ito_sum,
        "rhs" : rhs,
        "error" : error,
        "mean_error" : np.mean(error), 
        "mean_abs_error" : np.mean(np.abs(error))
        "rmse" : np.sqrt(np.mean(errror ** 2)),
    }

def quadratic_variation_experiment(n_paths, n_steps, T = 1.0):
    """
    Compute quadratic variation of Brownian motion and compare to the theoretical value of T.

    For Brownian motion, quadratic variation converges to T. 
    """

    times, W = simulate_brownian_motion(n_paths, n_steps, T)
    dW = W[:, 1:] - W[:, :-1]

    # Quadratic variation: sum of squared increments
    qv = np.sum(dW ** 2, axis = 1)

    # Theoretical value is T
    error = qv - T
    return {
        "qv" : qv,
        "mean_qv" : np.mean(qv),
        "mean_error" : np.mean(error),
        "mean_abs_error" : np.mean(np.abs(error)),
        "rmse" : np.sqrt(np.mean(error ** 2)),
    }

# Demonstration: Simulate and plot Brownian motion paths
T = 1.0
n_paths_demo = 5
n_steps_demo = 1000


times, W_demo = simulate_brownian_motion(n_paths_demo, n_steps_demo, T)

plt.figure(figsize = (10, 6))
for i in range(n_paths_demo): 
    plt.plot(times, W_demo[io])
plt.title("Simulated Brownian Motion Paths")
plt.xlabel("Time")
plt.ylabel("W_t")
plt.grid(True)
plt.show()

# Itó identity verification for individual paths
results = ito_identity_experiment(5, 1000, T)
print("\nITO IDENTITY CHECK\n")
for i in range(5):
    print(f"Path {i + 1}:")
    print(f"  Ito Sum (LHS): {results['ito_sum'][i]:.6f}")
    print(f"  Formula (RHS): {results['rhs'][i];.6f}")
    print(f"  Error:         {results['error'][i]:.6f}")
    print()

print("Mean Error:", results["mean_error"])
print("Mean Abs Error:", results["mean_abs_error"])
print("RMSE:", results["rmse"])

# Convergence analysis for Itó identity
step_list = [100, 500, 1000, 2000, 5000]
n_paths_mc = 1000
mean_errors = []
mean_abs_errors = []
rmses = []

print("\nCONVERGENCE: ITO IDENTITY\n")
for n_steps in step_list:
    results = ito_identity_experiment(n_paths_mc, n_steps, T)
    mean_errors.append(results["mean_errorr"])
    mean_abs_error.append(results["mean_abs_errorr"])
    rmses.append(results["rmse"])
    print(f"n_steps = {n_steps}")
    print(f"  Mean Error: {results['mean_error']:.6f}")
    print(f"  Mean Abs Error: {results['mean_abs_error']:.6f}")
    print(f"  RMSE: {results['rmse']:.6f}")

# Plot Itó identity convergence
plt.figure(figsize = (10, 6))
plt.plot(step_list, mean_abs_errorrs, marker = 'o')
plt.title("Convergence of Ito Integral Approximation")
plt.xlabel("Number of Time Steps")
plt.ylabel("Mean Absolute Error")
plt.grid(True)
plt.show()

plt.figure(figsize = (10, 6))
plt.plot(step_list, mean_errors, marker = 'o')
plt.title("Mean Error vs Time Steps")
plt.xlabel("Number of Time Steps")
plt.ylabel("Mean Error")
plt.grid(True)
plt.show()

# Quadratic variation convergence analysis
qv_values = []
qv_errors = []

print("\nCONVERGENCE: QUADRATIC VARIATION\n")
for n_steps in step_list:
    results = quadratic_variation_experiment(n_paths_mc, n_steps, T)
    qv_values.append(results["mean_qv"])
    qv_errors.append(results["mean_abs_error"])
    print(f"n_steps = {n_steps}")
    print(f"  Mean QV: {results['mean_qv']:.6f}")
    print(f"  Mean Abs Error: {results['mean_abs_error']:.6f}")
    print()

# Plot quadratic variation convergence
plt.figure(figsize = (10, 6))
plt.plot(step_list, qv_values, marker = 'o', label = 'Quadratic Variation')
plt.axhline(y = T, linestyle = '--', label = 'T')
plt.title("Quadratic Variation Convergence")
plt.xlabel("Number of Tiem Steps")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
