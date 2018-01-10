import sys
from util_functions import *

base_url = 'https://api.coinmarketcap.com/v1/ticker/'
endpoint = '?limit=0'

df = urls_to_dataframes(base_url,endpoint)
save_df(df,'coinmarketcap')

