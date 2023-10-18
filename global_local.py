# Inside a function
"""a = 20
def func():
    global a          # will change into global variable
    a += 10
    print(a)           # 30
func()
print(a)               # 30    """


# For the list elements.
"""l = [1,2,3]
def lis():
    global l
    l =[10,20,30]
    
print(l)           # [1,2,3]
lis()
print(l)           # [10,20,30]  """


# Nested function (global variable will be declared inside the nested function)
"""def add():
    a = 15
    def change():
        global a
        a = 20
    print("Outside nested function x is ",a)
    change()
    print("After calling nested function x is ",a)
add()
print("Outside the function x is ",a)"""


#################################################################################################

# global and local scope:
"""def func():
    print("inside ",s)
s = 20                                   # will print 20 in both cases as it's a global variable
func()
print("outside",s)"""

"""def func():
    s = 34
    print(s)
s = 90
func()
print(s)"""

"""def func():
    global s
    s += '1'
    print("inside", s)
    s = "hey there"
    print(s)
s = "hi"
func()
print(s)"""


"""a = 1
# Uses global because there is no local 'a'
def f1():
    print("inside f1", a)
# Variable 'a' is redefined as a local
def f2():
    a = 20
    print("inside f2", a)
# Uses global keyword to modify global 'a'
def f3():
    global a
    a = 30
    print("inside f3", a)

print("global: ",a)
f1()
print("global: ",a)
f2()
print("global: ",a)
f3()
print("global: ",a)"""


"""a = 10
def add():
    b = a + 5         # gives error, bcz a is not assigned here.
    a = b
    print(a)
add()
print(a)"""


# Modifying global Mutable Objects:
# 1. Modifying global Mutable Objects:
"""l = [1, 2, 3]
def change():
    for i in range(len(l)):
        l[i] += 10
    print(l)          # [1, 2, 3]
print(l)    # [11, 12, 13]
change()
print(l)    # [11, 12, 13]"""

# 2.  Modifying list variable using global keyword.
"""arr = {10, 20, 30}
def fun():
	global arr
	arr = {20, 30, 40}
print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)"""


