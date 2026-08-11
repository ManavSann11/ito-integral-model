"""
Itó Integral Numerical Verification - Day 1: Brownian Motion Simulation simulates the paths of 
Brownian motion using the Euler-Maruyama discretization scheme. 
"""
print("Starting script")
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
T = 1.0                # Total time horizon
n_steps = 1000         # Number of time steps
n_paths = 5            # Number of paths to simulate

#Discretization step 
dt = T / n_steps                             # Time step size
times = np.linspace(0, T, n_steps + 1)       # Time grid

# Generate Brownian increments and paths
# Each increment is normally distributed with mean 0 and variance dt
increments = np.sqrt(dt) * np.random.random(n_paths, n_steps)

# Cumulative sum to get Brownian motion paths
W = np.cumsum(increments, axis = 1)

# Add initial point at t = 0 (W_0 = 0)
W = np.hstack([np.zeros((n_paths, 1_)), W])

# Plot the simulated paths
plt.figure(figsize = (10, 6))
for i in range(n_paths):
  plt.plot(times, W[i], linewidth = 1.5)
plt.title("Simulated Brownian Motion Paths")
plt.xlabel("Time")
plt.ylabel("W_t")
plt.grid(True)
print("about to show plot")
plt.show()
print("finished")
