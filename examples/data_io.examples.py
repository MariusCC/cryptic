import cryptocompare as cc
from util_functions import *

"""
APPEND/READ PRICE HISTORY DATA to file for all default coins:
# default parameters will read and write data to pickle file ETH_in_USD_by_minute_on_CCCAGG.pkl
"""
coin_list = cc.default_coins.remove('USD')


def update_recent_price_histories(time_interval='hour', coin_list=coin_list, unit='USD'):

	for coin in coin_list:
		df = cc.price_history(time_interval=time_interval, coin=coin)
		cc.write_price_history(df)



time_interval = 'hour'
for coin in cc.defaul_coins:


# append new data to master df
df = cc.price_history()
cc.write_price_history(df)

# read stored data:
dfmaster = cc.read_price_history()

			
# hour data
df = cc.price_history(time_interval='day')
#cc.write_price_history(df, coin='ETH', unit='USD', time_interval='day', exchange='CCCAGG')


# READING DATA: