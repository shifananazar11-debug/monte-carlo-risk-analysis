import yfinance as yf
import pandas as pd

stocks = ["AAPL", "MSFT", "GOOGL", "AMZN"]
data = yf.download(stocks, start="2022-01-01")['Adj Close']

data.dropna(inplace=True)
returns = data.pct_change().dropna()
rolling_vol = returns.rolling(window=30).std()
print(rolling_vol.tail())