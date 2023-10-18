"""a=10
b=0
print("Before")         #it'll get executed(after that program get terminated)
c=a/b                   (b=0 that's why)
print(c)
print("After") """
#################################################################################
"""l1 = [10,11,12]
print(l1[4])  #Index error """
##################################################################################

#Exception Handling:
"""a=100
b=0
try:
    c=a/b
#except ZeroDivisionError as e:           #e is an object of the class "ZeroDivisionError" OR
except Exception as e:
    print("Denominator is zero")
    #print(e)                               #It'll print the default message
else:
    print(c)
finally:
    print("Default")
print("Rest of the code")"""

"""we can write class "Exception" in place of "ZeroDivisionError" or any other class if we
do not know the class name. "Exception" class will handle all the exceptions."""
"""if we write the wrong class name in the except block,the exception handling will occur
by the language itself and the rest of the code will not get executed """
"""only one of the blocks will get executed,either except block or else block"""
#try: block where exception generating statement is placed
#except: block where exception handling statement is placed
#else: block where statement is placed if exception does not come
#finally: closing statement is placed,it'll get executed whether there is exception or not

###################################################################################
#Q. wap to raise ZeroDivisonError exception if age entered by user is less than 18
"""a=int(input("Enter your age: "))
try:                                 
    if a>18:                         #we'll write if else condition inside the try block
        print("Eligible for voting")
    else:                            #here we use else to throw the exception
        raise ZeroDivisionError
except ZeroDivisionError as e:         #if the exception occurs then except block gets executed
    print("Age can't be less than 18")"""

####################################################################################

"""def func(a, b):
   try:
     c = ((a+b)/(a-b))
   except Exception as e:
     print("Error:",e)
   else:
     print(c)

func(3,2)
func(3,3)"""


# Multiple Exception Handling in Python:
"""try: 
	client_obj.get_url(url) 
except (URLError, ValueError):      # can give the exception names here
	client_obj.remove_url(url)      # after finding any of the exceptions this remove_url get hit
except SocketTimeout:               # is this exception occured , then it'll work accordingly.
	client_obj.handle_url_timeout(url) 
"""

# Built-in exceptions:
# 1. exception BaseException (base class for all built-in exceeptions)
# 2. exception Exception ( base class for all built-in non-system-exiting exceptions. All user-defined
# exceptions should also be derived from this class.)
# 3. exception ArithmeticError (OverflowError / ZeroDivisionError / FloatingPointError)
# 4. exception LookupError (keyError / IndexError)
# 5. exception AssertionError
# 6. exception AttributeError ( raised when an attribute reference or assignment fails such as when a
# non-existent attribute is referenced.)
# 7. exception MemoryError
# 8. exception NameError (This error is raised when a local or global name is not found.
# For example, an unqualified variable name.)
# 9. exception OverflowError
# 10. exception RuntimeError (The RuntimeError is raised when no other exception applies. It returns a
# string indicating what precisely went wrong.)
# IndexError, ImportError, IOError, ZeroDivisionError, TypeError, and FileNotFoundError
# ......and many more errors

# User-defined errors:
# print(help(Exception))        (can see about the exception here)

"""class Error(Exception):
    pass

class zero(Error):
    pass

try:
    x = int(input("Enter a number: "))
    if x == 0:
        raise zero
except zero:
    print("Input value is zero, try again!")
else:
    print(x)"""

