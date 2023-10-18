import time
import os
import pytz
import datetime
fmt = "%Y-%m-%d %H:%M:%S %Z %z"


# t = time.gmtime()
# print(time.asctime(t))
# print(time.ctime())
# time.sleep(secs)
# t = time.strptime("2023-10-10 9:48:25", "%Y-%m-%d %H:%M:%S")
# print(time.mktime(t))
# print(time.localtime())
# now = time.localtime()
# print(time.strftime("%Y-%m-%d  %H:%M:%S",now))

"""l = [1,2,3,4,5,6,7,8,8,12,22,33,44,]
start = time.monotonic()
print(start)
for i in l:
  print(i)
end = time.monotonic()
print(end)
print("time lapse: ",end-start)"""

"""format code	meaning	                                         example
%a	Abbreviated weekday name	                                 Sun, Mon
%A	Full weekday name 	                                         Sunday, Monday
%w	Weekday as decimal number	                                 0…6
%d	Day of the month as a zero-padded decimal	                 01, 02
%b 	Abbreviated month name	                                     Jan, Feb
%m	month as a zero padded decimal number	                     01, 02
%B 	Full month name	                                             January, February
%y	year without century as a zero padded decimal number	     99, 00 
%Y	year with century as a decimal number	                     2000, 1999
%H	hour(24 hour clock) as a zero padded decimal number	         01, 23
%I	hour(12 hour clock) as a zero padded decimal number	         01, 12
%p	locale’s AM or PM	                                         AM, PM
%M	Minute as a zero padded decimal number	                     01, 59
%S	Second as a zero padded decimal number	                     01, 59
%f	microsecond as a decimal number, zero padded on the left side	000000, 999999
%z	UTC offset in the form +HHMM or -HHMM	 
%Z	Time zone name	 
%j	day of the year as a zero padded decimal number	              001, 365
%U	Week number of the year (Sunday being the first)	          0, 6
%W	Week number of the year	                                      00, 53
%c	locale’s appropriate date and time representation	          Mon Sep 30 07:06:05 2013
%x	locale’s appropriate date representation	                  11/30/98
%X	locale’s appropriate time representation	                  10:03:43
%%	A literal ‘%’ character	                                      %  """


# time.tzset() Function in python    (helps in conversion of time to any timezone)
"""
# Define TZ environment variable
os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'

# reset the time conversion rules
time.tzset()

# print time
print(time.strftime('%X %x %Z'))

# Define TZ environment variable again
os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'

# reset the time conversion rules
time.tzset()

# print time
print(time.strftime('%X %x %Z'))"""


"""# time.tzset() Function in python
# Define TZ environment variable
os.environ['TZ'] = 'Australia/Melbourne'

# reset the time conversion rules
time.tzset()

# print time
print(time.strftime('%X %x %Z'))


# Define TZ environment variable again
os.environ['TZ'] = 'Egypt'

# reset the time conversion rules
time.tzset()

# print time
print(time.strftime('%X %x %Z'))
"""
# import time module
import time


# get_zone function to get the
# current time between current time zone and UTC
# by using timezone and altzone method
"""def get_zone():
    dst = time.daylight and time.localtime().tm_isdst

    # get altzone if there exists dst otherwise
    # get timezone
    offset = time.altzone if dst else time.timezone

    # check if offset greater than 0
    westerly = offset > 0

    # get the minutes and seconds
    minutes, seconds = divmod(abs(offset), 60)
    hours, minutes = divmod(minutes, 60)

    # return the timezone
    return '{}{:02d}{:02d}'.format('-' if westerly else '+', hours, minutes)


# call the function
print(get_zone())"""


# to get the current time :
"""current_time = time.localtime()
current_clock = time.strftime("%H:%M:%S", current_time)
print(current_clock)"""

"""UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')
print("UTC in default format: ",datetime.now(UTC))
print("IST in default format: ",datetime.now(IST))
datetime_utc = datetime.now(UTC)
datetime_ist = datetime.now(IST)
print("Date & Time in UTC: ", datetime_utc.strftime("%Y-%m-%d %H:%M:%S %Z %z"))
print("Date & Time in IST: ", datetime_ist.strftime("%Y-%m-%d %H:%M:%S %Z %z"))"""


# timestamp:
# time.time()
# datetime.datetime.now().timestamp()


# get datetime from timestamp:
# print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))  # local machine time
# print(datetime.datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))  # utc time



# conversion of various timezones according to the UTC:
"""utc = datetime.datetime.now(pytz.timezone('UTC'))
# print(utc)
# print(utc.strftime(fmt))
timezones = ['Asia/Kolkata', 'Europe/Istanbul','Europe/Helsinki','Europe/Moscow','Indian/Maldives',
             'Pacific/Fiji', 'Europe/Athens', 'America/Chicago', 'America/Denver']

for tz in timezones:
   x = utc.astimezone(pytz.timezone(tz))
   print(tz)
   print(x.strftime(fmt))
   print()
   time.sleep(1.50)"""



# convert one timezone into another timezone:
"""datetime_string = "2023-10-11 13:28:20"             # string from db
datetime_India = dt.datetime.strptime(datetime_string,"%Y-%m-%d %H:%M:%S")       # converts string into object

current_Timezone = pytz.timezone("Asia/Kolkata")                    
target_Timezone = pytz.timezone("Europe/Vienna")

localised_timezone = current_Timezone.localize(datetime_India)
print(localised_timezone)

datetime_vienna = localised_timezone.astimezone(target_Timezone)

print(datetime_vienna)"""



"""naive = datetime.datetime(2023, 10, 11, 15, 32)   # naive: that doesn't have any timezone set
UTC = pytz.timezone('UTC')
ASIA = pytz.timezone('Asia/Kolkata')
print(naive)
print(UTC)
aware = UTC.localize(naive)                         # aware: that know it's timezone (we localize naive to the UTC,now it'll be showing timezone of UTC)

time_in_India = aware.astimezone(ASIA)
print(time_in_India)"""



# without pytz:
"""# naive
naive = datetime.datetime.now()
print(naive)

# UTC aware
UTC = datetime.datetime.now(datetime.timezone.utc)
print(UTC)

# Creating a datetime with timezone of JST (Japan):
jst_datetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9),'JST'))
print(jst_datetime)"""

# with pytz:
"""naive = datetime.datetime.now()
UTC  = pytz.timezone('UTC')
Japan = pytz.timezone('Japan')
aware = UTC.localize(naive)
japan_datetime = aware.astimezone(Japan)
print(japan_datetime)   


# tzinfo : tzname/ utcoffset/ dst

# will print the timezone name:
print(japan_datetime.tzname())  # JST

# get utcoffset: 
print(japan_datetime.utcoffset())    # 9:00:00

# Get the daylight saving time (DST offset) adjustment
print(japan_datetime.dst())        # 0:00:00   """




"""# Indian Standard Time
India = pytz.timezone('Asia/Kolkata')
India_datetime = India.localize(datetime.datetime.now())
print("Indian Standard time: ",India_datetime.strftime(fmt))

#Europe/Amsterdam time:
Amsterdam = pytz.timezone('Europe/Amsterdam')
dt = datetime.datetime(1983, 8, 3, 2, 0, 0)
Amsterdam_datetime = Amsterdam.localize(dt, is_dst=True)
print("Amsterdam with daylight saving time: ",Amsterdam_datetime.strftime(fmt))

# Daylight saving:
print("Daylight saving time in Amsterdam on 3/8/1983: ",Amsterdam_datetime.tzinfo.dst(Amsterdam_datetime))"""


# date.fromtimestamp(datetimestamp)
# print(datetime.date.fromtimestamp(time.time()))

# datetime from timestamp:
# print(datetime.datetime.fromtimestamp(time.time()))

