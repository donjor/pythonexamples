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

# dfDataSet20200306 = pd.DataFrame(columns=columns)
dfDataSet20200306 = pd.DataFrame(columns=list(dfDataSet.columns)) #use columns from existing df

for x in range(len(dfDataSet)):
    contractExp = dfDataSet['contractExp'].iloc[x]
    if contractExp == 20200306:
        dfDataSet20200306.loc[len(dfDataSet20200306)] = dfDataSet.iloc[x]
        # dfDataSet20200306.append(dfDataSet.tolist())

print(dfDataSet20200306)

# for x in range(len(dfDataSet20200306)):
#     print(dfDataSet20200306.iloc[x])
