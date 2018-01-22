from cryptic import cryptocompare as cc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def plot_price_history(path='ETH_in_USD_by_minute_on_CCCAGG.pkl', df=None, url=None):
	"""
	plot from df, API call, or pkl file; default is ETH minute data saved in pkl
	"""	
	if df is None and url is None:

		df = pd.read_pickl(path)

	if df is not None:
		pass
	
	elif url is not None:
		

	df = cc.price_history()
	
	ax = df['close'].plot()
	#ticklabels = df.index.strftime('%Y-%m-%d')
	#ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
	ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
	plt.show()
	plt.draw()




