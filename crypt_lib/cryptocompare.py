from util_functions import *
#import sys
#import urllib.parse

"""
In this file:
- coin_list():
- live_price(value_symbol='ETH', unit_symbols=['USD','BTC'], exchange='')
- def live_price_matrix(coin_symbols=['ETH','BTC','USD'], exchange='')
- ...

To add? reference: https://www.cryptocompare.com/api
-  'https://www.cryptocompare.com/api/data/CoinSnapshot?fsym=ETH&tsyms=USD'
- https://www.cryptocompare.com/api#-api-data-coinsnapshot-
- https://min-api.cryptocompare.com/data/top/pairs?fsym=ETH
"""


def coin_list():
	"""
	list of coins listed on cryptocompare with additional data.
	"""
	url = 'https://www.cryptocompare.com/api/data/coinlist/'
	df 	= url_to_dataframe(url)
	df = df.T
	df.url = url
	return df


def live_price(value_symbol='ETH', unit_symbols=['USD','BTC'], exchange=''):
	"""
	return the value of coin1 in units [coin2,coin3,...coinN].
	example:
	live_price
	"""
	url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
			.format(value_symbol.upper(), ','.join(unit_symbols).upper())

	if exchange:
		url += '&e={}'.format(exchange)
	
	data 	= url_to_dict(url)
	df = pd.DataFrame.from_dict(data,orient='index')

	df.columns = [value_symbol]
	return df

def live_price_matrix(coin_symbols=['ETH','BTC','USD'], exchange=''):
	"""
	returns a live price matrix of coins
	to do:
	sort dict or dataframe
	"""
	url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'\
			.format(','.join(coin_symbols).upper(), ','.join(coin_symbols).upper())

	if exchange:
		url += '&e={}'.format(exchange)
	
	data 	= url_to_dict(url)
	df = pd.DataFrame.from_dict(data,orient='index')
	#df.columns = [value_symbols]
	return df

def live_data_dump(coin_symbols=['ETH','BTC','USD'], exchange=''):
	"""
	returns a dict of dataframes.  Each keys is a coin symbol. 
	to do:
	- write doc example
	- filter dfs/refine format
	- sort dict/dataframe entries
	"""
	url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}'\
			.format(','.join(coin_symbols).upper(), ','.join(coin_symbols).upper())
	if exchange:
		url += '&e={}'.format(exchange)
	
	data 	= url_to_dict(url)['RAW']
	
	df_dict = dict()
	for k,v in data.items():
		df_dict[k] = pd.DataFrame.from_dict(v)
	return df_dict

def live_twitter(coin_symbols=['ETH','BTC']):
	"""
	returns df of twitter data for given coin symbols
	"""
	ids = list(coin_list().loc[coin_symbols]['Id'])
	dfs = []
	for j, id in enumerate(ids):
		res = requests.get('https://www.cryptocompare.com/api/data/socialstats/?id='+id)
		df = pd.DataFrame.from_dict(res.json()['Data']['Twitter'],orient='index')
		df.columns = [coin_symbols[j]]
		dfs.append(df)
	
	df = pd.concat(dfs, axis=1)
	return df

def live_reddit(coin_symbols=['ETH','BTC']):
	"""
	returns df of reddit data for given coin symbols
	"""
	ids = list(coin_list().loc[coin_symbols]['Id'])
	dfs = []
	for j, id in enumerate(ids):
		res = requests.get('https://www.cryptocompare.com/api/data/socialstats/?id='+id)
		df = pd.DataFrame.from_dict(res.json()['Data']['Reddit'],orient='index')
		df.columns = [coin_symbols[j]]
		dfs.append(df)
	
	df = pd.concat(dfs, axis=1)
	return df

def live_facebook(coin_symbols=['ETH','BTC']):
	"""
	returns df of facebook data for given coin symbols
	"""
	ids = list(coin_list().loc[coin_symbols]['Id'])
	dfs = []
	for j, id in enumerate(ids):
		res = requests.get('https://www.cryptocompare.com/api/data/socialstats/?id='+id)
		df = pd.DataFrame.from_dict(res.json()['Data']['Facebook'],orient='index')
		df.columns = [coin_symbols[j]]
		dfs.append(df)
	
	df = pd.concat(dfs, axis=1)
	return df

def price_history(coin='ETH', unit_coin='USD', unit_time='minute', exchange=''):
	"""
	returns price history by minute of value_coin in units of unit_coin.
	parameters: 
	coin: 		'ETH','BTC',...
	unit_coin:	'ETH','BTC',...
	unit_time:	'mintue','hour','day'
	to do:
	- example:
	"""
	#url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}&e={}'
	url = 'https://min-api.cryptocompare.com/data/histo{}?fsym={}&tsym={}'.format(unit_time, coin.upper(), unit_coin.upper())
	if exchange:
		url += '&e={}'.format(exchange)
	
	data 	= url_to_dict(url)['Data']
	df 		= pd.DataFrame(data)
	return df

def mining_info():
	url = 'https://www.cryptocompare.com/api/data/miningequipment/'

	mining_data = url_to_dict(url)['MiningData']
	coin_data 	= url_to_dict(url)['CoinData']	
	df1 		= pd.DataFrame(mining_data).T
	df2 		= pd.DataFrame(coin_data)
	
	return [df1, df2]


# def live_github(coin_symbols=['ETH','BTC']):
# 	"""
# 	returns df of github data for given coin symbols
# 	"""
# 	ids = list(coin_list().loc[coin_symbols]['Id'])
# 	dfs = []
# 	for j, id in enumerate(ids):
# 		res = requests.get('https://www.cryptocompare.com/api/data/socialstats/?id='+id)
# 		value = res.json()['Data']['CodeRepository']['Points']
		
# 		df = pd.DataFrame.from_dict(value,orient='columns')			
# 		df.columns = [coin_symbols[j]]
# 		dfs.append(sub_df)
	
# 	df = pd.concat(dfs, axis=1)
# 	return df
