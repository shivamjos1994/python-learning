# reduce()
import functools
"""l = [1,2,3,8,4,5,6,7]
print("Sum of elements: ",end="")"""
# print(functools.reduce(lambda a,b:a*b,l))   #for multiplication of elements of list
# print(functools.reduce(lambda a,b : a if a > b else b, l))    # to show max element.

# reduce() can also be used with operator
import operator
"""l = [1,2,3,4,5,6,7]
print("Sum of elements: ")"""
# print(functools.reduce(operator.mul, l))
# print(functools.reduce(operator.add, l))


# filter()
"""l = [1,2,3,4,5,6,7,8,9,10]
print(l)"""
"""even = filter(lambda x : x%2 == 0, l)
print("Even numbers: ",list(even))
odd = filter(lambda x : x%2 != 0, l)
print("Odd numbers: ",list(odd))"""

"""def length(n):
    if len(n) <= 7:
        print(n)
l =['hello','there','howareyou','dearfriend','nice','tomeet','you!']
x = filter(length, l)
print(list(x))"""



# map()
"""def square(n):
    return n*n"""
"""l =[1,2,3,4,5,6]
print(l)"""
# x = map(square, l)
# print(list(x))
# OR
"""x = map(lambda x: x*x, l)
print(list(x))"""


