#Single Inheritance:
"""class parent:
    surname="Joshi"
    city="Pune"
class child(parent):        #derived class of the base class
    name="Shivam"
    def display(self):
        print(self.name,self.surname,self.city)
c1=child()
c1.display()"""
##########################################################################

#Multilevel Inheritance:
"""class GP:                 #base class for parent()
    surname="AAA"          
class parent(GP):            #base class for child()/derived class for GP()
    middlename="BBB"
class child(parent):         #derived class for parent()
    name="CCC"
    def show(self):
        print(self.name,self.middlename,self.surname)
c1=child()
c1.show()"""
##########################################################################

#Hierarchical Inheritance: (one base class and multiple derived class)
"""class shape:
    def draw(self):               #function in the base class
        print("Will draw shape")
class circle(shape):
    def draw(self):            #function overriding(having same name and same parameters)
        print("Will draw circle")
class rectangle(shape):
    def draw(self):           #function overriding(having same name and same parameters)
        print("Will draw rectangle")
s1=shape()
c1=circle()
r1=rectangle()
s1.draw()
c1.draw()
r1.draw()  """
###########################################################################

#super(): accessing data of the immediate base class from the derived class
"""class A:
    a=100
class B(A):
    a=200
    def show(self):
        print(self.a,super().a)        #accessed data from the A() class
b1=B()
b1.show()   """
###########################################################################

#super():  accessing the methods from the immediate base class
"""class A:
    def show(self):
        print("A show")
class B(A):
    def show(self):
        print("B show")
    def display(self):
        self.show()
        super().show()
b1=B()
b1.display()    """
###########################################################################

#passing base class constructor to the derived class:
"""class parent:
    def __init__(self,surname):      #creating a constructor in the base class
        self.surname=surname        #defining the parameter of the base class
class child(parent):
    def __init__(self,name,surname):     #creating a constructor in the derived class
        self.name=name                 #defining the parameter of the derived class
        super().__init__(surname)        #passing base class constructor to the derived class
    def show(self):
        print(self.name,self.surname)     
c1=child("Shivam","Joshi")
c1.show()"""
############################################################################

# Destruction in Recursion:
"""class RecursionClass:
    def __init__(self, n):
        self.n = n
        print("Object is being created with n = ", n)

    def run(self, n=None):
        if n is None:
            n = self.n
        if n <= 0:
            return
        print("Running recursive function with n = ", n)
        self.run(n - 1)

    def __del__(self):
        print("Destructor called")


r = RecursionClass(5)
r.run()"""


