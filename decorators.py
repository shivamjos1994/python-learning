"""def main(func):
    def wrapper():
        print("before execution")
        func()
        print("after execution")
    return wrapper

def func1():
    print("hi how are you")

yes = main(func1)
yes()"""


# find out the time taken by a function:
"""import time
import math
def calculateTime(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("total time taken: ", end-begin)
    return inner

@calculateTime
def fact(n):
    time.sleep(2)
    print(math.factorial(n))

fact(10)"""


# What if a function returns something or an argument is passed to the function?
"""def sum_decorator(func):
    def inner(*args, **kwargs):
        print("before execution")
        x = func(*args, **kwargs)
        print("after execution")
        return x
    return inner

@sum_decorator
def sum(a, b):
    print("inside the function")
    return a + b
a, b = 10, 20
print("Sum of numbers: ", sum(a, b)) """

# Chaining decorators:
"""def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1                  # placement of decorators also matters  (2nd check)
@decor2                   # 1st check
def num():
    return 10

@decor2                    # placement of decorators also matters  (2nd check)
@decor1                  # 1st check
def num1():
    return 10

print(num())
print(num1())"""

"""		
def decor1(func):
		def wrap():
			print("************")
			func()
			print("************")
		return wrap
		
def decor2(func):
		def wrap():
			print("@@@@@@@@@@@@")
			func()
			print("@@@@@@@@@@@@")
		return wrap
	
@decor1
@decor2
def sayhellogfg():
		print("Hello")
		
def saygfg():
		print("GeekforGeeks")
		
sayhellogfg()
saygfg()
"""


# Conditional decorators:
"""x = int(input("Enter a numbers (1/2): "))
def decor1(func):
    def wrapper():
        oldString = func()
        newString = oldString.upper()
        return newString
    return wrapper

def decor2(func):
    def wrapper():
        oldString = func()
        newString = oldString.lower()
        return newString
    return wrapper

if x == 1:
    @decor1
    def func():
        return "Hello"
elif x == 2:
    @decor2
    def func():
        return "Hello"
else:
    def func():
        return "Hello"

print(func())"""



