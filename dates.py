import datetime as dt
import pytz

dateString = "2020-03-06 11:10:04"
date = dt.datetime.strptime(dateString,'%Y-%m-%d %H:%M:%S')
print(date)

dateOutput = date.strftime('%Y-%m-%d %H.%M.%S')
print(dateOutput)


now = dt.datetime.now()
print(now)
dateString = now.strftime('%Y%m%d')
print(dateString)


logDateString = "2020-04-25 01:53:28.024816"

date = dt.datetime.strptime(logDateString,'%Y-%m-%d %H:%M:%S.%f')
date = date + dt.timedelta(minutes=10)
print(date)

datetimenow = dt.datetime.now()
datenow = dt.datetime.now().date()
closeTime = dt.time(7,00)
closeDateTime = dt.datetime.combine(datenow, closeTime)

nyc_datetime = dt.datetime.now(pytz.timezone('US/Eastern'))
nyc_datetime = nyc_datetime.replace(tzinfo=None)
nyc_date = nyc_datetime.strftime('%Y%m%d')

contractExp = "20200424"


#contractExpDate = dt.datetime.strptime(contractExp,'%Y%m%d')

if (datetimenow > closeDateTime):
    print("\nComparing contractExp date to nyc datetime")
    if contractExp == nyc_date:
        print("dates are equal")
    else:
        print("dates aren't equal")
else:
    print("wrong time to close position")



print(contractExp)
print(nyc_date)
