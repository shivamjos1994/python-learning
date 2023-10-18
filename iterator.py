"""An iterator in Python is an object that is used to iterate over iterable objects like lists,
tuples, dicts, and sets. The Python iterators object is initialized using the iter() method.
It uses the next() method for iteration."""
"""string = "Hey there"
iterator = iter(string)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""

"""class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        else:
            self.x += 1
        return x


for i in Test(15):
    print(i)

for i in Test(5):
    print(i)"""

"""Iterable vs Iterator
Python iterable and Python iterator are different. The main difference between them is, iterable in 
Python cannot save the state of the iteration, whereas in iterators the state of the current iteration
gets saved."""

# Iterating over an iterator:
"""tup = ('a', 'b', 'c', 'd', 'e')
tup_iter = iter(tup)

print("Going inside of the loop")
for index, value in enumerate(tup_iter):            # to iterator over an iterator we use enumerate
     print(value)
     if index == 2:
         break
print("Outside the loop")
print(next(tup_iter))
print(next(tup_iter))"""

"""Note: In iterator, we can iterate over it and access the elements only one time, after completion 
of the loop, if we use next() then we'll get the StopIteration exception. Whereas, we can iterator over
the iterables multiple times."""

