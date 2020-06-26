## All CryptoCompare Symbols and Stats
import pandas as pd
import json, urllib.request

# Download Coin Names and Stats from CryptoCompare
# https://min-api.cryptocompare.com/documentation?key=Other&cat=allExchangesV2Endpoint
url = 'https://www.cryptocompare.com/api/data/coinlist/'
data = urllib.request.urlopen(url).read().decode('utf8')
data = json.loads(data)
data = pd.DataFrame(data['Data']).T

# Convert str to int with "N/A" as NaN
data.FullyPremined = data.FullyPremined.apply(pd.to_numeric, errors='coerce') 
data.BuiltOn = pd.to_numeric(data.BuiltOn, downcast='integer', errors='coerce')
data.Id = data.Id.apply(pd.to_numeric, errors='coerce') 
data.SortOrder = data.SortOrder.apply(pd.to_numeric, errors='coerce') 
data.TotalCoinSupply = data.TotalCoinSupply.apply(pd.to_numeric, errors='coerce') 

# Sort by "SortOrder"
data = data.sort_values("SortOrder")
data['BuiltOn'] = data['BuiltOn'].fillna(data['Id'])
print(data)