import sys

bool_small = "False"
args = sys.argv
tickers = []

if len(args) > 1:
    #print(args)
    tickers = []
    for x in range(len(args)):
        if x > 0:
            if x == 1:
                print(args[x])
                bool_small = args[x]
            else:
                #print(args[x])
                ticker = str(args[x])
                tickers.append(ticker)

if bool_small == "True":
    print("bool_small = True")
else:
    print("bool_small = False")


print(tickers)
