"""s={"monday","tuesday","monday","saturday"}
print(s)      #set ignores the duplicate values and print the values in a random order
print(type(s))
s1={}   #this  is dictionary
print(type(s1))   """


#Set Operators:
"""s1={11,12,13,14,15,16}
          for i in s1:     we can use to print set elements using loop
             print(i)"""
#s2={17,18,19,12,13,20}
#s3=s1|s2              union operator = '|'
#s3=s1.union(s2)       union function
#s3=s1&s2              intersection operator = '&'
#s3=s1.intersection(s2)     intersection function
#s3=s1-s2        difference operator='-', (s1-s2=only value present in s1)
#s3=s2-s1         (s2-s1=only value present in s2)
#s3=s1.difference(s2)    difference function(s1-s2=only value present in s1)
#s3=s2.difference(s1)    (s2-s1=only value present in s2)
#print(s3)
##############################################################################################

# Type Casting with Python Set method:
"""x = set(["a", "b", 'c', 3, 3, 4, 5, 6, "a"])
print(x)
x.add("r")
print(x)"""

# Frozen Sets:
"""Frozen sets in Python are immutable objects that only support methods and operators that produce a 
result without affecting the frozen set or sets to which they are applied. It can be done with 
frozenset() method in Python."""
"""x = frozenset([1, 2, 'e', 4, 5, 'f'])  # can't perform add operator to it
print(x)"""

# Methods for set:
# 1. add():
"""x = {1, 2, 3, 4, 5}
x.add(20)
for i in range(10,18):
    x.add(i)
print(x)"""

# 2. clear():
"""x = {2, 3, 4, 5, 6}
x.clear()
print(x)"""


# Append Multiple Elements in Set in Python:
# 1. update():
"""x = {1, 2, 3, 4, 5, 6, 7, 8}
y = [10, 20, 30, 40]
x.update(y)     # argument in the update() must be an iterable
print(x)"""

# 2. Using | Operator (Pipe Operator):
"""x = {1, 2, 3, 4, 5}
print(x)
y = ['a', 'b', 'c', 'd']
x |= set(y)
print(x)"""

# 3. Using List Comprehension:
"""Here, we will use the Python list comprehension method to append only those elements in a set that 
are not already present in it. Then we use the set() constructor to convert the list to a Python set."""
"""x = {1, 2, 3, 4, 5}
y = list(x)
z = [2, 5, 6, 7]
y += [i for i in z if i not in x]
print(set(y))"""

# 4. Using reduce() Method:
"""from functools import reduce
x = {1, 2, 3, 4, 5}
y = [6, 7, 6, 2, 8, 9, 10]
res = reduce(lambda a, b: a.union(set([b])), y, x)
print(res)"""




# Removing elements of the set one by one:
# 1. pop():
"""x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
while x:
    x.pop()
    print(x)"""

# 2. discard():
"""x = {1, 2, 3, 4, 5, 6}
while x:
    x.discard(max(x))       # discard takes exactly one argument.
    print(x)"""


# 3. remove():
"""Use the remove method on the first element of the set which is retrieved by the next() method on 
iter() function. """
"""x = {1, 2, 3, 4, 5, 6, 7, 8}
for i in range(len(x)):
    x.remove(next(iter(x)))
    print(x)"""




# How to check if a set contains an element in Python?
# 1. Using in operator:
# s = {1, 2, 3, 4, 5}
"""print(2 in s)           # true          
print(4 in s)              # true
print(7 in s)"""          # false

# 2. Using not in operator:
"""print(1 not in s)         # false
print(7 not in s)  """       # true

# 3. Using Counter() Function:
"""from collections import Counter
c = Counter(s)
print(1 in c.keys())            # true
print(3 in c.keys())            # true
print(8 in c.keys()) """           # false

# 4. Using operator.countOf() method:
"""from operator import countOf
print(countOf(s, 1) > 0)          # true
print(countOf(s, 9) > 0)"""       # false