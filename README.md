# Itó Integral Numerical Verification

A numerical verification of the Itó Integral identity using Monte Carlo simulation. The project
simulates Brownian motion paths, computes left-point Riemann sums, and demonstrates convergence 
to the theoretical result.

## Mathematical Background

The Itó Integral identity states that for a standard Brownian motion \( W_t \):

$$ \int_0^T W_t \, dW_t = \frac{1}{2} (W_T^2 - T) $$

The left-hand side is approximated using a left-point Riemann sum:

$$ \sum_{i=0}^{n-1} W_{t_i} (W_{t_{i+1}} - W_{t_i}) $$

The project verifies this identity numerically and analyzes the convergence of the approximation
as the number of time steps increases.

## Project Progression

### Day 1: Brownian Motion Simulation
Simulates multiple paths of Brownian motion using the Euler-Maruyama discretization scheme. 

