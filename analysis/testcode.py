"""
tmp code buffer for debugging, frequently overwritten.
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


#%% BINANCE
# base_url = 'https://api.binance.com/api/v1/'
# endpoint = 'exchangeInfo'


#%% convert to request to database:

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











# %% useful functions:

#check for nans in entries
pd.isnull(df)














