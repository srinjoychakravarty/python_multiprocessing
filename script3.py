import pandas as pd
# For protocol plots below
import numpy as np
import json, urllib.request

url = 'https://www.cryptocompare.com/api/data/coinlist/'
data = urllib.request.urlopen(url).read().decode('utf8')
data = json.loads(data)
data = pd.DataFrame(data['Data']).T

# Protocol token counts per coin
protocols = pd.merge(pd.DataFrame(data.groupby(['BuiltOn']).size().sort_values(ascending=False)), data[['Id', 'Name']], left_on = 'BuiltOn', right_on = 'Id')
protocols.rename(columns={0: 'Counts', 'Name':'ProtocolSymbol'}, inplace=True)

protoFlags = np.linspace(.01, .99, len(protocols))
np.random.shuffle(protoFlags)
protocols['Flags'] = protoFlags
protocols = protocols[['Id', 'Counts', 'ProtocolSymbol', 'Flags']].head(30)

# Merge scoring for plots
protocolPlot = pd.merge(data, protocols, right_on = 'Id', left_on = 'BuiltOn', how = 'outer').sort_values("SortOrder")
print(protocols.head(30))