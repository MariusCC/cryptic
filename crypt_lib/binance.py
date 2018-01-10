from util_functions import *
"""
create dbs from api:
https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md
"""

def binance_df():
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

	for record in data:

		df_row = pd.DataFrame.from_dict(record, orient='index').T
		df = pd.concat([df, df_row], axis=0)

	df.index = df.symbol
	return df


