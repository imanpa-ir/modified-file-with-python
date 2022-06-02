import os
import time
import datetime

# file address
fileLocation = r"c:\\test.txt"

year = int(input('year : '))
month = int(input('month : '))
day = int(input('day : '))
hour = int(input('hour : '))
minute = int(input('minute : '))
second = int(input('second : '))

date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
modTime = time.mktime(date.timetuple())

os.utime(fileLocation, (modTime, modTime))
print('DONE!')
