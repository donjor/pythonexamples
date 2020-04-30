import datetime as dt
import time
import pause
import pandas as pd
import sys

stockValues = []

symbol = "APPL"
price = 286
stockValues.append([symbol, price])

symbol = "TSLA"
price = 714
stockValues.append([symbol, price])

stockValuesColumns = ["symbol", "price"]
dfStockValues = pd.DataFrame(stockValues, columns=stockValuesColumns)

print(dfStockValues)

appl_price = float(dfStockValues['price'][dfStockValues['symbol'] == "APPL"])
print(appl_price)
