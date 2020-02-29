import datetime as dt
import time
import pause
import pandas as pd
import sys

args = sys.argv
#print(args)

if len(args) > 1:
    print(args[1])

time = dt.time(10,30)
print(time)

tickers = ['AAPL','SPY','TSLA','AMD','BYN','AMZN','GOOG','ZM','V','SPOT','FB','MSFT','SPCE','RIG','FLS','GDI', 'WMT', 'MDT', 'TRU', 'ALLE', 'ALLE', 'HLF', 'GRMN', 'IMAX', 'APRN', 'ZG', 'FIVN', 'DPZ', 'WIX', 'DBX', 'FSLY', 'FIT']


for i in range(0,len(tickers),5):
    for j in range(5):
        if (i+j) < len(tickers):
            print(str(i+j))
            print(str(tickers[i+j]))

#
# string = "2020-02-11 13:31:52.984700+00:00"
# print(string.find("."))
# string = string[0:string.find(".")]
# print(string)
#
# #string = "2020-02-11 13:31:52"
# date = datetime.datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
# print(date)
#
# dateLastestHour = date.strftime('%Y-%m-%d %H:%M')
# print(dateLastestHour)
# printDate = dt.datetime.now().strftime('%Y%m%d %H.%M.%S')

# pause.seconds(5)
# endTradingTime = dt.datetime(2020, 2, 15, 10, 30)
#
# while dt.datetime.now() < endTradingTime:
#     if dt.datetime.now() > dt.datetime(2020, 2, 15, 3, 30):
#         print(dt.datetime.now())
#         exec(open("getOptionPrice.py").read())
#         pause.seconds(5)
#         exec(open("getOptionChains.py").read())
#         pause.seconds(5)
#         exec(open("calcExpectedReturns.py").read())
#         pause.minutes(15)
#     else:
#         print("outside of trading hours")
#         pause.seconds(5)
#

# print(date)
# list = ["error"]
#
#     df = pd.DataFrame(["error"], columns = ["symbol"])
# print(df)
