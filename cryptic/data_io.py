"""
retrieves needed data either from saved data store or from API call
"""

def call_API(function):
	"""
	based on passed function, retrieves data either from data folder or new API call	
	Parameters:
	function (function): name of function to evaluate
	return (bool):	call API or not
	"""
	if function == 'coin_data':
		pass
	if function == 'live_price':
		pass
	# etc
	#return True

def append_dataframe_rows(df, df_new):
	"""
	append df_new rows to df to dataframe
	"""
	pass