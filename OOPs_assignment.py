"""Q1.Write a python program using class which contains two variables of type integer. Create and
initialize the object using parameterized constructor. Write a method to display maximum
from given two numbers for all objects """
"""class maximum:
      def __init__(self,num1,num2):
          self.a = num1
          self.b = num2
      def max(self):
          if self.a > self.b:
              print(self.a, "is greater")
          else:
              print(self.b, "is greater")
m1 = maximum(23,32)
m1.max()

m2 = maximum(45,33)
m2.max() """

#Q2. Write a program to perform all the arithmetic operations between two numbers.
"""class maths:
    def __init__(self,n1,n2):
        self.a = n1
        self.b = n2
    def add(self):
        print("Addition: ", self.a + self.b)
    def sub(self):
        print("Substraction: ", self.a - self.b)
    def mul(self):
        print("Multiplication: ", self.a * self.b)
    def div(self):
        print("Division: ", self.a / self.b)
m1=maths(20,10)
m1.add()
m1.sub()
m1.mul()
m1.div() """

#Q3.Write a program to find the records of students having greater marks.
"""class student:
    def __init__(self,n,a,m):
        self.name = n
        self.age = a
        self.marks = m
    def show(self):
        if self.marks >= 35:
            print(self.name,self.age,self.marks)
s=student("rohit",20,20)
s.show()
s1=student("mohit",20,36)
s1.show()"""

##########################################################################################
"""class Flight:
  def __init__(self,capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passengers(self,name):
      if not self.empty_seats():
         return False
      self.passengers.append(name)
      return True
    
  def empty_seats(self):
     return self.capacity - len(self.passengers)

flight = Flight(5)
people = ["Ram", "Sham", "Sohan", "Mohan", "Kishore", "Abdul"]
for person in people:
  if flight.add_passengers(person):
    print(f"{person} booked a seat successfully")
  else:
    print(f"{person} could not booked a seat, all seats has been taken.")"""



# we can sort the list elements that are dict with the help of key attribute:
"""person = [
  {"name":"Harry", "house":"Gryffindor"},
  {"name": "Cho", "house":"Ravenclaw"},
  {"name":"Draco", "house":"Slytherin"}
]
def f(p):                                   # creating a function that take the 'keys' of a dict 
  return p["name"]                          

person.sort(key=f)                        # sort() with key equal to the function

print(person)"""

# another way to this is with lambda function:
"""person = [
  {"name":"Harry", "house":"Gryffindor"},
  {"name": "Cho", "house":"Ravenclaw"},
  {"name":"Draco", "house":"Slytherin"}
]
person.sort(key=lambda x : x["name"])        # lambda function is used here.
print(person)"""