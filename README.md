# Itó Integral Numerical Verification

A numerical verification of the Itó Integral identity using Monte Carlo simulation. The project
simulates Brownian motion paths, computes left-point Riemann sums, and demonstrates convergence 
to the theoretical result.

## Mathematical Background

The Itó Integral identity is a fundamental result in stochastic calculus. For a standard Brownian motion $\( W_t \)$, the identity states:

$$ \int_0^T W_t \, dW_t = \frac{1}{2} (W_T^2 - T) $$

This result is non-intuitive because it differs from the classical calculus result $\( \int x \$, $dx = \frac{1}{2}x^2 \)$. The difference arises because Brownian motion has nonzero quadratic variation, which contributes the \( -T/2 \) term.

The left-hand side is approximately using a left-point Riemann sum:

$$ \sum_{i=0}^{n-1} W_{t_i} (W_{t_{i+1}} - W_{t_i}) $$

The project verifies this identity numerically and analyzes the convergence of the approximation as the number of time steps increases.

## Problem Statement

The goal of this project is to numerically confirm the Itó integral identity and demonstrate the convergence of the discrete approximation. This is important because:
- It provides intuition for stochastic calculus
- It validates the numerical methods used in quantitative finance
- It demonstrates the difference between deterministic and stochastic integration

## Project Progression

### Day 1: Brownian Motion Simulation
Simulates multiple paths of Brownian motion using the Euler-Maruyama discretization scheme with normally distributed increments. 

### Day 2: Itó Integral Verification
Computes the Itó sum for each path and compares it to the theoretical right-hand side, displaying individual path errors.

### Day 3: Convergence Analysis
Analyzes how the approximation error decays as the number of time steps increases, with both mean error and mean absolute error plotted against step size. The analysis includes multiple step sizes from 100 to 5000. 

### Day 4: Extended Analysis
Includes quadratic variation convergence analysis alongside the Itó identity, with RMSE metrics and comprehensive plots. 

## Tech Stack
- Python 3
- NumPy for numerical computation
- Matplotlib for visualization

## Repository Structure
Ito-integral-verification/
├── README.md
├── day1_brownian_motion.py
├── day2_ito_verification.py
├── day3_convergence_analysis.py
├── day4_extended_analysis.py

## How to Run
1. Clone the repository
2. Install dependencies: `pip install - r requirements.txt`
3. Run the scripts in order from day1 to day4

## Results

The numerical results confirm the Itó identity:

-**Itó sum** converges to \( \frac{1}{2}(W_T^2 - T) \) as the number of time steps increases
- **Mean absolute errorr** decay as \( O(1/\sqrt{n}) \), consistent with theoretical expectations
- **Quadratic variation** converges to \( T \), confirming the properties of Brownian motion
- **RMSE** provides a robust measure of convergence across multiple paths

These results demonstrate that the discrete approximation accurately captures the continuous stochastic integral. 

## Author
Manav Sannappanavar
NYU | Mathematics and Data Science


