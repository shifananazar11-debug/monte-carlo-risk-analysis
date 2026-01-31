# ================================
# Financial Risk Management Project
# Monte Carlo Simulation & VaR
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load Dataset
# -------------------------------
data = pd.read_csv("AAPL_sample_yahoo.csv")

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

prices = data['Adj Close']

# -------------------------------
# 2. Daily Returns & Volatility
# -------------------------------
returns = prices.pct_change().dropna()

mean_return = returns.mean()
volatility = returns.std()

print("Mean Daily Return:", mean_return)
print("Daily Volatility:", volatility)

# -------------------------------
# 3. Monte Carlo Simulation
# -------------------------------
simulations = 10000
trading_days = 252

simulated_returns = np.random.normal(
    mean_return,
    volatility,
    simulations
)

# -------------------------------
# 4. Value at Risk (95%)
# -------------------------------
VaR_95 = np.percentile(simulated_returns, 5)
print("Value at Risk (95%):", VaR_95)

# -------------------------------
# 5. Visualizations
# -------------------------------

# Create output folder if needed
import os
os.makedirs("outputs", exist_ok=True)

# --- Price Trend Plot ---
plt.figure()
prices.plot()
plt.title("Adjusted Close Price of AAPL")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("outputs/aapl_adjusted_close.png")
plt.close()

# --- Monte Carlo + VaR Plot ---
plt.figure()
plt.hist(simulated_returns, bins=50, density=True)
plt.axvline(VaR_95, linestyle='--', linewidth=2, label='VaR 95%')
plt.title("Monte Carlo Simulation - Value at Risk (95%)")
plt.xlabel("Simulated Returns")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/monte_carlo_var.png")
plt.close()
plt.show
print("Plots saved successfully in the 'outputs' folder.")
