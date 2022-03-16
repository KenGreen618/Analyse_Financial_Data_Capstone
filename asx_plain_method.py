import numpy as np
import datetime as dt
from pandas_datareader import data as pdr


# Import Data
def getData(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start=start , end=end)
    stockData = stockData['Adj Close']

    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

def portfolioPerformance(weights, meanReturns, covMatrix):
    returns = np.sum(meanReturns * weights) * 252
    std = np.sqrt(np.dot(weights.T, np.dot(covMatrix, weights))) * np.sqrt(252)
    return returns, std


stockList = ['CBA', 'BHP', 'TLS']
stocks = [stock + '.AX' for stock in stockList]
# .AX is for australian stocks

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365)

print(getData(stocks, start=startDate, end=endDate))
