from cryptic.util_functions import *
from cryptic.default_parameters import *

base_url = 'https://min-api.cryptocompare.com/data/'
endpoints = ['pricehistorical?fsym=ETH&tsyms=BTC,USD&ts=1452195664&extraParams=your_app_name',
             'histoday?fsym=BTC&tsym=USD&limit=30&aggregate=1']

dfs = url_to_dataframe(base_url, endpoints)

for j, df in enumerate(dfs):
    fname = 'cryptocompare_df' + str(j)
    save_df(df1, fname)

# df2 = url_to_df(base_url + endpoint1)
# save_df(df2,'cryptocompare_histoday')
