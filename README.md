# monte-carlo-risk-analysis
Monte Carlo simulation and VaR analysis using Yahoo Finance data
# Monte Carlo Risk Analysis Using Yahoo Finance Data

## 📌 Project Overview
This project focuses on analyzing stock market risk using historical price data obtained from Yahoo Finance.  
The primary objective is to estimate potential future risk and returns of a stock using **Monte Carlo simulation** and **Value at Risk (VaR)** methodology.

The project demonstrates how probabilistic models can be applied to financial time-series data to support data-driven investment and risk management decisions.

---

## 🎯 Objectives
- To collect and preprocess historical stock price data
- To compute daily returns and volatility
- To apply Monte Carlo simulation for future return estimation
- To calculate Value at Risk (VaR) at a 95% confidence level
- To visualize price trends and risk distributions

---

## 🗂️ Dataset Description
- **Source:** Yahoo Finance  
- **Stock Used:** Apple Inc. (AAPL)  
- **Frequency:** Daily  
- **Key Column Used:** Adjusted Close Price  

The Adjusted Close price is used as it accounts for dividends and stock splits, making it suitable for accurate return calculations.

---

## 🛠️ Tools & Technologies
- **Programming Language:** Python  
- **Libraries Used:**
  - Pandas (Data manipulation)
  - NumPy (Numerical computation)
  - Matplotlib (Data visualization)
- **Data Source:** Yahoo Finance (CSV format)
- **Version Control:** GitHub

---

## 🔍 Methodology

### 1. Data Collection
Historical stock price data was collected from Yahoo Finance and stored in CSV format.

### 2. Data Preprocessing
- Date column converted to datetime format
- Date set as index
- Adjusted Close prices selected for analysis

### 3. Return Calculation
Daily returns were calculated using percentage change of adjusted closing prices.

### 4. Monte Carlo Simulation
Monte Carlo simulation was applied to model potential future returns by assuming a normal distribution based on historical mean and volatility.

- Number of simulations: 10,000
- Trading days considered: 252

### 5. Value at Risk (VaR)
Value at Risk at the 95% confidence level was calculated to estimate the maximum expected loss under normal market conditions.

### 6. Visualization
- Adjusted closing price trend
- Distribution of simulated returns
- VaR threshold marked on distribution

---

## 📊 Results
- Mean daily return and volatility were computed successfully
- Monte Carlo simulation generated a distribution of possible future returns
- Value at Risk (95%) provided a quantitative risk estimate
- Visualizations effectively illustrated price movement and risk exposure

---

## ▶️ How to Run the Project

1. Clone or download this repository
2. Ensure the following files are in the same directory:
   - `monte.py`
   - `AAPL_sample_yahoo.csv`
3. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib
## Run the Script

python monte.py

##📈 Output
---
Console output displaying:

Mean daily return
Volatility
Value at Risk (95%)
Graphs:
Stock price trend
Monte Carlo return distribution with VaR line

##Applications
---
Portfolio risk assessment
Financial forecasting
Quantitative finance learning
Investment decision support

##🔮 Future Enhancements
---

Extend analysis to multiple stocks (portfolio-level risk)

Incorporate correlation between assets

Implement advanced risk metrics (CVaR, Sharpe Ratio)

Integrate with visualization tools such as Tableau or Power BI

