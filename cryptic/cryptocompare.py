from cryptic.util_functions import *
from cryptic.default_parameters import *
import os
# import sys
# import urllib.parse

"""
data from: https://www.cryptocompare.com/api.  Functions are based on API calls.

SUMMARY OF MODULE CONTENTS:

def coin_data():    
def live_price(coin_sym='ETH', unit_syms=['USD','BTC'], exchange=''):
def live_price_matrix(coin_syms=default_coins, exchange=''):
def live_data_dump(coin_syms=default_coins, exchange=''):
def live_twitter(coin_syms=default_coins):
def live_reddit(coin_syms=default_coins):
def live_facebook(coin_syms=default_coins):
def price_history(coin='ETH', unit_coin='USD', unit_time='minute', exchange=''):
def mining_info():
    
To Do:
- clean df cols, types
- convert live_data_dump to multi-indexed df
"""


# tsym != tsyms.
def get_coin_url(coin='ETH', units=['USD', 'BTC'], exchange=default_exchange):
    formatted_input = '?fsym={coin}&tsyms={units}&e={exchange}'
    if not isinstance(coin, str):
        coin = ','.join(coin)
        formatted_input = '?fsyms={coin}&tsyms={units}&e={exchange}'
    return formatted_input.format(coin=coin,
                                  units=','.join(units),
                                  exchange=exchange)


def coin_data():
    """
    returns dataframe of cryptocurrency coin info.
    
    Parameters: (None)

    Description:
    Id (int):       The internal id, this is used in other calls
    Url (string):   The url of the coin on cryptocompare
    ImageUrl (str): The logo image of the coin
    Name (str):     The symbol
    CoinName (str): The name
    FullName (str): A combination of the name and the symbol
    Algorithm (str):The algorithm of the cryptocurrency
    ProofType (str):The proof type of the cryptocurrency
    SortOrder (int):The order we rank the coin inside our internal system
    """
    url = "https://www.cryptocompare.com/api/data/coinlist/"
    df = url_to_dataframe(url)
    df = df.T
    numeric_cols = ['FullyPremined', 'Id', 'SortOrder', 'TotalCoinSupply']
    df = numerify(df, numeric_cols)
    #df.url = url
    return df


def price_history(time_interval='minute', coin='ETH', unit='USD', N=2000, aggregate=0, exchange=default_exchange, datetime_obj=None):
    """
    https://www.cryptocompare.com/api/#-api-data-histohour-
    returns price history at minute of value_coin in units of unit_coin:
    parameters:
    coin:                   'ETH','BTC',...
    unit:                   'ETH','BTC',...
    time_interval:          'minute','hour','day'
    aggregate:              1,10 (aggregates (averages?) data points)
    N (limit):              number rows of data to retrieve
    datetime_obj (toTs):    datetime.datetime.now()

    tryConversion:  (not incl) if set to 'false', will not use intermediate coins to return price hist. 
    sign:           (not incl) will sign server requests if included

    #TODO 
    - use coin = 'USD', units=['ETH','BTC',...] to get more data with each call?
    - add time
    """
    if datetime_obj is None:
        timestamp = datetime.datetime.now().timestamp()
    else:
        timestamp = datetime_obj.timestamp()

    url = 'https://min-api.cryptocompare.com/data/histo{}?fsym={}&tsym={}&limit={}&aggregate={}&e={}&toTs={}'.format(time_interval, coin.upper(), unit.upper(), N, aggregate, exchange, int(timestamp))

    df              = url_to_dataframe(url)
    df['time']      = pd.to_datetime(df.loc[:,'time'], unit='s')
    df.set_index('time',inplace=True)
    
    # metadata
    # df.args = dict(time_interval=time_interval, coin=coin.upper(), unit=unit.upper(), N=N, aggregate=aggregate, exchange=exchange, datetime_obj=datetime_obj)
    df.url = url
    return df

    
def read_price_history(fname='ETH_in_USD_by_minute_on_CCCAGG.pkl'):
    """
    if file exists, returns df; else returns None

    TO DO:
    verify that fpath has correct format
    """
    file_path = '../data/' + fname
    
    if os.path.exists(file_path):
        #df_main = pd.read_csv(file_path, parse_dates=['time'], date_parser = pd.to_datetime , index_col='time')
        df_main = pd.read_pickle(file_path)
        return df_main

    else:
        return None 


def write_price_history(df, file_extension='pkl'):
    """
    writes or appends/merges df = cc.price_history() to pickle file.  Filename is parsed from url attribute kept in df; this attribute is wiped on write.  

    Example: 
    df = cc.price_history()
    cc.write_price_history(df)
        
    TO DO:
    - warn/stop if record conflict are found
    - write merge failsafes: same columns index ?, same index type as existing df?  Warn/abort on conflicting records.
    - prevent metadata from being wiped?  Keep a log of metadata?
    """
    
    # path = '../data/' + '{}_in_{}_by_{}_on_{}.{}'.format(coin, unit, time_interval, exchange, filetype)

    p = url_to_params(df.url)
    fname = '{}_in_{}_by_{}_on_{}.{}'.format(p['coin'], p['unit'], p['time_interval'], p['exchange'], file_extension)
    file_path = '../data/' + fname
    
    df_orig = read_price_history(fname)
    if df_orig is None:
        open(file_path, 'x')
        print('no previous data; writing new file from current dataframe.')
        df_updated = df
    else:
        print('appending current df to:')
        print(file_path)
        df_updated = df.combine_first(df_orig)

    # df_updated.to_csv(file_path)
    df_updated.to_pickle(file_path)


# corrupted.
# def live_price(coin='ETH', units=['USD', 'BTC'], exchange=default_exchange):
#     """
#     Gets the price of a currency against multiple currencies.

#     Parameters:
#     coin_sym (str):             coin of interest
#     unit_syms (list of str):    unit coins
#     exchange (str):             currency exchange

#     return the value of coin1 in units [coin2,coin3,...coinN].
    
#     Example:
#     live_price(value)
    
#     #TODO add exchange to index
#     """
#     # spec_coin_url = get_coin_url(coin=coin,
#     #                              units=units,
#     #                              exchange=exchange)
#     # url = '{base_url}/price{coin_url}'.format(base_url=get_base_url(),
#                                               # coin_url=spec_coin_url)

#     url = url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}'\
#             .format(coin.upper(), units.upper(), limit, aggregate)
#     data = url_to_dict(url)
#     df = pd.DataFrame(data, index=[coin])
#     #df.columns = units
#     #df.url = url
#     return df


def live_price_matrix(coins=default_coins, exchange=default_exchange):
    """
    Returns matrix of coin exchange prices.  The exchange

    Parameters:
    coins (list of str):Coin symbols for matrix
    exchange (str):         Exchange that data is pulled from.

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

    # df_dict['url']    = url
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