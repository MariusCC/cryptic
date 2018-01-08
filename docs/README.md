# cryptic basic framework
This repo is a suite of tools for up-to-date analysis of alt-coins.  Provisional workflow:

- website APIs from various sources will collect data live, and saved in a pandas DataFrame (stored in `data`)
- DFs (will be) merged to a master DataFrame for convenience (also in `data`)
- Analysis/query definitions and classes developed to query the DF stored in `./lib`
- ready-to-run scripts and notes kept in `./analysis`
- notes, write-ups, and conclusions can be contributed in `./docs`
- rough code in `testcode.py`

# data
Interested in quantitative and sentiment data to discover and assess trends.  Partial api source list:

- https://coinmarketcap.com/api/
- https://www.cryptocompare.com/api/
- https://www.cryptocompare.com/api/?javascript#-api-data-pricehistorical-
- http://alt19.com/
- http://alt19.com/marketindexes.html 