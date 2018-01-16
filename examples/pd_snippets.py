import numpy as np;

np.random.seed(42)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;

sns.set(color_codes=True)
from datetime import datetime
import cryptic.cryptocompare as cc
import cryptic.binance as bn
import cryptic.kukoin as kk

"""
Simple snippets for populating, cleaning, organizing, and plotting data.  See also: 

missing data:
https://pandas.pydata.org/pandas-docs/stable/missing_data.html

cookbook:
https://pandas.pydata.org/pandas-docs/stable/cookbook.html

plotting:
https://python-graph-gallery.com/110-basic-correlation-matrix-with-seaborn/
https://tomaugspurger.github.io/modern-6-visualization.html

To add:
- timeseries from binance start (try crypto compare?)
- histogram of future prices for one month, for each time step. Is it safe to "buy low, sell high?"  what are low and high markers?
- 24hr, 7 day change in cryptos relative to USD, BTC, ETH
"""

# POPULATE DF with API call:
df = cc.coin_data()
# df = cc.data_dump()
# df = live_price_matrix()


# ___________DATA CLEANING__________:

# number of nan entries in df:
np.sum(np.sum(df.isnull()))

# replace NaN values with 0:
pd.options.mode.use_inf_as_na = True
df.fillna(0)  # , inplace=True)

# drop rows/cols (axis=0,1) that have NaN values:
df.dropna(axis=0)  # , inplace=True)

# convert column entries to numeric type, else NaN: (pandas 0.22)
df.col = pd.to_numeric(df.col, errors='coerce')

# ________DATA QUERY & MANIPULATION__________:
# get first 20 rows
sample = df[0:20]
# get 20 random rows
sample = df.sample(n=20)
# get 10% random sample of rows
sample = df.sample(frac=0.1)
# randomly scramble rows
sample = df.sample(frac=1.0)

# sort df rows by a column:
df.sort_values(by=['col_name'], inplace=True)
# sort by col1, subsort by col2 (descending order)
df.sort_values(by=['col1', 'col2'], inplace=True, acending=False)

# _____________DATATYPE SPECIFIC ____________:
# convert unix timestamps to datetime strings:
timestamps = cc.price_history().time
time_str = pd.to_datetime(10 ** 9 * timestamps).dt.strftime('%H:%M:%S')

# ______________PLOTTING EXAMPLES_____________:

# BASIC FIGURE, AXES:
df = cc.price_history()
times = df.time
prices = df.close
time_str = pd.to_datetime(10 ** 9 * df.time).dt.strftime('%H:%M:%S')

f, ax = plt.subplots()
ax.plot(times, prices)
ax.set_ylim(min(prices), max(prices))
ax.set_xticklabels(time_str)
ax.set_xlim(min(times), max(times))
plt.show()


def plot_timeseries(timestamps, prices, f=f, ax=ax, title='prices', timestr_format='%H:%M:%S'):
    """
    for line plots

    parameters:
    timestamps (pd.Series):	unix timestamp series
    prices (pd.Series):		timeseries values
    time_format_str (str): 	ex: '%Y-%m-%d', '%H:%M:%S'
    """
    time_str = pd.to_datetime(10 ** 9 * df.time).dt.strftime(timestr_format)

    # if ax is None and f is None:
    # 	f, ax = plt.subplots()

    ax.plot(timestamps, prices)

    ax.set_title(title)
    ax.set_xlim(min(timestamps), max(timestamps))
    ax.set_xticklabels(time_str)
    ax.set_ylim(min(price), max(price))
    f.autofmt_xdate()
    return f, ax


# DF HEATMAP (SNS):
df = cc.live_price_matrix(coins_of_interest)
ax = sns.heatmap(df, annot=True, annot_kws={"size": 7})
plt.show()
f = matplotlib.figure()

# MULTI TIMEPLOT:
df = cc.price_history()
f, axes = plt.subplots()
df.iloc[:, 1].plot()
df.iloc[:, 2].plot()
plt.show()

# HEATMAP PCT CHANGE:
coin_syms = cc.coin_data().sample(frac=.01).index
data_dump = cc.live_data_dump(coin_syms=default_coins)

# df.drop(url)
df = pd.DataFrame()

for k, v in data_dump.items():
    df[k] = v['CHANGEPCT24HOUR'].dropna()
df.sort_index(inplace=True)
df = df.T
df.sort_index(inplace=True)

df.fillna(0, inplace=True)

ax = sns.heatmap(df, annot=True, annot_kws={"size": 3})
plt.show()
