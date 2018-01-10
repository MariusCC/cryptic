from util_functions import *
from cryptocompare import *
from pprint import pprint

#EXAMPLE 1: relative prices
print('price matrix of 5 (random) coins:')
coin_symbols = coin_list().sample(n=5).index.tolist()
price_matrix = live_price_matrix(coin_symbols=coin_symbols)
print(price_matrix)

