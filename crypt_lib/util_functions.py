import requests
import json
import pandas as pd
import datetime
import urllib
# import io

def url_to_fname(url):
	"""
	formats/parses url to make valid, creation-dated filename
	"""
	url_parts = urllib.parse.urlparse(url)
	#fname = ''.join([c if c.isalnum() else '_' for c in url])
	fn1 = url_parts.netloc.replace('www.', '').replace('.com','')
	fn2 = url_parts.path.replace('/', '_')
	fn3 = url_parts.query.replace('/', '_')

	date_str = datetime.datetime.now().strftime('%Y%m%d')

	fname = fn1 + fn2 + fn3 + date_str
	return fname


def url_to_dataframe(url, json_key='Data'):
	"""
	extract url data into pandas df.  RPC requests may return data in slightly different forms; this function tries to "smartly" convert request data to dataframe.  The original url request is saved as attribute `url`.
	
	example:
	url = 'https://www.cryptocompare.com/api/data/coinlist/'
	df = url_to_dataframe(url)
	df.url
	"""
	res = requests.get(url)
	if res.status_code != 200:
		print('Error in request!')
		return None
	try:
		#df = pd.read_json(res.content)
		data 	= res.json()[json_key]
		df 		= pd.DataFrame.from_dict(data)
	except KeyError:
		print('there was an error loading req.json()[\'Data\'] to df.') 
		print('list of available keys:')
		print(res.json().keys())
		# data = json.loads(res.content)
		# df = pd.DataFrame.from_dict(data['Data'])
	
	df.url = url	
	return df


def url_to_dict(url):
	"""
	return values from rpc request.	
	to do:
	add example
	add error handling
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
	fname 	= url_to_fname(df.url) + '.csv'
	path 	= '../data/'
	
	df.to_csv(path + fname)	
	if silent == False:
		print('\nsaved to: ' + path + fname)


def load_dataframe(url, date_str=None, silent=False):
	"""
	looks in data folder for saved dataframe matching url and date.  Will look for df created today if date_str is not given.
	date_str format: 'yyyymmdd'	
	to do:
	- add example
	- exception handling
	"""
	if date_str is not None:
		#parse fname
		base_name = url_to_fname(url)[:-8]
		fname 	= base_name + date_str + '.csv'

	else: 
		fname 	= url_to_fname(url) + '.csv'

	path = '../data/'
	
	pd.read_csv(path + fname)

	if silent == False:
		print('df read from ' + path + fname)
	return df

def call_apis():
	"""
	automates api calls	
	# scheduled api calls to retrieve new data
	# https://pypi.python.org/pypi/schedule
	# https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
	"""
	pass


def inspect_response(url):
	"""
	guided inspection of url request data
	"""
	pass

