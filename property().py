"""the main purpose of using getters and setters in object-oriented programs is to ensure data
encapsulation."""
""" Getters and Setters in python are often used when:
1.We use getters & setters to add validation logic around getting and setting a value.
2.To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified
by external user."""
"""In Python property()is a built-in function that creates and returns a property object. A property
object has three methods, getter(), setter(), and delete(). property() function in Python has four
arguments property(fget, fset, fdel, doc), fget is a function for retrieving an attribute value. fset
is a function for setting an attribute value. fdel is a function for deleting an attribute value. doc
creates a docstring for attribute. A property object has three methods, getter(), setter(), and delete()
to specify fget, fset and fdel individually. """


# Using property() function to achieve getters and setters behaviour:
"""class Prop:
   def __init(self):
     self._age = 0

   def get_age(self):
     print("getter method called")
     return self._age

   def set_age(self,a):
     print("setter method called")
     self._age = a

   def del_age(self):
      del self._age

   age = property(get_age, set_age, del_age)

p = Prop()
p.age = 10
print(p.age)"""


# Using @property decorators to achieve getters and setters behaviour:
"""class Prop:
  def __init__(self):
    self._age = 0

  @property                                 # getter function
  def age(self):
    print("Getter function called")
    return self._age

  @age.setter                                # setter function
  def age(self, a):              
    if (a < 18):
      raise ValueError("Age is not upto eligibility criteria")
    print("Setter function called")
    self._age = a

p = Prop()
p.age = 19
print(p.age)  """


"""try:
    a, b = [int(i) for i in input("Enter x and y: ").split()]
    op = input("Enter an operator ('+','-','*','/','%'): ")
except Exception as e:
    print(e)
else:
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    elif op == '%':
        print(a % b)"""

