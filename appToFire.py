import sys

print("app fired")
args = sys.argv

if len(args) > 1:
    print("passed ticker:")
    print(args[1])
    tickers = [str(args[1])]
