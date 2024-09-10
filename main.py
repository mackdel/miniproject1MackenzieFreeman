# INF601 - Advanced Programming in Python
# Mackenzie Freeman
# Mini Project 1

import pprint
import yfinance as yf

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]
# marvell is MRVL
# intel is INTC
# amazon is #AMZN

mydata = {}

for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dailyHigh': result.info['dayHigh']
                      }
    print(f"Ticker: {ticker} \tDaily High: {result.info['dayHigh']}")

# get all stock info
#pprint.pprint(msft.info)

# get historical market data
#hist = msft.history(period="5d")

#pprint.pprint(hist)