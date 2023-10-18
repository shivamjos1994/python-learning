"""t1=(10,12,13,14,19,89)
t2=(34,)      #we've to give a comma after one element otherwise it'll not consider a tuple
t3=(23,"hey")
print(type(t1))
print(type(t2))
print(type(t3))
print(t1)       """


#conversion of list into tuple and vice versa
"""l=[10,11,12]
t=tuple(l)   #tuple() is used to convert list into tuple
k=list(t)    #list() is used to convert tuple into list
print(type(l))    # list
print(type(t))    #tuple
print(type(k))    """ #list

#t=(1,2,3,4)
#t[2]=20       tuple doesn't allowed element insertion
#del t[3]     'tuple' object doesn't support item deletion
#del t         we can delete the whole tuple(but can not delete all the elements)

###################################################################################################

""" Methods that cannot be used for tuples:
append(), insert(), remove(), pop(), clear(), sort(), reverse()"""

"""Functions that can be used for both lists and tuples:
len(), max(), min(), sum(), any(), all(), sorted()"""

"""Methods that can be used for both lists and tuples:
count(), Index()"""



# Create a tuple from string and list Using extend method
"""list = [2, 3, 4, 6]
string = "hey there"
list.extend([string])
print(tuple(list))"""


# Access front and rear element of Python tuple:
# 1. Using Access Brackets:
# l = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# print(l[0], l[-1])

# 2. Using itemgetter():
"""from operator import itemgetter
x = itemgetter(0, -1)(l)
print(x)"""

# 3. Using indexing:
# print(l[0], l[len(l)-1])

# 4. Using Unpacking tuple:
"""This method requires the *_ syntax, which is called “unpacking” in Python and allows you to 
assign a specific portion of a tuple to a variable. In this case, the *_ syntax is used to 
ignore the intermediate elements in the tuple."""
"""front, *_, rear = l          # Accessing front and rear element of tuple Unpacking the tuple
res = (front, rear)      # Storing the front and rear elements
print(res)"""

# 5. Using List Comprehension:
"""x = tuple(([l[i] for i in [0, -1]]))        # will print list, convert it into tuple.
print(x)"""



# Ways to concatenate tuples:
# 1. Using + operator:
"""t1 = (1, 2, 3)
t2 = (4, 5, 6)"""
# print(t1 + t2)

# 2. Using sum() :
"""res = sum((t1, t2),())
print(res)"""

# 3. Using list() and extend() methods:
"""l = []
l.extend(t1)
l.extend(t2)
print(tuple(l))"""

# 4.  Using itertools.chain() function:
"""from itertools import chain
t3 = chain(t1, t2)           # t3 is an object, convert it into tuple
print(tuple(t3))"""

# 5. Using the += operator and the += method:
"""t1 += t2            # modifies the first tuple
print(t1)"""

# 6. Using reduce:
"""from functools import reduce
x = reduce(lambda a, b: a+b, [t1, t2])
print(x)"""



#  Clearing a tuple:
# 1. Using list() + clear() + tuple() :
# t = (1, 2, 3, 4)
"""x = list(t)
x.clear()
t = tuple(x)
print(t)"""

# 2. Reinitialization using tuple()
"""t = ()
print(t)"""

# 3. Using * operator
"""t = t * 0
print(t)"""

# 4. Using slicing and concatenation:
"""t = t[0:0] + ()
print(t)"""


