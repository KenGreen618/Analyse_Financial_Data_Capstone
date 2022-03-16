import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
def get_risk(prices):
    return (prices / prices.shift(1) - 1).dropna().std().values
def get_return(prices):
    return ((prices / prices.shift(1) - 1).dropna().mean() * np.sqrt(250)).values
symbols = ['BA', 'C', 'AAL', 'NFLX']
prices = pd.DataFrame(index=pd.date_range(start, end))
for symbol in symbols:
    portfolio = web.DataReader(name=symbol, data_source='quandl', start=start, end=end)
    close = portfolio[['AdjClose']]
    close = close.rename(columns={'AdjClose': symbol})
    prices = prices.join(close)
    portfolio.to_csv("~/workspace/{}.csv".format(symbol))
prices = prices.dropna()
risk_v = get_risk(prices)
return_v = get_return(prices)

fig, ax = plt.subplots()
ax.scatter(x=risk_v, y=return_v, alpha=0.5)
ax.set(title='Return and Risk', xlabel='Risk', ylabel='Return')
for i, symbol in enumerate(symbols):
    ax.annotate(symbol, (risk_v[i], return_v[i]))
plt.show()