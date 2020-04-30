import datetime as dt

currentDateTime = dt.datetime.now()
print(currentDateTime)

# subtract time
print("\n Subtract Time")
print("currentDateTime: " + str(currentDateTime))
newDateTime = currentDateTime - dt.timedelta(minutes=2)
print("newDateTime: " + str(newDateTime))

#convert from string to usable formot
print("\n Convert from string to usable formot")
dateString = "2020-02-27 13:23:24.834536+00:00"
print("dateString: " + dateString)
dateString = dateString[0:dateString.find(".")] #remove from millisconds

dateStringConverted = dt.datetime.strptime(dateString,'%Y-%m-%d %H:%M:%S')
print("dateStringConverted: " + str(dateStringConverted))
