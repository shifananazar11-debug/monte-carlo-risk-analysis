# ==========================================
# Portfolio Risk Management using Monte Carlo
# Value at Risk (VaR)
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ------------------------------------------
# 1. Load Portfolio Data
# ------------------------------------------
# CSV should contain multiple Adj Close columns
# Example columns: Date, AAPL, MSFT, GOOGL, AMZN

data = pd.read_csv("portfolio_data.csv")

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

prices = data

# ------------------------------------------
# 2. Calculate Daily Returns
# ------------------------------------------
returns = prices.pct_change().dropna()

mean_returns = returns.mean()
cov_matrix = returns.cov()

# ------------------------------------------
# 3. Portfolio Weights (Equal-weighted)
# ------------------------------------------
num_assets = len(prices.columns)
weights = np.array([1 / num_assets] * num_assets)

# ------------------------------------------
# 4. Monte Carlo Simulation
# ------------------------------------------
simulations = 10000
trading_days = 252

portfolio_returns = []

for i in range(simulations):
    simulated_daily_returns = np.random.multivariate_normal(
        mean_returns,
        cov_matrix,
        trading_days
    )
    portfolio_daily_returns = simulated_daily_returns.dot(weights)
    portfolio_returns.append(portfolio_daily_returns.sum())

portfolio_returns = np.array(portfolio_returns)

# ------------------------------------------
# 5. Portfolio Value at Risk (95%)
# ------------------------------------------
VaR_95 = np.percentile(portfolio_returns, 5)

print("Portfolio VaR (95% confidence):", VaR_95)

# ------------------------------------------
# 6. Visualizations
# ------------------------------------------
os.makedirs("outputs", exist_ok=True)

# Portfolio price trends
plt.figure()
prices.plot()
plt.title("Portfolio Adjusted Close Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("outputs/portfolio_prices.png")
plt.close()

# Portfolio Monte Carlo VaR
plt.figure()
plt.hist(portfolio_returns, bins=50, density=True)
plt.axvline(VaR_95, linestyle='--', linewidth=2, label='VaR 95%')
plt.title("Portfolio Monte Carlo Simulation - VaR (95%)")
plt.xlabel("Simulated Portfolio Returns")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/portfolio_var_95.png")
plt.close()

print("Portfolio VaR plots saved in outputs folder.")
