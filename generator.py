"""Return sends a specified value back to its caller whereas Yield can produce a sequence of
values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire
sequence in memory. Yield is used in Python generators."""
"""def f1():
    i = 1
    while True:
        yield i*i
        i += 1
for i in f1():
    if i > 100:
        break
    else:
        print(i)"""

# generator object:
"""Python Generator functions return a generator object that is iterable, i.e., can be used as an 
Iterator. Generator objects are used either by calling the next method of the generator object or using
the generator object in a “for in” loop"""
"""def f1():
    yield 1
    yield 2
    yield 3
x = f1()    # x is a generator object
# Iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))"""


# A simple generator for Fibonacci Numbers  (using next() and for in loop method):
"""def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, (a + b)
# Create a generator object
x = fib(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# Iterating over the generator object using for in loop:
for i in x:
    print(i)"""


# Python Generator Expression:
"""In Python, generator expression is another way of writing the generator function. It uses the Python 
list comprehension technique but instead of storing the elements in a list in memory, it creates 
generator objects."""
"""generator_expression = [i*5 for i in range(5) if i % 2 == 0]
for i in generator_expression:
    print(i)"""

