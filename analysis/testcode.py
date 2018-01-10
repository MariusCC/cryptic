"""
tmp code buffer for debugging, frequently overwritten.
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
See slack channel: #tools

SENTIMENT DATA:
"/1.1/search/tweets.json?q=from%3ANasa%20OR%20%23nasa"
http://www.livecryptotweets.com
http://www.livecryptotweets.com/#.WlZkmBovbrE.link
 google trends?
"""


#EXAMPLE 2: histogram of percent change vs time:
df['percent_change_24h'].dropna().hist()
df['percent_change_7d'].dropna().hist()










#useful functions:

#check for nans in entries
pd.isnull(df)
df.dropna() 	#dropx rows with nans














