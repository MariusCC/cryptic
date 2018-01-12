#basic snippets for fast retrieval
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)
import numpy as np;  np.random.seed(42)
import datetime.datetime
import cryptic.cryptocompare as cc
import cryptic.binance as bn
import cryptic.kukoin as kk

"""
Plotting examples:
https://python-graph-gallery.com/110-basic-correlation-matrix-with-seaborn/
https://tomaugspurger.github.io/modern-6-visualization.html
"""

# BASIC FIGURE, AXES:
df 		= cc.price_history()
dates 	= pd.to_datetime(10**9*df.time).dt.strftime('%Y-%m-%d')
price 	= df.close


f, ax 	= plt.subplots()
ax.plot(dates, price)
ax.set_ylim(min(price), max(price))
#ax.set_yticks()
ax.set_xlim(min(dates), max(dates))
plt.show()


#DF HEATMAP (SNS):
df = cc.live_price_matrix(coins_of_interest)
ax = sns.heatmap(df, annot=True, annot_kws={"size": 7})
plt.show()


#MULTI TIMEPLOT:
df = cc.price_history()
f, axes = plt.subplots()
df.iloc[:,1].plot()
df.iloc[:,2].plot()
plt.show()

#HEATMAP PCT CHANGE:
coin_syms = cc.coin_data().sample(frac=.01).index
data_dump = cc.live_data_dump(coin_syms=default_coins)

#df.drop(url)
df = pd.DataFrame()

for k,v in data_dump.items():
	df[k] = v['CHANGEPCT24HOUR'].dropna()
df.sort_index(inplace=True)
df = df.T
df.sort_index(inplace=True)

df.fillna(0,inplace=True)

ax = sns.heatmap(df, annot=True, annot_kws={"size": 3})
plt.show()






