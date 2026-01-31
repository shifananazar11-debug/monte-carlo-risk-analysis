import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 1️⃣ LOAD DATA
# ===============================
data = pd.read_csv("AAPL_sample_yahoo.csv")

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

prices = data['Adj Close']

# ===============================
# 2️⃣ DAILY RETURNS
# ===============================
returns = prices.pct_change().dropna()

mean_return = returns.mean()
std_return = returns.std()

print("Mean Daily Return:", mean_return)
print("Daily Volatility:", std_return)

# ===============================
# 3️⃣ MONTE CARLO SIMULATION
# ===============================
simulations = 10000
days = 252  # trading days in a year

simulated_returns = np.random.normal(
    mean_return,
    std_return,
    simulations
)

# ===============================
# 4️⃣ VALUE AT RISK (VaR 95%)
# ===============================
VaR_95 = np.percentile(simulated_returns, 5)
print("VaR at 95% confidence level:", VaR_95)

# ===============================
# 5️⃣ GRAPHS
# ===============================

# Price chart
plt.figure()
prices.plot(title="AAPL Adjusted Close Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

# Returns distribution
plt.figure()
plt.hist(simulated_returns, bins=50)
plt.axvline(VaR_95, linestyle='--', label='VaR 95%')
plt.title("Monte Carlo Simulated Returns")
plt.legend()
plt.show()
