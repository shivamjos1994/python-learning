import random
import math
# l = [1, 2, 'hello', 3, 4, 'how', 5, 6, 'are', 7, 8, 'you']
# print(random.choice(l)) # using choice function in random module for choosing a random element from a set such as a list

# printing random integer between 0 and 5
# print(random.randint(0, 5))                    # will five integer value

# print random floating point number between 0 and 1
# print(math.floor(random.random()* 100))            # now will give integer value

# random number between 0 and 100
# print(random.random()* 100)            # wil give float value


# another modules are:
# 1.datetime module
import datetime
# print(datetime.datetime.now())         #current time
# print(datetime.datetime.utcnow())      # Return the current UTC date and time, with tzinfo None. like .now()
# print(datetime.time())
# y = datetime.datetime(2020,5,17)      # will print the desired year, month and day
# print(y)
a = datetime.datetime.timestamp()



# 2 time module :
import time
t = time.localtime()
y = time.strftime("%Y-%m-%d  %H:%M:%S")                     # %D = date/month/year   ex: 10/6/23
print(y)
x = time.strptime("13 Nov 23", "%d %b %y")
# time.struct_time(tm_year=2023, tm_mon=11, tm_mday=13, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0,
# tm_yday=317, tm_isdst=-1)      (it'll print this)
print(x)

