import datetime as dt
import time
import pause
import pandas as pd
import sys
import os


tickers = ['AAPL','SPY','TSLA','AMD','BYND','AMZN','GOOG','ZM','V','SPOT','FB','MSFT','SPCE','RIG','FLS','GDI', 'WMT', 'MDT', 'TRU', 'ALLE', 'ALLE', 'HLF', 'GRMN', 'IMAX', 'APRN', 'ZG', 'FIVN', 'DPZ', 'WIX', 'DBX', 'FSLY', 'FIT']

for ticker in tickers:
    file_name = "app.py " +  str(ticker)
    os.system(file_name)
