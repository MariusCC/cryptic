"""
tmp code buffer for testing new ideas; no expectation that this code will be saveds.
"""
import requests
import pandas as pd
import numpy as np
import time
import datetime
import random
import json
from pprint import pprint
import io
import matplotlib.pyplot as plt
"""
things to write now:
-X price history for one coin
- price history (from exchange open) of many coins
- price history of sentiment data

things to write later:
- arbitrage between exchanges
- 2D plot of price difference, t1,t2
	- statistics on how frequently differences arise?

"""




Examples:
import 
coin_data = 
syms = list(coin_data.Symbol.sample(n=20))

#EXAMPLE 2: histogram of percent change vs time:
#df['percent_change_24h'].dropna().hist()
#df['percent_change_7d'].dropna().hist()










#useful functions:

#check for nans in entries
pd.isnull(df)
df.dropna() 	#dropx rows with nans














