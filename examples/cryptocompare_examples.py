import cryptic.cryptocompare as cc
from cryptic.default_parameters import *
"""
Examples using cryptocompare data
"""

# Get basic data from all functions:
coin_data = cc.coin_data()


coin_syms = list(coin_data.Symbol.sample(n=20))


# Get price matrix of 20 random coins



#Price matrix
price_matrix = cc.live_price_matrix(coin_syms=coin_syms)
print(price_matrix)









#if __name__ == "__main__":
	
	#run examples