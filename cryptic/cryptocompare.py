from cryptic.util_functions import *
from cryptic.default_parameters import *

# import sys
# import urllib.parse

"""
data from: https://www.cryptocompare.com/api.  Functions are based on API calls.

SUMMARY OF MODULE CONTENTS:

def coin_data():
	Returns dataframe of cryptocurrency coin info.
	
def live_price(coin_sym='ETH', unit_syms=['USD','BTC'], exchange=''):
	Gets the price of a currency against multiple currencies.

def live_price_matrix(coin_syms=default_coins, exchange=''):
	Returns a live price matrix of coins
	
	
def live_data_dump(coin_syms=default_coins, exchange=''):
	Returns a dict of dataframes.  Each keys is a coin symbol. 
	
def live_twitter(coin_syms=default_coins):
	returns df of twitter data for given coin symbols

def live_reddit(coin_syms=default_coins):
	returns df of reddit data for given coin symbols
	
def live_facebook(coin_syms=default_coins):
	returns df of facebook data for given coin symbols
	
def price_history(coin='ETH', unit_coin='USD', unit_time='minute', exchange=''):
	returns price history by minute of value_coin in units of unit_coin.
	
def mining_info():
	returns mining info
	
To Do:
- convert columns to correct numeric type
- convert live_data_dump to type df

-  'https://www.cryptocompare.com/api/data/CoinSnapshot?fsym=ETH&tsyms=USD'
- https://www.cryptocompare.com/api#-api-data-coinsnapshot-
- https://min-api.cryptocompare.com/data/top/pairs?fsym=ETH
"""

exchanges = ['Cryptsy', 'BTCChina', 'Bitstamp',
             'BTER', 'OKCoin', 'Coinbase',
             'Poloniex', 'Cexio', 'BTCE',
             'BitTrex', 'Kraken', 'Bitfinex',
             'Yacuna', 'LocalBitcoins', 'Yunbi',
             'itBit', 'HitBTC', 'btcXchange',
             'BTC38', 'Coinfloor', 'Huobi',
             'CCCAGG', 'LakeBTC', 'ANXBTC',
             'Bit2C', 'Coinsetter', 'CCEX',
             'Coinse', 'MonetaGo', 'Gatecoin',
             'Gemini', 'CCEDK', 'Cryptopia',
             'Exmo', 'Yobit', 'Korbit',
             'BitBay', 'BTCMarkets', 'Coincheck',
             'QuadrigaCX', 'BitSquare', 'Vaultoro',
             'MercadoBitcoin', 'Bitso', 'Unocoin',
             'BTCXIndia', 'Paymium', 'TheRockTrading',
             'bitFlyer', 'Quoine', 'Luno',
             'EtherDelta', 'bitFlyerFX', 'TuxExchange',
             'CryptoX', 'Liqui', 'MtGox', 'BitMarket',
             'LiveCoin', 'Coinone', 'Tidex', 'Bleutrade',
             'EthexIndia', 'Bithumb', 'CHBTC',
             'ViaBTC', 'Jubi', 'Zaif',
             'Novaexchange', 'WavesDEX', 'Binance',
             'Lykke', 'Remitano', 'Coinroom',
             'Abucoins', 'BXinth', 'Gateio',
             'HuobiPro', 'OKEX']


def social_url():
    return 'https://www.cryptocompare.com/api/data/socialstats/?id={id}'


def get_base_url():
    return 'https://min-api.cryptocompare.com/data'


# tsym != tsyms.
# def get_coin_url(coin='ETH', units=['USD', 'BTC'], exchange=default_exchange):
#     formatted_input = '?fsym={coin}&tsyms={units}&e={exchange}'
#     if not isinstance(coin, str):
#         coin = ','.join(coin)
#         formatted_input = '?fsyms={coin}&tsyms={units}&e={exchange}'
#     return formatted_input.format(coin=coin,
#                                   units=','.join(units),
#                                   exchange=exchange)


def coin_data():
    """
    returns dataframe of cryptocurrency coin info.
    
    Parameters: (None)

    Description:
    Id (int):		The internal id, this is used in other calls
    Url	(string):	The url of the coin on cryptocompare
    ImageUrl (str): The logo image of the coin
    Name (str): 	The symbol
    CoinName (str):	The name
    FullName (str):	A combination of the name and the symbol
    Algorithm (str):The algorithm of the cryptocurrency
    ProofType (str):The proof type of the cryptocurrency
    SortOrder (int):The order we rank the coin inside our internal system
    """
    url = "https://www.cryptocompare.com/api/data/coinlist/"
    df = url_to_dataframe(url)
    df = df.T
    df.iloc[:,[3,4,9,12]] = df.iloc[:,[3,4,9,12]].astype(int, errors='ignore')
    #df.url = url
    return df


def price_history(unit_time='minute', coin='ETH', units='USD', limit=2000, aggregate=1, exchange=default_exchange):
    """
    returns price history by minute of value_coin in units of unit_coin.
    parameters: 
    coin: 		'ETH','BTC',...
	units:	'ETH','BTC',...
	unit_time:	'minute','hour','day'
	#TODO 
    - merge with existing dataframes
    - example:
    """
    url = 'https://min-api.cryptocompare.com/data/histo{}?fsym={}&tsym={}&limit={}&aggregate={}&e={}'.format(unit_time, coin, units, limit, aggregate, exchange)

    df          = url_to_dataframe(url)
    tstamps     = pd.to_datetime(10**9*df.time)
    df          = df.assign(timestamps=tstamps)
    df.index    = df.timestamps

    return df


def live_price(coin='ETH', units=['USD', 'BTC'], exchange=default_exchange):
    """
    Gets the price of a currency against multiple currencies.

    Parameters:
    coin_sym (str): 			coin of interest
    unit_syms (list of str):	unit coins
    exchange (str):				currency exchange

    return the value of coin1 in units [coin2,coin3,...coinN].
    
    Example:
    live_price(value)
    
    #TODO add exchange to index
    """
    spec_coin_url = get_coin_url(coin=coin,
                                 units=units,
                                 exchange=exchange)
    url = '{base_url}/price{coin_url}'.format(base_url=get_base_url(),
                                              coin_url=spec_coin_url)

    data = url_to_dict(url)
    df = pd.DataFrame(data, index=[coin])
    #df.columns = units
    #df.url = url
    return df


def live_price_matrix(coins=default_coins, exchange=default_exchange):
    """
    Returns matrix of coin exchange prices.  The exchange

    Parameters:
    coins (list of str):Coin symbols for matrix
    exchange (str):			Exchange that data is pulled from.

    Description of content:
    Returns a price matrix based on 

    to do:
    - skip coins that error, issue warning
    """
    base_url = get_base_url()
    spec_coin_url = get_coin_url(coin=coins,
                                 units=coins,
                                 exchange=exchange)
    url = '{base_url}/pricemulti{coin_url}'.format(base_url=base_url,
                                                   coin_url=spec_coin_url)

    data = url_to_dict(url)
    df = pd.DataFrame.from_dict(data, orient='index')
    # df.columns = [value_symbols]
    df.sort_index(inplace=True)
    df.sort_index(axis=1, inplace=True)
    df.url = url
    df.exchange = exchange
    return df


def live_data_dump(coins=default_coins, exchange=default_exchange):
    """
    returns a dict of dataframes.  Each keys is a coin symbol. 
    to do:
    - write doc example
    - filter dfs/refine format
    - sort dict/dataframe entries
    """
    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}&e={}' \
        .format(','.join(coins).upper(), ','.join(coins).upper(), exchange.upper())
    data = url_to_dict(url)['RAW']

    df_dict = dict()
    for k, v in data.items():
        df_dict[k] = pd.DataFrame.from_dict(v).T

    # df_dict['url'] 	= url
    return df_dict


def live_social(input_coin_data=coin_data(), coins=default_coins,
                social_media='Twitter'):
    """
    Returns df of data from social feed for given coin symbols
    
    #TODO deal with multiple sites for CodeRepository
    """
    coin_id_df = input_coin_data.loc[coins, ['Name', 'Id']].dropna()

    dfs = []
    for index, coin_row in coin_id_df.iterrows():
        res = requests.get(social_url().format(id=int(coin_row['Id'])))
        df = pd.DataFrame.from_dict(res.json()['Data'][social_media],
                                    orient='index')
        df.columns = [coin_row['Name']]
        dfs.append(df)

    df = pd.concat(dfs, axis=1)
    df.url = social_url()
    return df.T

def mining_info():
    url = 'https://www.cryptocompare.com/api/data/miningequipment/'

    mining_data = url_to_dict(url)['MiningData']
    coin_data = url_to_dict(url)['CoinData']
    df1 = pd.DataFrame(mining_data).T
    df2 = pd.DataFrame(coin_data)
    # df.url = url
    return [df1, df2]