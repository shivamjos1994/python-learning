# sep operator (separator operator used to modify the soft space between arguments)
# print(2,3,4,sep='@')
# print("Hello", "there",sep='')
# print("Hello","there",sep='-')
# print(3,10,2023,sep='-')


# Taking multiple inputs from user in Python (split() is used)
"""x, y = input("Enter two values: ").split()
print(x)
print(y)"""

"""a, b = input("Enter two numbers: ").split()
print("The value of a is {} and b is {}".format(a,b))"""

"""x = list(map(int, input("Enter multiple values: ").split()))
print("multiple values of x: ",x)"""


# taking multiple input using list comprehension
"""x, y = [int(x) for x in input("Enter two values: ").split()]
print("x:", x)
print("y:", y)"""

"""x, y = [int(x) for x in input("Enter two values: ").split()]
print("The value of a is {} and b is {}".format(x, y))"""

"""x = [int(x) for x in input("Enter multiple values: ").split()]
print(x)"""


# taking multiple inputs at a time separated by comma
"""x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)"""


# flush() [code prints in buffering, means in chunks. To run the code smoothly we use flush()]
# without flush():
"""import time
countDown = 3
for i in reversed(range(countDown+1)):
    if i > 0:
        print(i, end=">>>")
        time.sleep(1)
    else:
        print("Start")"""

# without flush():
"""import time
countDown = 3
for i in reversed(range(countDown+1)):
    if i > 0:
        print(i, end=">>>", flush=True)
        time.sleep(1)
    else:
        print("Start")"""


# File argument
"""import io
dummyFile = io.StringIO()
print("Hey There!!", file=dummyFile)
print(dummyFile.getvalue())"""

# Writing to a File with Python’s print() Function
# This code is writing the data in the print() function to the text file.
# print('Welcome to Python world.!!', file=open('Testfile.txt', 'w'))  [it'll create a file and add the text into it.]

# Formatting Output using The String Method
str = "Hey there how are you??"
# print(str.center(40, '#'))         # counts the total number of characters including '#'
# print(str.ljust(40, '-'))
# print(str.rjust(40, '-'))

