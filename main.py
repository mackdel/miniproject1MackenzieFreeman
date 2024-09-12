# INF601 - Advanced Programming in Python
# Mackenzie Freeman
# Mini Project 1
import os
import pprint
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

# 5 stock tickers
mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]
# marvell is MRVL
# intel is INTC
# amazon is #AMZN

# Get today's date
today = datetime.now()

# Calculate the date 10 days ago
ten_days_ago = today - timedelta(days=14)

mytickers.sort()
for ticker in mytickers:
    # Collect the closing price of the stock tickers
    # for the last 10 trading days.
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    # Convert array to an array in NumPy and plot graph
    if len(last10days) == 10:
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} last 10 Closing Prices")
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")
