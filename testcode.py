"""
test/sandbox code.
- harvest crypto data (start with coinmarket cap)
- get (new) alt coins from API to plot, automated
- write analysis suite
	- performance vs time of particular alt coin (not available without saving snapshots)
	- EV of (filtered) coins over X time frame
	- price as a function of time from first appearance
	- price


"""
import requests
import pandas as pd
import numpy as np
import time
import datetime
import random
import json
from pprint import pprint
import io
import matplotlib.pyplot as plt


#INPUT: select a base_url and endpoint below it:

#Coinmarketcap
# all currently available coinmarketcap api data
base_url = 'https://api.coinmarketcap.com/v1/ticker/'
endpoint = '?limit=0'

#%% Cryptocompare
#list of available altcoins,
#Soc media data (provis)
base_url = 'https://www.cryptocompare.com/api/'
endpoint = 'data/coinlist/'
endpoint = 'SocialStats'
endpoint = 'CoinSnapshot?fsym=ETH&tsyms=USD'

#- data at given timestamp (UTC)
#- daily historical data 
base_url = 'https://min-api.cryptocompare.com/data/'
endpoint = 'pricehistorical?fsym=ETH&tsyms=BTC,USD&ts=1452195664&extraParams=your_app_name'
endpoint = 'histoday?fsym=BTC&tsym=USD&limit=30&aggregate=1'

#%% BINANCE
# base_url = 'https://api.binance.com/api/v1/'
# endpoint = 'exchangeInfo'


#%% convert to request to database:
req 	= requests.get(base_url+endpoint)
def req_to_db(req):

	if req.status_code != 200:
		print('Error in request')
		return None
	
	try:
		df = pd.read_json(req.content)
	except ValueError:
		data = json.loads(req.content)
		df = pd.DataFrame.from_dict(data['Data'])

	return df


# db summary
df 	= req_to_db(req)
df.columns
df.head()


#%% plotting examples:



#histogram of 24h, 7d %change
#base_url='https://api.coinmarketcap.com/v1/ticker/'
#'?limit=0'
df['percent_change_24h'].dropna().hist()
df['percent_change_7d'].dropna().hist()

















