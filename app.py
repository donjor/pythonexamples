import datetime

string = "2020-02-11 13:31:52.984700+00:00"
print(string.find("."))
string = string[0:string.find(".")]
print(string)

#string = "2020-02-11 13:31:52"
date = datetime.datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
print(date)

dateLastestHour = date.strftime('%Y-%m-%d %H:%M')
print(dateLastestHour)
