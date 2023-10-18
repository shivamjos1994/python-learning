"""def msg():   #function without parameters
    print("Function Called")
    print("Hey")

print("Before")
msg()   #function called
print("After")
msg()  """

"""def add(a,b):   #formal parameter
    res=a+b                         #This is the function definition block
   # print(res)
    return res      #returning the value to the main function
c=int(input("Enter first number: "))
d=int(input("Enter second number: "))              #This is the main function block
#add(c,d)  #actual parameter
s=add(c,d)          # we need to store the calling function result in some variable in order to print
print("Addition: ",s)          """


#Q.write a function to calculate area of rectangle:
"""def ar(a,b):
    res=a*b
    return res
a=int(input("Enter length: "))
b=int(input("Enter breadth: "))
s=ar(a,b)
print("Area of rectangle: ",s)    """

#Q.write a function to calculate cube of entered number
"""def cube(a):
    res=a*a*a
    return res
a=int(input("Enter any number: "))
s=cube(a)
print("Cube: ",s)   """

#Q.Write a function to find the factorial of entered number
"""def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("Enter any number: "))
f=fact(n)
print("Factorial: ",f)   """

#Q.Write a function to calculate the entered number is divisible by 5 or not?
"""def div(n):
    if n%5==0:
        print("number is divisible by 5")
    else:
        print("number is not divisibble by 5")
n=int(input("Enter any number: "))
div(n)   """

#Q.Write a Python function that accepts a string and calculate the number
# of upper case letters and lower case letters.
"""def show(a):
    u=0
    l=0
    for i in a:
        if i.islower():
            l=l+1
        elif i.isupper():
            u=u+1
    print("Number of lowercase letters: ",l)
    print("Number of uppercase letters: ",u)
a=input("Enter a string: ")
show(a)               """

#Q.wap to find even numbers in a list using function:
"""l=[11,12,13,14,15,16,17,18]
print(l)
def even(l):
    for i in l:
        if i%2==0:
            print(i,end=" ")
even(l)      """
###############################################################################################

# Types of Python Function Arguments:
# 1. Default Arguments:
"""def add(a, b=12):
    return a + b
print("addition of two numbers is",add(8))
print("addition of two numbers is",add(8, 6))"""

# 2. Keyword Arguments:
"""def info(name, age):
    print(name, age)
info(name="Rohan", age=45)"""

# 3. Positional Arguments:
"""def nameAge(name, age):
    print("hi my name is", name)
    print("hi my age is", age)
nameAge("Rohit", 53) """

# 4. Arbitrary Keyword  Arguments: (*args & **kwargs)
#  Variable length non-keywords argument:
"""def hey(*args):
    for i in args:
        print(i)
hey('hey', 'there', 'how', 'are', 'you', 3)"""
# Variable length keyword arguments:        kwargs shows dictionary operators
"""def func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
func(a='ewe', b=23, c='io', e='ioi')    """     # can print key value pair

# nested function:
"""def f1():
    x = "hey"
    def f2():
        print(x)
    f2()
f1()"""

# Pass by value and Pass by reference:
"""In Python every variable name is a reference. When we pass a variable to a function, a new reference
to the object is created. """
"""When we pass a reference and change the received reference to something else, the connection between
the passed and received parameter is broken."""
"""def f1(x):
    x[0] = 10
l = [1, 2, 3, 4]          # l is modified
f1(l)
print(l)"""

"""def f1(x):
    x = 30
x = 29            # this x is in global scope, will print.
f1(x)             # x is in local scope
print(x)"""

"""def swap(x, y):
    temp = x
    x = y
    y = temp
x = 20
y = 34
swap(x, y)          # the values will not swap.
print(x)
print(y)"""




# *args & **Kwargs:
"""def f1(arg1, *args):
    print("first argument: ", arg1)
    for i in args:
         print("Number of arguments: ", i)
f1('hey', 'how', 'are', 'you', '?')"""

"""def f1(**kwargs):
    for key, value in kwargs.items():
        print("%s  == %s" % (key, value))
f1(a='ewe', b=23, c='io', e='ioi',)"""


# Using both *args and **kwargs in Python to call a function:
# 1
"""def f1(a, b, c):
    print("first argument: ", a)
    print("second argument: ", b)
    print("third argument: ", c)
args = ('hey', 'there', 'hi')
f1(*args)
kwargs = {"a": "Geeks", "b": "for", "c": "Geeks"}    # keys should match the arguments passed to the function.
f1(**kwargs)"""

# 2
"""def f1(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
f1('hi', 'how', 'are', 'you', a=23, de=32, ad='33')"""


# Using *args and **kwargs in Python to set values of object:
"""*args receives arguments as a tuple.
**kwargs receives arguments as a dictionary."""
# 1. args:
"""class Car:
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]
bmw = Car(290,'black')
audi = Car(280, 'red')
print(bmw.color)
print(audi.speed)"""

# 2. kwargs:
"""class Car:
    def __init__(self, **kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']
bmw = Car(s=290, c='red')
audi = Car(s=240, c='white')
print(bmw.color)
print(audi.speed)"""


# First Class Functions:
# 1. Functions are objects:
"""we are assigning function to a variable. This assignment doesn’t call the function. It takes the 
function object referenced by shout and creates a second name pointing to it, yell."""
"""def shout(text):
     return text.upper()
print(shout("hello"))
k = shout
print(k("hello"))"""

# 2. Functions can be passed as arguments to other functions:
"""Because functions are objects we can pass them as arguments to other functions. Functions that can
accept other functions as arguments are also called higher-order functions"""
"""def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):                      # passing function as an argument
     # storing the function in a variable
     greeting = func("Hi How Are you, Hope You Are Doing Good")
     print(greeting)

greet(shout)
greet(whisper)"""

# 3. Functions can return another function:
"""def f1(x):
    def f2(y):
        return x + y
    return f2
yes = f1(10)
print(yes(25))"""


# non-local variables:
"""non-local variables are used within nested functions to access and modify variables from their 
enclosing (parent) function's scope, but not in the global scope. """
"""def outer():
    x = 10
    def inner():
       nonlocal x
       x += 5
       print(x)
    inner()
outer()"""


# Python closures:
# Python program to illustrate closures:
"""def outer(text):
    def inner():
        print(text)
    return inner        # the inner func reference now refer to the outer func.
closure = outer("hi")   # closure is the object created and now it'll point out the location of the inner function 
closure()"""         # That's why if we call the closure() it'll go inside the inner func().
