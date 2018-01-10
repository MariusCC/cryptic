from util_functions import *
from cryptocompare import *
from pprint import pprint

"""
Repository of Simple Examples.
API data from each site has its own organizational scheme.  Snippets are organized by website as useful examples from the derived databases.
"""

#CRYPTOCOMPARE

#EXAMPLE 1: relative prices
print('price matrix of 5 (random) coins:')
coin_symbols = coin_list().sample(n=5).index.tolist()
price_matrix = live_price_matrix(coin_symbols=coin_symbols)
print(price_matrix)


#EXAMPLE 2: histogram of percent change vs time:
df['percent_change_24h'].dropna().hist()
df['percent_change_7d'].dropna().hist()


#EXAMPLE 3: 