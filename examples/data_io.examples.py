import cryptocompare as cc
from util_functions import *


#APPEND MINUTE, DAILY DATA:
df = cc.price_history()
cc.write_price_history(df,'ETH', 'USD', 'minute', 'CCCAGG')

df = cc.price_history(time_interval='day')
cc.write_price_history(df, coin='ETH', unit='USD', time_interval='day', exchange='CCCAGG')