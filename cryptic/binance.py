from cryptic.util_functions import *
from cryptic.default_parameters import *
"""
create dbs from api:
https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md

examples: https://github.com/sammchardy/python-binance/blob/master/examples/save_historical_data.py
"""

def test_connection():
	"""
	valid response from binance api server?
	"""
	res = requests.get('https://api.binance.com/api/v1/ping')
	if res.status_code == 200:
		print('successfully pinged binance api.')
	else:
		print('error connecting with binance api.')

def exchange_data():
	"""
	returns binance api data.  Example of column data:
	example:
	df.iloc[0]
	symbol 				ETHBTC
	status				TRADING
	baseAsset			ETH
	baseAssetPrecision 	8
	quoteAsset			BTC
	orderTypes			[LIMIT, LIMIT_MAKER,...]
	icebergAllowed		True
	filters 			#dict of filters
	"""
	url =  'https://api.binance.com/api/v1/exchangeInfo'

	res 	= requests.get(url).json()
	data 	= res['symbols']

	df = pd.DataFrame()
	for record in data:

		df_row = pd.DataFrame.from_dict(record, orient='index').T
		df = pd.concat([df, df_row], axis=0)

	df.index = df.symbol
	return df

def candle_data(sym='',interval=''):

	res = requests.get('https://api.binance.com/api/v1/klines?&symbol=LTCBTC')

	res = requests.get('https://api.binance.com/api/v1/klines/symbol=LTCBTC').json()

