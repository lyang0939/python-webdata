＃get webdata from internal yahoo 

# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from pandas_datareader import data

DAX = data.DataReader(name='^GDAXI', data_source='yahoo',
                     start='2000-1-1')
DAX.info()
df=pd.DataFrame(DAX)
df.to_csv('DAX.csv')
! cat DAX.csv
df_load=pd.read_csv('DAX.csv')
DAX.tail()

%pylab inline

DAX['Close'].plot(figsize=(8, 5), grid=True)
# tag: dax
# title: Historical DAX index levels

%time DAX['Return'] = np.log(DAX['Close'] / DAX['Close'].shift(1))

DAX[['Close', 'Return']].tail()

DAX[['Close', 'Return']].plot(subplots=True, style='b',
                              figsize=(8, 5), grid=True)
# tag: dax_returns
# title: The DAX index and daily log returns

DAX['42d'] = pd.rolling_mean(DAX['Close'], window=42)
DAX['252d'] = pd.rolling_mean(DAX['Close'], window=252)
DAX[['Close', '42d', '252d']].tail()

DAX[['Close', '42d', '252d']].plot(figsize=(8, 5), grid=True)
# tag: dax_trends
# title: The DAX index and moving averages

import math
DAX['Mov_Vol'] = pd.rolling_std(DAX['Return'],
                                window=252) * math.sqrt(252)
# moving annual volatility

DAX[['Close', 'Mov_Vol', 'Return']].plot(subplots=True, style='b',
                                         figsize=(8, 7), grid=True)
# tag: dax_mov_std
# title: The DAX index and moving, annualized volatility






























import pandas.io.data as web
DAX = web.DataReader(name='^GDAXI', data_source='yahoo',start='2000-1-1')
DAX.info()
DAX.tail()
DAX['Close'].plot(figsize=(8, 5), grid=True)
# tag: dax
# title: Historical DAX index levels

%time DAX['Return'] = np.log(DAX['Close'] / DAX['Close'].shift(1))

DAX[['Close', 'Return', 'Return']].tail()

DAX[['Close', 'Return']].plot(subplots=True, style='b',figsize=(8, 5), grid=True)

# tag: dax_returns
# title: The DAX index and daily log returns

DAX['42d'] = pd.rolling_mean(DAX['Close'], window=42)
DAX['252d'] = pd.rolling_mean(DAX['Close'], window=252)

DAX[['Close', '42d', '252d']].tail()

DAX[['Close', '42d', '252d']].plot(figsize=(8, 5), grid=True)
# tag: dax_trends
# title: The DAX index and moving averages

import math
DAX['Mov_Vol'] = pd.rolling_std(DAX['Return'],window=252) * math.sqrt(252)

# moving annual volatility

DAX[['Close', 'Mov_Vol', 'Return']].plot(subplots=True, style='b',figsize=(8, 7), grid=True)
# tag: dax_mov_std
# title: The DAX index and moving, annualized volatility
