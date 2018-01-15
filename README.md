# Description
Cryptic is a suite for real-time cryptocurrency analysis that includes API data collection and analysis definitions that provide insight to the evolving cryptocurrency market.

# Getting started
- in terminal: `git clone https://github.com/tcrensink/cryptic.git`
- in `~/.bash_rc` or `~/.profile_rc`, add folder to your python path, e.g: `export PYTHONPATH="path/to/Cryptic:$PYTHONPATH"
`
- see scripts in `examples` folder

# Organization
- https://tcrensink.github.io/cryptic/ or `./docs`: wiki-like notes, analysis, and reference
- `cryptic`: package definitions for API data extraction and analysis tools.
- `examples`: simple, ready-to-run examples that demonstrate the cryptic module
- `data`: read-only storage of (dated) dataframe data.
- `analysis`: analysis based on `data`; figure/plot output and the scripts required to generate them.

# Workflow (in progress)
- pandas dataframes created from API calls
- dataframes dated and saved to `./data`
- (optional) dataframes merged to a master DataFrame for convenient analysis
- write stand alone output to analysis
- figures embedded into wiki as desired

# Data
Included quantitative and sentiment data, collected from exchanges and social media platforms (reddit, facebook, twitter).  

API sources include:
- https://www.cryptocompare.com (exchanges, twitter, reddit, Facebook)
- https://binance.com
- https://kucoin.com

# Mining sources
- [multipool](https://www.multipool.us)
- [fairpool](https://fairpool.xyz)

