import requests
import pandas as pd

url = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10&e=Bitfinex"
f = requests.get(url)
ipdata = f.json()
df = pd.DataFrame(ipdata['Data'])
print(df)

