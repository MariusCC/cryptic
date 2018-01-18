import requests
import json
import pandas as pd
import datetime
import urllib
import datetime
# import io

"""
Description: helper functions used by website api modules.
"""


# rename module to "API_functions.py"

def refresh():
    """
    automates api calls
    # scheduled api calls to retrieve new data
    # https://pypi.python.org/pypi/schedule
    # https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
    """
    pass

def url_to_fname(url):
    """
    formats/parses url to make valid, creation-dated filename
    """
    url_parts = urllib.parse.urlparse(url)
    # fname = ''.join([c if c.isalnum() else '_' for c in url])
    fn1 = url_parts.netloc.replace('www.', '').replace('.com', '')
    fn2 = url_parts.path.replace('/', '_')
    fn3 = url_parts.query.replace('/', '_')
    fname = fn1 + fn2 + fn3 + get_date_str()
    return fname

def url_to_params(url):
    """
    Input:  price_hist() url
    Output: dict of parameters names and values, including:
    coin
    unit
    time_interval
    exchange
    N
    aggregate
    toTs
    TO DO:
    - either append datetime object, or deal with timestamps everywhere
    """
    param_codes = {'fsym':'coin', 'tsym':'unit', 'limit':'N', 'aggregate':'aggregate', 'toTs':'timestamp', 'e':'exchange'}
    
    base_url, endpoint  = url.split('?')
    time_interval = base_url.split('histo')[1]
    
    param_list  = endpoint.split('&')    
    param_list  = [s.split('=') for s in param_list]
    params = [[param_codes[s[0]],s[1]] for s in param_list]
    params.append(['time_interval', time_interval])
    return dict(params)    


def social_url():
    return 'https://www.cryptocompare.com/api/data/socialstats/?id={id}'


def get_base_url():
    return 'https://min-api.cryptocompare.com/data'


def numerify(df=None, numeric_cols=None):

    for k in numeric_cols:
        df.loc[:, k] = df.loc[:, k].apply(pd.to_numeric, errors='coerce')
    return df


def to_datetime(series, unit='s'):
    """
    basic wrapper for pd.to_datetime.

    Parameters:
    series (type=pd.Series) 
    unit (type=str), {'s','ns',...}.  Unit of timestamps
    Returns: datetime Series 

    Example: 
    (pending)
    df.timeseries = pd.to_datetime()
    """
    return pd.to_datetime(series, unit=unit)    


def to_timeSeries(datetime, time_unit='minute'):
    """
    Parameters: 
    datetime (type=pd.Series): datetime objects
    time_unit (str): time unit of output Series
    ['year', 'quarter', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'nanosecond']
    
    Returns: Series of time_unit values 

    Example: 
    equivalent of, e.g.: datetime.dt.minute
    """
    return getattr(datetime.dt, time_unit)


# def to_epoch(timestamp):
#     """converts datetime_index to unix epoch
#     Example:
#     timestamps = pd.date_range('2018-01-16 09:15:05', periods=4, freq='H')
#     """
#     stamps.view('int64') // pd.Timedelta(1, unit='s')


def get_date_str():
    """
    returns yyyymmdd datestring
    """
    return datetime.datetime.now().strftime('%Y%m%d')


def url_to_dataframe(url, json_key='Data'):
    """
    extract url data into pandas df.  RPC requests may return data in slightly different forms; this function tries to "smartly" convert request data to dataframe.  The original url request is saved as attribute `url`.
    example:
    url = 'https://www.cryptocompare.com/api/data/coinlist/'
    df = url_to_dataframe(url)
    df.url
    
    """
    url_res = url_to_dict(url)
    try:
        # df = pd.read_json(res.content)
        data = url_res[json_key]
        df = pd.DataFrame.from_dict(data)
    except KeyError:
        print('there was an error loading req.json()[\'Data\'] to df.')
        print('list of available keys:')
        print(url_res.json().keys())
    # data = json.loads(res.content)
    # df = pd.DataFrame.from_dict(data['Data'])

    df.url = url
    return df


def url_to_dict(url):
    """
    return values from rpc request.	
    to do:
    - add example
    - add error handling
    """
    res = requests.get(url)
    if res.status_code != 200:
        print('Error in request!')
        return None

    return res.json()


def save_dataframe(df, silent=False):
    """
    save dataframe to ./data named url_to_fname(url).csv
    example: 
    url = 'https://www.cryptocompare.com/api/data/coinlist/'	
    df = url_to_dataframe(url)
    save_dataframe(df)
    
    to do:
    - check if file exists before writing
    - add path parameter
    """
    path = '../data/'
    fname = url_to_fname(df.url) + '.csv'

    df.to_csv(path + fname)
    if silent is False:
        print('\nsaved to: ' + path + fname)


def load_dataframe(url, date_str=get_date_str(), silent=False):
    """
    looks in data folder for saved dataframe matching url and date.  Will look for current df if date_str is not given.
    date_str format: 'yyyymmdd'	
    to do:
    - load by filename (w/wo date)
    - date_str=None -> fname has no date in it
    - add example
    - exception handling
    """
    path = '../data/'

    if date_str is not 'today':
        # parse fname
        base_name = url_to_fname(url)[:-8]
        fname = base_name + date_str + '.csv'
    else:
        fname = url_to_fname(url) + '.csv'

    df = pd.read_csv(path + fname)
    if silent is False:
        print('df read from ' + path + fname)
    return df
