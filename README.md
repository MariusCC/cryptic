# Description
Cryptic collects live from website APIs and provides analytic tools to assess "alt-coin" cryptocurrencies for investment purposes.

# Organization:
- https://tcrensink.github.io/cryptic/, `./docs`: wiki-like notes, analysis, and reference
- `crypt_lib`: definitions for API data extraction and analysis tools.
- `analysis`: ready-to-run examples and analysis scripts
- `data`: read-only storage of (dated) dataframe data.
- `output`: saved output figures and scripts to recreate them.  `data` is only dependency.

# Workflow (in progress):
- pandas dataframes created from API calls
- dataframes dated and saved to `./data`
- (optional) dataframes merged to a master DataFrame for more convenient analysis

# Data sources
(partial) API source list:
- https://www.cryptocompare.com/api/
- https://api.binance.com/api/
