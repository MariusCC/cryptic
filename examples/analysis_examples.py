import cryptocompare as cc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def plot_price_history():
	"""
	template to finish, from SO
	"""	
	df = cc.price_history()
	ax = df['close'].plot()
	#ticklabels = df.index.strftime('%Y-%m-%d')
	#ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
	ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
	plt.show()
	plt.draw()




