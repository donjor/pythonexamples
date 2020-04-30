import datetime as dt
import time
import pause
import pandas as pd
import sys

contractExps = [20200306,20200306,20200306,20200306,
                20200313,20200313,20200313, 20200313]
columns = ["data", "ticker", "contractExp"]
data = []

dataset = []

for x in range(8):
    data = "penis"
    ticker = "AAPL"
    contractExp = contractExps[x]
    data = [data, ticker, contractExp]
    dataset.append(data)


print(dataset)

dfDataSet = pd.DataFrame(dataset, columns=columns)
print(dfDataSet)

dfDataSetUnique = dfDataSet.drop_duplicates('contractExp')
print(dfDataSetUnique)
