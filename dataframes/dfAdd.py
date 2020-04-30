import datetime as dt
import time
import pause
import pandas as pd
import sys

def createExampleDf(ticker):
    #creating an example df
    contractExps = [20200306,20200306,20200306,20200306,
                    20200313,20200313,20200313, 20200313]
    columns = ["data", "ticker", "contractExp"]
    data = []
    dataset = []

    for x in range(8):
        data = "penis"
        ticker = ticker
        contractExp = contractExps[x]
        data = [data, ticker, contractExp]
        dataset.append(data)


    # print(dataset)
    print("\nNew Dataframe with ticker: " + str(ticker))
    dfDataSet = pd.DataFrame(dataset, columns=columns)
    print(dfDataSet)
    return dfDataSet

def createExampleDf2(ticker):
    #creating an example df
    contractExps = [20200306,20200306,20200306,20200306,
                    20200313,20200313,20200313, 20200313]
    columns = ["data", "ticker", "contractExp", "extraColumn"]
    data = []
    dataset = []

    for x in range(8):
        data = "penis"
        ticker = ticker
        contractExp = contractExps[x]
        extra = 1
        data = [data, ticker, contractExp, extra]
        dataset.append(data)


    # print(dataset)
    print("\nNew Dataframe with ticker: " + str(ticker))
    dfDataSet = pd.DataFrame(dataset, columns=columns)
    print(dfDataSet)
    return dfDataSet

dfDataSet1 = createExampleDf("AAPL")
dfDataSet2 = createExampleDf2("TSLA") #has a new column

#adding dataframes together
frames = [dfDataSet1, dfDataSet2]
dfAllDataSets = pd.concat(frames)

print("\nDataframes added:")
print(dfAllDataSets)
