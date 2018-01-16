# basic snippets for fast retrieval
import matplotlib.pyplot as plt
import seaborn as sns;

sns.set(color_codes=True)
import numpy as np;

np.random.seed(42)
from datetime import datetime
import cryptic.cryptocompare as cc
import cryptic.binance as bn
import cryptic.kukoin as kk


def timeseries(timestamps, prices, f=f, ax=ax, title='prices', timestr_format='%H:%M:%S'):
    """
    simplifies timeseries plotting.  Probably better as a class than a function.

    PARAMETERS:
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
    ax.set_ylim(min(prices), max(prices))
    f.autofmt_xdate()
    return f, ax


def heatmap(df, title='', fontsize=7):
    """
    makes a heatmap of dataframe values.  Column
    
    df (pd.DataFrame): dataframe with numerical entries
    return: ax (matplotlib axes object)
    """
    f, ax = plt.subplots()
    ax = sns.heatmap(df, annot=True, annot_kws={"size": fontsize})
    return f, ax
