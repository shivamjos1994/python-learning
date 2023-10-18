#d1={}
#print(type(d1))        it'll print dictionary

"""emp={'empid':101,'empname':'abc','age':27}
print(emp)           #it'll print the key values in the same sequence
#print(len(emp))      shows length 3
#emp.clear()  delete all the elements
#print(emp['empname'])    to print the particular value,we write keynote in[]
#print(emp.get('empname'))     get() is also used to print a particular value
#emp['empid']=102        it'll update the value given in the key empid
#emp['email']='aaa'        if key is not present then it'll add the value at the last
#emp.update({'empname':'def','contact':123})   update() updates the values and also add new values at the end
#emp.popitem()    it'll delete the last item of the dictionary by default
#emp.pop('empname')    it'll delete the item according to our need
#del emp['empname']    it'll delete the item according to our need
print(emp)   """


"""emp={'empid':101,'empname':'abc','age':27}
#k=emp.keys()          it returns the list of keys = dict_keys(['empid', 'empname', 'age'])
#k=emp.values()   it reurns the list of values = dict_values([101, 'abc', 27])
#k=emp.items()  it returns both keys and values in the form of tuple = dict_items([('empid', 101), ('empname', 'abc'), ('age', 27)])
print(k)             """

#Q.wap to create a dictionary for book, having book_id, name.
#print the dictionary
#add price into dictionary
# print the name of book
# update the price of dictionary
# remove the bookid from dictionary
"""book={'book_id':101,'name':'Harry Potter'}
print(book)         #print the dictionary

book['price']=1000       #add price into dictionary
print(book)

print(book['name'])         # print the name of book

book['price']=1500            # update the price of dictionary
print(book)

book.pop('book_id')          # remove the bookid from dictionary
print(book)                """

###################################################################################################
# Nested dictionary
"""d = {1: 'hi', 2: 'there', 3: {4: 'how', 5: 'are', 6: 'you'}}
print(d)"""


# Adding elements to a Dictionary:
"""d = {}
print(d)
# adding elements one at a time:
d[0] = 'a'
d[1] = 'c'
d[2] = 1
print(d)
# adding set of values to a single key:
d[3] = ('s', 30, 'rr')
print(d)
# updating existing key's value:
d[1] = 'xd'
print(d)
#  Adding Nested Key value to Dictionary:
d[4] = {5: 'erw', 6: 34, 7: 'w2e'}
print(d)  """


# Accessing an element of a nested dictionary:
"""d = {1: 'hi', 2: 'there', 3: {4: 'how', 5: 'are', 6: 'you'}}
print(d[3][4])"""

# update():
"""d1 = {1: '2', 2: 'e', 3: 'd'}
d2 = {5: '3', 'o': 5}
d1.update(d2)
print(d1)"""


# demo for all dictionary methods
"""dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
dict2 = dict1.copy()
print(dict2)

# clear() method
dict1.clear()
print(dict1)

# get() method
print(dict2.get(1))

# items() method
print(dict2.items())

# keys() method
print(dict2.keys())

# pop() method
dict2.pop(4)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Scala"})
print(dict2)

# values() method
print(dict2.values())"""


# Add values to dictionary Using two lists of the same length:
"""roll_no = [10, 20, 30, 40, 50]
names = ['Rohan', 'Mohan', 'Sohan', 'Ram', 'Sham']
students = dict(zip(roll_no, names))
print(students)"""

# Converting a list to the dictionary:
"""l = ['a', 'b', 'c', 'd']
d = dict(enumerate(l))
print(d)"""


# Add values to dictionary Using the merge( | ) operator:
"""d1 = {1: 'a', 2: 'b'}
d2 = {3: 'c', 4: 'd'}
print(d1 | d2)"""


# Add values to dictionary Using the in-place merge( |= ) operator:
"""d1 = {1: 'a', 2: 'b'}
d2 = {3: 'c', 4: 'd'}
d1 |= d2
print(d1)"""


# Accessing Key-value in Dictionary:
# 1: using iteration
# d = {1: 'a', 2: 'b', 3: 'c', 'd': 4}
"""for i in d:
    print(i, d[i])"""

# 2. using list comprehension:
# print([(k, d[k]) for k in d])

# 3. Using dict.items() items():
# print(d.items())
"""for key, value in d.items():
     print(key, value)"""

# 4. Using enumerate():
"""for i in enumerate(d.items()):
    print(i)"""

# 5. Using for loop and items() method:
"""l = []               # creating an empty list
for key, value in d.items():        
    l.append((key, value))            # appending key,value into the list

for i in l:             # iterating the key,value pair in the list.
    print(i)"""



# Python del to delete objects:
# 1. Del Keyword for Deleting Objects:
"""class hey:
    a = 20
    def my_method(self):
        print("yes")
print(hey)
# del hey
# print(hey)"""

# 2. Del Keyword for Deleting Variables:
"""a = 20
b = 40
print(a)
print(b)
# del a
# del b
# print(a)
# print(b)"""

# 3. Del Keyword for Deleting List and List Slicing:
"""l1 = [1, 2, 3, 4, 5, 6]
l2 = ['a', 'b', 'c', 'd']
print(l1)
print(l2)
del l1[2]
print(l1)
del l2[1:3]
print(l2)"""

# 4. Del Keyword for Deleting Dictionaries and Removing key-value Pairs:
"""d = {1: 'a', 2: 'e', 's': 4, 'e': 5, 7: 'r'}
print(d)
del d['e']     # can delete by accessing key in the dictionary.
print(d)"""
