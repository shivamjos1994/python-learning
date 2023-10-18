#Method overloading is not allowed in Python
#Method Overriding:(method in the base class redefined in the derived class)
"""class Bank:
    p=1000
    t=3
    def si(self):
        print("Will calculate SI")
class Axis(Bank):
    r=8.9
    def si(self):
        si=(self.p * self.r * self.t)/100
        print(si)
class SBI(Bank):
    r=8.7
    def si(self):
        si = (self.p * self.r * self.t) / 100
        print(si)
a1=Axis()
s1=SBI()
a1.si()
s1.si() """
##############################################################################

#Abstraction: hiding data that we don't need
"""class A:
    a=100
    __b=200
    def show(self):
        print(self.a,self.__b)
a1=A()
#a1.show()    #private data only available to the method of the same class
print(a1.a)
print(a1.__b) """ #private data not available outside the class


#accessing private data in the derived class(not inherited in the derived class):
"""class A:
    a=100
    __b=200
class B(A):
    def show(self):
        # print(self.a)
        print(self.__b)       #cannot inherit the private data
b1=B()
b1.show() """
###############################################################################

# Polymorphism with class method:
"""class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()"""


# Polymorphism with function and objects:
"""class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

def func(obj):
	obj.capital()
	obj.language()
	obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)"""


# Polymorphism using inheritance and method overriding:
"""class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement thi s method")

class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow!"

obj = [Dog(), Cat()]
for i in obj:
    print(i.speak())"""

# Class or Static variable:
"""class A:
  name = "hi"                     # class variable
  def __init__(self,age):
    self.age = age                # instance variable

a = A(27)
b = A(28)
print(a.name)         # can access class variable using object
print(a.age)          # can access instance variable using object
print(A.name)         # can access class variable using Class 
A.name = "bye"        # can modify the class variable, it'll be applicable to both the objects
a.name = "bye"        # it'll be applicable only to the 'a' object
print(a.name)
print(b.name)"""



"""class A:
  staticVar = 0               
  def __init__(self):
     A.staticVar += 1
     self.instanceVar = A.staticVar         # incremented value to be stored in instance variable
a = A()                   # it'll make the static variable to 1
b = A()                   # it'll make the static variable to 2
print(a.instanceVar)      # prints 1
print(a.staticVar)        # prints 2  (as there are two objects right now so the static variable will be 2)
print(A.staticVar)"""     # prints 2  (with number of variable increased, there is increase in static variable)



# Class method and static method:
"""What is Class Method in Python? 
The @classmethod decorator is a built-in function decorator that is an expression that gets evaluated
after your function is defined. The result of that evaluation shadows your function definition. A 
class method receives the class as an implicit first argument, just like an instance method receives
the instance"""
"""A class method is a method that is bound to the class and not the object of the class. 
They have the access to the state of the class as it takes a class parameter that points to the class
and not the object instance.
It can modify a class state that would apply across all the instances of the class. For example, it 
can modify a class variable that will be applicable to all the instances."""

"""What is the Static Method in Python?
A static method does not receive an implicit first argument. A static method is also a method that is
bound to the class and not the object of the class. This method can’t access or modify the class state.
It is present in a class because it makes sense for the method to be present in class."""

"""Class method vs Static Method
The difference between the Class method and the static method is:
1.A class method takes cls as the first parameter while a static method needs no specific parameters.
2.A class method can access or modify the class state while a static method can’t access or modify it.
3.In general, static methods know nothing about the class state. They are utility-type methods that take
some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
4.We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create
a static method in python."""

"""class A:
  def __init__(self,value):
     self.value = value
    
  @staticmethod
  def maxValue(a,b):
      return max(a,b)

a = A(10)
print(A.maxValue(23,43))
print(A.maxValue(23,43))"""



"""from datetime import date
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  @classmethod
  def BirthYear(cls,name,year):
     return cls(name, date.today().year-year)

  @staticmethod
  def isAdult(age):
    return age > 18

p1 = Person("Mayank", 28)
p2 = Person.BirthYear("Mayank",2000)
print(p1.age)
print(p2.age)
print(p2.isAdult(22))"""
################################################################################


# Metaprogramming with Metaclasses in Python:
"""metaprogramming is the code that manipulates code."""
"""def test_method(self):
  print("This is test method")

class Base:
  def func(self):
    print("This is class method")

Test = type('Test', (Base,), dict(x = "sam",my_method=test_method))  # type(class name, (base classes in tuple), dictionary(contains arguments and methods))

t = Test()
print(type(Test))
print(type(t))
t.func()
t.my_method()
print(t.x)  """