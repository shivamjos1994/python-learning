# mutidimensional list (nested list)
"""l = [[1, 23, 3], [4, 5, 6, 7]]
print(l)
print(l[0][1])   # 23
print(l[1][3])   # 7"""
import functools

# adding multiple values in a list using list comprehension
"""x = [int(x) for x in input("enter the numbers :").split()]
print(x)"""

# adding multiple values in a list using map()
"""x = list(map(int, input("Enter: ").split()))
print(x)"""

# reverse() and reversed():
"""l = [1, 2, 3, 4]
l.reverse()
print(l)"""

"""l = [1, 2, 3, 4]
# l1 = reversed(l)     # l1 is an iterator object, it must be converted into list.
l1 = list(reversed(l))
print(l1)"""

# remove() [used to remove only first occurrence of an element ]
"""l = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 5, 4]
for i in l:
    l.remove(i)
print(l)"""

# enumerate:
# l = [1, "eat", 2, "sleep", 3, "rave", 4, "repeat"]
# print(enumerate(l))   # will return an iterator object
# print(list((enumerate(l))))   # [(0, 1), (1, 'eat'), (2, 2), (3, 'sleep'), (4, 3), (5, 'rave'), (6, 4), (7, 'repeat')]


# Using Enumerate Object in Loops
# l = ['hey', 'there', 'how', 'are', 'you']
"""for i in enumerate(l):       # printing the tuples in object directly
    print(i)"""

"""for c, i in enumerate(l, 100):     # changing index and printing separately
     print(c, i)"""

"""for c, i in enumerate(l):         # getting desired output from tuple
    print(c)
    print(i)"""


# Accessing the next element:
"""To access the next element in an enumerate object, you can use the next() function. It takes
 the enumerate object as input and returns the next value in the iteration."""
"""fruits = ['apple', 'banana', 'strawberry', 'blueberry']
x = enumerate(fruits)
print(next(x))
print(next(x))
print(next(x))"""

# filter():
"""l = ['e', 'a', 'r', 'u', 't', 'i', 'k', 'o']
def even(x):
    if x in "AEIOUaeiou":
        return x

l1 = list(filter(even, l))
print(l1)"""

# map():
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""def func(a):
    if a % 2 == 0:
        return a ** 2
    else:
        return a

l1 = list(map(lambda x : func(x), l))
print(l1)
"""

# Python Lambda Function with List Comprehension
# item() is used to get the desired value in the list by calling the object function inside the loop
"""l = [1, 2, 3, 4, 5, 6, 7]
even = [lambda arg=x: arg*2 for x in l]   # stores the list the lambda function objects.
for item in even:
    print(item(),end=' ')"""

# Python Lambda Function with if-else
"""Max = lambda a, b: a if a > b else b
print(Max(9, 3))"""


# Python Lambda with Multiple Statements
"""List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)"""


# Using lambda() Function with filter()
"""l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = list(filter(lambda x : x % 2 == 0, l))
print(l1)"""


# Using lambda() Function with map()
"""animals = ['dog', 'cat', 'parrot', 'rabbit']
list = list(map(lambda x: x.upper(), animals))
print(list)"""


# Using lambda() Function with reduce()
"""from functools import reduce
list = [10, 20, 30, 90, 40, 50, 60]
l1 = functools.reduce(lambda a,b: a if a > b else b, list)
print(l1)"""


# Find the Length of a List in Python using length_hint()
"""from operator import length_hint
l = [1, 2, 3, 4, 5, 6]
# print(len(l))
print(length_hint(l))"""

# Find the Length of a List in Python using sum()
"""l = [2, 3, 4, 6, 7, 9, 10]
x = sum(1 for i in l)     # add 1 until the very end of the list, in order to give the length
print(x)"""

# Find the Length of a List in Python using a List Comprehension
"""list = [2, 3, 5, 6, 8, 1, 10, 13, 14, 15, 17, 20]
length = sum(1 for _ in list)
print(length)"""

# The Length of a List in Python using enumerate function
"""list = [2, 3, 4, 5, 6, 77, 45, 52]
c = 0
for i, a in enumerate(list):
    c += 1
print(c)"""

"""Functions that can be used for both lists and tuples:
len(), max(), min(), sum(), any(), all(), sorted()"""

"""Methods that can be used for both lists and tuples:
count(), Index()"""

