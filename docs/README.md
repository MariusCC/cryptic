CRYPTIC

# organization
Cryptic collects up-to-date data from website APIs and provides analytic tools to assess "alt-coin" cryptocurrencies for investment purposes.  Provisional workflow:

- notes, analysis, and conclusions (markdown) kept at `./docs`.  Viewable at: https://tcrensink.github.io/cryptic/
- each API endpoint is stored in a unique pandas DataFrame and regularly updated (in `./data`)
- DataFrames merged to a master DataFrame for convenient analysis (`./data`)
- shared class/functions stored in `./lib`
- ready-to-run scripts in `./analysis`
- rough code in `testcode.py`

# data
Interested in quantitative and sentiment data to discover and assess trends.  Partial api source list:

- https://coinmarketcap.com/api/
- https://www.cryptocompare.com/api/
- https://www.cryptocompare.com/api/?javascript#-api-data-pricehistorical-
- http://alt19.com/
- http://alt19.com/marketindexes.html 