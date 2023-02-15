import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

import plotly
import plotly.graph_objs as go
import operator
from datetime import datetime

fp = open('stocks', 'r')

content = fp.read()

fp.close()

stocks = []

for line in content.split("\n"):
    if line.strip():
        stocks.append(line)


results = {}
    
for stock_ticker in stocks:
    stock_ticker = stock_ticker.strip()
    try:
        print(stock_ticker)
        #stock_ticker = 'TSLA'
        ticker = yf.Ticker(stock_ticker)

        #data = yf.download(stock_ticker, start="2017-01-01", end="2017-04-30")
        data = ticker.history(period='1y')
        #data = ticker.history(period="max")
        #end_date = datetime.now().strftime('%Y-%m-%d')
        #data = ticker.history(start='2022-01-01',end=end_date)

        first_row = data.iloc[0]
        #print(first_row)
        #print(first_row)

        last_row = data.iloc[-1]
        #print(last_row)
        #print(last_row)

        change = last_row['Open'] - first_row['Open']
        #percent_change = (last_row['Open'] - first_row['Open']) / first_row['Open']
        #print("change: \n")
        #print(change)
        if change>0:
            results[stock_ticker] = change
    except:
        print("Error with stock "+str(stock_ticker))


#print(results)
sorted_x = sorted(results.items(), key=lambda x: x[1], reverse=True)
print(sorted_x)
print("Amount of good stock choices:"+str(len(sorted_x)))



# data['Close'].plot(title="TSLA's stock price")
'''
fig = go.Figure()
fig.add_trace(go.Candlestick())
fig.add_trace(go.Candlestick(x=data.index,open = data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name = 'market data'))
fig.update_layout(title = str(stock_ticker)+' share price', yaxis_title = 'Stock Price (USD)')
fig.show()
'''

