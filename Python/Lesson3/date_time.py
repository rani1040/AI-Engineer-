import datetime
today_time = datetime.datetime.now()
print(today_time)


# you can extract everything from it
year = today_time.year
print("Year : ",year)

month = today_time.month
date = today_time.day

print("date : ",date,"month: ",month)

hour = today_time.hour
print(hour)