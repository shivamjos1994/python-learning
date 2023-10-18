"""class emp:
    empid=101
    empname="Sohan"
    empemail="Sohan@123"
    def display(self):              #self is default parameter
        print(self.empid,self.empname,self.empemail)
e1=emp()                            #e1 is the object/instance of the class emp.
e1.display()
e2=emp()
e2.display()   """
##################################################################################

"""class emp:
    def __init__(self,id,name,email):     #parameterized constructor(__init__)
        self.empid=id
        self.empname=name
        self.empemail=email
    def display(self):
        print(self.empid,self.empname,self.empemail)
e1=emp(101,"Sohan","Sohan@123")        #constructor calling
e1.display()

e2=emp(102,"Mohan","Mohan@321")         #constructor calling
e2.display()  """
####################################################################################

#Q create a class book and have 3 objects of the class:
"""class book:
    def __init__(self,name,author,price):
        self.b_name=name
        self.b_author=author
        self.b_price=price
    def show(self):
        print(self.b_name,self.b_author,self.b_price)
b1=book("Harry Potter","J.k. Rolling",900)
b1.show()

b2=book("Rich Dad Poor Dad","Robert Kiyosaki",899)
b2.show()

b3=book("Sapiens","Y.N. Harari",767)
b3.show()  """
####################################################################################

#Q.Write a python program using class which contains two variables of type integer.
# Create and initialize the object using parameterized constructor.
# Write a method to display maximum from given two numbers for all objects.
"""class maximum:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def max(self):
        if self.a>self.b:
            print(self.a,"is greater")
        else:
            print(self.b,"is greater")
m1=maximum(23,32)
m1.max()

m2=maximum(56,43)
m2.max()  """
##################################################################################

#Q.Write a program to perform all the arithmetic operations between two numbers
"""class maths:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("Addition: ",self.num1+self.num2)
    def sub(self):
        print("Substraction: ",self.num1-self.num2)
    def mul(self):
        print("Multiplication: ",self.num1*self.num2)
m1=maths(23,32)
m1.add()
m1.sub()
m1.mul()"""

