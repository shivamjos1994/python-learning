#Q1. Write a Program to take two numbers from user and perform basic operations addition, subtraction,
#division and remainder.
"""a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Addition: ",a+b)
print("Substraction: ",a-b)
print("Division: ",a/b)
print("Remainder: ",a%b)  """
import math
import operator
import sys

#Q2.Write a program to take input from user for empId , name, salary and print the Employee Details.
"""id=int(input("Enter employee ID: "))
name=input("Enter employee name: ")
sal=int(input("Enter salary: "))
print("...........Employee Details............. ")
print("Employee ID: ",id)
print("Employee Name: ",name)
print("Salary: ",sal)  """

#Q3. Write a program to calculate the area of triangle. Ask input from user (0.5*base*height)
"""b=int(input("Enter base: "))
h=int(input("Enter height: "))
ar=0.5*b*h
print("Area of triangle: ",ar)   """

#Q4. Write a program to convert temperature from Fahrenheit to Celsius degree.
"""f=float(input("Enter temp in fehrenheit: "))
c= (f-32) * 0.5556
print("temp in celcius: ",c)  """

#Q5.Write a program to take year from user and find whether it is a leap year or not:
"""a=int(input("Enter a year of your choice: "))
if a%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")  """

#Q6.. Write a program to find the cube of number upto the given numbers by the user
"""a=int(input("Enter the limit: "))
c=1
while c<=a:
    print(c*c*c)
    c=c+1   """

#Q7. Write a program to find the sum of digits of a number.
"""a=int(input("Enter any number: "))
s=0
n=a
while n>0:
    r=n%10
    n=n//10
    s=s+r
print("Sum of digits: ",s)       """

#Q8. Write a program to find whether a number entered by the user is a palindrome or not.
"""a=int(input("Enter any number: "))
rev=0
n=a
temp=n
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
if rev==temp:
    print(temp,"is Palindrome")
else:
    print(temp,"is not Palindrome")   """

#Q9.Write a program to find the number of digits entered by the user.
"""a=int(input("Enter any number: "))
c=0
n=a
while n>0:
    n=n//10
    c=c+1
print("Number of digits: ",c)   """

#10. Write a program to swap two numbers(interchange the numbers)
"""a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Before swapping: a:",a,"b:",b)
a=a+b
b=a-b
a=a-b
print("After swapping: a:",a,"b:",b)  """

#Q11.. Write a program to input student marks by condition :
#a) Marks is greater than 0 and less than 50--FAIILED
#b) Marks is greater than 50 and less than 75--1st Class
#c) Marks greater than 75 –and less than 100 Distinction
"""a=int(input("Enter your marks to know result: "))
if a>0 and a<=50:
    print("FAILED")
elif a>50 and a<75:
    print("1st Class")
elif a>=75 and a<100:
    print("Distinction")
else:
    print("Enter Valid Marks!")   """

#Q12.Generate Fibonacci series of a given range
"""n=int(input("Enter the limit: "))
a,b,c=0,1,0
for i in range(n):
    a=b
    b=c
    c=a+b
    print(c,end=" ")  """

#Q13. Write a program to check the number entered by a user is Armstrong or not.
"""n=int(input('Enter any number: '))
s=0
a=n
temp=n
while a>0:
    r=a%10
    a=a//10
    s=s+r*r*r
if temp==s:
    print(temp,"is an Armstrong")
else:
    print(temp,"is not an Armstrong")    """

#Q(14a).Print the following patterns :
"""a)
     A
     B C
     D E F
     G H I J """
#Ans(14a)
"""n=4
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(61+n),end=" ")
        n+=1
    print() """

#Q(14b).
"""1
   1 2
   1 2 3 
   1 2 3 4 
   1 2 3 4 5 """
#Ans(14b)
"""n = 6
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=' ')
        n+=1
    print() """

#Q(14c).
"""1
   2 2
   3 3 3
   4 4 4 4
   5 5 5 5 5 """
#Ans(14c)
"""n = 6
for i in range(1,n):
    for j in range(1,i+1):
        print(i,end=' ')
        n+=1
    print() """

#Q15. Write a Python program to get the Python version you are using
"""import sys
print(sys.version) """

#Q16.Define a function that computes the length of a given list or string.
"""def find(str):
    c=0
    for i in str:
        c+=1
    return c
str = input("Enter a sting: ")
print(find(str))  """

""" Q17.Write a Python program which accepts a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers.   """
"""a = (input("Enter numbers with comma in between them: "))
l = a.split(",")
print(l)
t = tuple(l)
print(t) """


#Q18. Write a Python program to accept a filename from the user print the extension of that.
"""file = input("Enter a file name with the extension: ")
extension = file.split(".")
print("Extension of file is: ",extension[-1]) """

"""Q19.Write a Python program to display the first and last colors from the following list. 
 color_list = ["Red","Green","White" ,"Black"]  """
"""color_list = ["Red","Green","White" ,"Black"]
print(color_list[::len(color_list)-1]) """


"""Q20.Write a Python program to display the examination schedule. 
 (extract the date from exam_st_date). 
 exam_st_date = (11, 12, 2016)
 Sample Output : The examination will start from : 11 / 12 / 2016 """
"""exam_date = (24,4,2023)
print("Exam will start from: %i/%i/%i"%exam_date) """

"""Q21Write a Python program to print the documents (syntax, description etc.) of Python
 built-in function(s). 
 Sample function : abs()  """
"""func = input("Enter a function (without braces): ")
print(help(func)) """


#Q22.Write a Python program to concatenate all elements in a list into a string and return it
"""l = ['hey','there','how','are','you?']
print("List: ",l) """
"""c = ' '
for i in l:
    c = c+' '+i
print("String format:",c) """
#OR
"""x = ' '.join(l)
print(x) """

#Q23.Write a Python script to sort (ascending and descending) a dictionary by value
"""import operator
dict = {'a':12,'b':13,'c':16,'d':14,'e':15}
print("Original dictionary: ",dict)
asc = sorted(dict.items(),key=operator.itemgetter(1))
print("Ascending order:",asc)
desc = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
print("Descending Order:",desc) """

#Q24.Write a Python script to add key to a dictionary.
"""d = {'a':2,'b':6}
print("Original dictionary:",d)
x = d.update({'c':56})
print("Added key in the dictionary: ",d) """

#Q25.Write a Python program to sum all the items in a list.
"""l = [11,12,13,14,15]
print("List: ",l)
s = 0
for i in l:
    s = s+i
print("Sum of elements in the list: ",s) """

#Q26.Python program to print even length words in a string
"""str = input("Enter a string: ")
x = str.split(' ')
for i in x:
    if len(i) % 2 == 0:
        print(i,end=" ") """

"""Q27.Define a function sum() and a function multiply() that sums and multiplies (respectively)
all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and
multiply([1, 2,3,4]) should return 24. """
"""l = [1,2,3,4,5]
print("List: ",l)
def sum(l):
    s = 0
    for i in l:
        s = s+i
    print("Sum of elements of list: ",s)
def mul(l):
    m = 1
    for i in l:
        m = m * i
    print("Multiplication of elements of list: ",m)
sum(l)
mul(l) """

####################################################################################
                                  #Python Fundamentals-2
#Q1.Write a Python program to display the current date and time
"""import datetime
x = datetime.datetime.now()
print(x) """

#Q2.Write a Python program which accept the radius of a circle from the user and compute the area
"""r = float((input("Enter radius of circle: ")))
area = 3.14 * r * r
print("Area of circle: ",area) """

"""Q3.Write a Python program which accept the user's first and last name and print them in 
reverse order with a space between them """
"""f = input("Enter first name: ")
l = input("Enter last name: ")
x = f+" "+l
print("Full name: ",x)
c = len(x)-1
while c >=0:
    print(x[c],end="")
    c = c-1 """

#Q4.Write a Python program that accept an integer (n) and computes the value of n+nn+nnn.
"""n = int(input("Enter a number: "))
x = n + n * n + n * n * n
print("n+nn+nnn: ",x) """

"""Q5.Write a Python program to print the calendar of a given month and year.
 Note : Use 'calendar' module"""
"""import calendar
print(calendar.month(2023,5)) """


"""Q6.Write a Python program to get the difference between a given number and 17, if the number
is greater than 17 return double the absolute difference."""
"""n = int(input("Enter a number: "))
x = 17-n
y = 2 * (n-17)
if n <= 17:
    print("Difference: ",x)
else:
    print("Double difference: ",y) """


"""Q7.Write a Python program to get a new string from a given string where "Is" has been added
to the front.If the given string already begins with "Is" then return the string unchanged"""
"""def addis(x):
    if x.startswith("Is"):
        return x
    else:
        return "Is "+ x

x = input("Enter a string: ")
print(addis(x)) """

#Q8.Write a Python program to test whether a passed letter is a vowel or not.
"""a = input("Enter an alphabet: ")
ch = "AEIOUaeiou"
if a in ch:
    print("Vowel")
else:
    print("Consonant") """

#Q9.Write a Python program to concatenate all elements in a list into a string and return it.
"""l = ['hello','how','are','you','?']
print("List: ",l)

x = ' '.join(l)
print("String format: ",x)

#Or

c = ' '
for i in l:
    c = c+' '+i
print("String format: ",c) """

"""Q10.Write a Python program to print all even numbers from a given numbers list in the same 
order and stop the printing if any numbers that come after 237 in the sequence."""
numbers = [
  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,
  345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
  687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843,
  831, 445, 742, 717, 958,743, 527]
"""for i in numbers:
    if i%2==0:
        print(i,end=" ")
    elif i==237:
        break """

"""Q11.Write a Python program to print all even numbers present before 237 from the above 
list in the same order and odd numbers that come after 237 in the sequence"""
#NOT DONE

#Q12.Write a Python program to solve (x + y) * (x + y).
"""x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = (x+y) * (x+y)
print("({}+{}) ^ 2 = {}".format(x,y,z)) """

#Q13.Write a Python script to check if a given key already exists in a dictionary.
"""dict = {'name':'kaushal','rollno':2,'age':23}
a = input("Enter a key: ")
x = dict.keys()
if a in x:
  print("Key exists")
else:
  print("Key doesn't exist") """

#Q14.Write a Python program to iterate over dictionaries using for loops.
"""dict = {'book_name':'Harry Potter','Author':'J.K.Rowling','Price':900}
x = dict.items()
for i in x:
  print(i) """

"""Q15.Write a Python script to generate and print a dictionary that contains number 
(between 1 and n) in the form (x, x*x)."""
"""n = int(input("Enter the limit: "))
d = dict()
for x in range(1,n+1):
  d[x] = x*x
print(d) """

#Q16.Write a Python script to merge two Python dictionaries.
"""d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6}
#x = d1 | d2
#OR
#x = {**d1, **d2}
# print(x)
#OR
d1.update(d2)
print(d1) """

#Q17. Write a python program to find size of a tuple.
"""t = (1,2,3,4,5,6,7,)
#x = t.__sizeof__()
#OR
x = str(sys.getsizeof(t))
print("Sixe of tuple: ",x,"bytes")"""
"""NOTE:The sys.getsizeof() function includes the marginal space usage, which includes the garbage 
collection overhead for the object. Meaning it returns the total space occupied by the object 
in addition to the garbage collection overhead for the spaces being used."""

#Q18. Write a python program to join tuples if similar initial elements.
#NOT DONE

#####################################################################################
                     #Operators Conditional Statement & Loops

"""Q1.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
between 1500 and 2700 (both included)."""
"""for i in range(1500,2701):
    if i%35==0:
      print(i,end=" ") """

"""Q2.Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guess wrong then the prompt appears again 
until the guess is correct, on successful guess user will get a "Well guessed!" message, 
and the program will exit."""
"""a = int(input("Guess a number(1-9): "))
while True:
  if a<1 or a>9:
    print("Guess is not right")
    a = int(input("Guess a number(1-9): "))
  else:
    print("Well guessed.BYE!")
    break    """

"""Q3.Write a Python program to construct the following pattern, using a nested for loop.
*
**
***
****
***
**
*  """
"""n=4
for i in range(n):
  for j in range(i):
    print('*',end="")
  print('')

for i in range(n,0,-1):
  for i in range(i):
    print('*',end="")
  print('') """

#Q4.Write a Python program that accept a word from the user and reverse it.
"""a = input("Enter a string here: ")
c = len(a)-1
while c >=0:
    print(a[c],end="")
    c = c-1 """

"""Q5.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
 Note : Use 'continue' statement."""
"""for i in range(0,7):
   if i==3 or i==6:
     continue
   print(i,end=" ") """

#Q6.Write a Python program to get the Fibonacci series between 0 to 50.
"""a,b,c = 0,1,0
for i in range(50):
  a = b
  b =c
  c = a+b
  print(c,end=" ") """

"""Q7.Write a Python program which takes two digits m (row) and n (column) as input and 
generates a two dimensional array. The element value in the i-th row and j-th column of the 
array should be i*j."""
"""row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
arr = [[0 for j in range(col)]for i in range(row)]
for i in range(row):
  for j in range(col):
     arr[i][j] = i*j
 
print(arr) """

"""Q8.Write a Python program which accepts a sequence of comma separated 4 digit binary numbers
as its input and print the numbers that are divisible by 5 in a comma separated sequence."""
"""def binary(a):
  l = a.split(',')
  res = []
  for i in l:
    x = int(i,2)
    if x % 5 == 0:
       res.append(i)
  return ','.join(res)

a = input("Enter comma separated 4 digits binary numbers: ")
print(binary(a)) """

#Q9.Generate Fibonacci series of a given range. (example 1 1 2 3 8)
"""n = int(input("Enter the limit: "))
a,b,c=0,1,0
for i in range(n):
   a = b
   b = c
   c = a+b
   print(c,end=" ") """

#Q10.Write a program to check the number entered by a user is Armstrong or not.
"""n=int(input('Enter any number: '))
s=0
temp=n
while n>0:
    r=n%10
    n=n//10
    s=s+r*r*r
if temp==s:
    print(temp,"is an Armstrong")
else:
    print(temp,"is not an Armstrong") """

##########################################################################################
          #Collections in Python (String, List, Tuple, Set, Dictionary)

#Q1.Write a program to count the number 4 in a given list
"""
l = [1,2,3,4,5,4,6,4,4,5,7,4,3,2]
print("List: ",l)
# x = l.count(4)
# print("Number of occurence of 4 is",x,"times")
#OR
c = 0
for i in l:
  if i==4:
    c +=1
print("Number of occurence of 4 is",c,"times") """

"""Q2.Write a program to display the first and last colors from the following list. Given list 
color_list = ["Red","Green","White","Black"] """
"""color_list = ["Red","Green","White","Black"]
print(color_list)
x = color_list[::len(color_list)-1]
print(x) """

#Q3. Write a Program to create a List of Numbers and find the sum of elements.
"""l = [1,2,3,4,5,6,7]
print("List: ",l)
s = 0
for i in l:
  s+=i
print("Sum of elements: ",s) """

"""Q4.Create a Student list with at least 10 names ask values from user and append the list
with 10 Subjects . 
Perform the following on the List formed:
a) remove the element at index1
b) remove the last element
c) print the list in reverse order """
"""l = ['Maths','Physics','Chemistry','Geology','Geogaphy','Social Studies','History','English','Sanskrit','Hindi']
print("list: ",l)
s = input("Enter 10 students' name separated by comma: ")
l.append(s)
print(l)
# l.pop(1)    #a
# l.pop(-1)   #b
print(l[::-1]) """

#Q5.Create a List with atleast 10 numbers and find the largest and smallest element in List.
"""l =[12,24,36,42,57,62,77,48,79,17,]
print("List: ",l)
ma = max(l)
mi = min(l)
print("Maximum element: ",ma)
print("Minimum element: ",mi) """

#Q6.Write a program to replace the last element in a list with another list.
"""l1 = [1,2,3,54,6]
print("List1: ",l1)
l2 = ['hello',7,8,9,10]
print("List2: ",l2)
l1 = l1[:-1] + l2
print("Appended list at last: ",l1) """

#Q7.Write a program to create a List and then insert the context “Python is a language ” in the 3rd index.
"""l = [1,2,"hello",4,5,7,10]
print("List: ",l)
l.insert(3,"Python is a language")
print("Appended list: ",l)  """

#Q8.Write a Program to Create a List with and check the element is present or not.
"""l = [1,2,3,4,5,6,7,8,9,10]
print("List: ",l)
a = int(input("Enter a element of the list: "))
if a in l:
  print("Element present in the list")
else:
  print("Element not present in the list") """

"""Q9.Create a list with empId name salary taking input from user and then perform the action 
to update the name """
"""l = []
id = int(input("Enter ID of the employee: "))
name = input("Enter name of the employee: ")
sal = int(input("Enter salary: "))
l.append(id)
l.append(name)
l.append(sal)
print("List:",l)
name = input("Enter updated name of the employee: ")
l[1] = name
print("Updated List: ",l) """


"""Q2)Take 10 integer values  from user in a list.print the following

1.No.of positive numbers

2.no.of negative numbers

3.no.of odd numbers

4.no.of even numbers

5.no.of zeros """
"""l =[]
for i in range(10):
    a = int(input("Enter 10 integer values: "))
    b =l.append(a)
print("List: ",l)
p,n,e,o,z = 0,0,0,0,0

for i in l:
    if i > 0:
        p += 1
    elif i < 0:
        n += 1
    else:
        z += 1

    if i % 2 == 0:
        e += 1
    else:
        o += 1

print("Positive: ",p)
print("Negative: ",n)
print("Zeroes: ",z)
print("Even: ",e)
print("Odd: ",o)"""


"""def solve(s):
    for i in s.split():
        if i.isalpha():
            s = s.replace(i,i.title())
    return s
s=input("Enter: ")
print(solve(s))"""

"""Q10.. Write a program to take input from user and create a List, name it as Languages and
convert it to Tuples .Also try it vice versa"""
"""languages = []
for i in range(5):
    a = input("Enter the list language: ")
    languages.append(a)
print("Languages: ",languages)
t = tuple(languages)
print("Languages: ",t)"""

"""Q11. Create a List of your favorite songs. Then create a list of your
a) favorite movies. Join the two lists together (Hint: List1 + List2). Finally,
b) append your favorite book to the end of the list and print it"""
"""songs = ['s1', 's2', 's3', 's4']
movies = ['m1', 'm2', 'm3', 'm4']
print(songs)
print(movies)
# print(songs+movies)
songs.extend(movies)
print(songs)
songs.append('harry potter')
print(songs)"""

"""Q12. Create a Set and add some data to it by taking it from the user and traverse it. Also 
perform the following operations:
a) union
b) intersection
c) difference """
"""s1 = set()
for i in range(5):
    a = int(input("Enter the set1 elements: "))
    s1.update([a])
print("Set: ",s1)
s2 = set()
for i in range(5):
    a = int(input("Enter the set1 elements: "))
    s2.update([a])
print("Set: ",s2)
print("Union: ",s1|s2)
print("Intersection: ",s1&s2)
print("Difference: ",s1-s2) """

"""Q13. Create a dictionary with subjects as Keys and marks as values
Traverse the dictionary through loop ."""
"""d = {'Maths': 89, 'English': 94, 'Hindi': 95, 'Science': 91}
c = 0
for i in d:
    print(i,":",d[i],end=" ")
    c += 1 """

"""Q14. Create a dictionary and values from List, Set and tuples
Create a List of colors…
Create a tuples of Programming language
Create a Set of Numbers """
"""l = [('html','css','python'),('sql','mysql','c++'),('red','green','yellow')]
s = {}
for t in l:
  if t[0] in s:
    s[t[0]].update(set(t[1:]))
  else:
    s[t[0]] = set(t[1:])
  print(s)"""
"""Explaination: Go through each tuple in the list for e.g. (1, 2, 3) ( for t in l )
Then check if the first element in the tuple is in the dictionary i.e. dictionary has already 
a key with that value? ( if t[0] in s )If yes, then update the value which is a set with the new
elements in the tuple excluding the first element - because first element is the 
key ( s[t[0]].update(set(t[1:])) )It not, then create an item in the dictionary with
key = first element and value = set( remaining elements ) ( s[t[0]] = set(t[1:]) )"""

"""Q15. Create a String and perform the following functions on it:
a) to check the length of String
b) to convert the String to uppercase
c) to capitalize the String
d) to traverse the String using for loop """
"""s = input("enter the string: ")
print(s)
print("Length of string: ",len(s))
print("Uppercase string: ",s.upper())
print("Capitalized: ",s.capitalize())
c = 0
for i in s: 
   print(i,end=" ")
   c += 1 """

###############################################################################################
                                 #String

"""Q1. Write a Python program to count the number of characters (character frequency) in a 
string. Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}"""
"""def string(s):
   d = {}
   for i in s:
     keys = d.keys()
     if i in keys:
       d[i] += 1
     else:
       d[i] = 1
   return d
s = input("Enter a string: ")
print(string(s))"""

"""Q2+3.Write a Python program to add 'ing' at the end of a given string (length should be at
least 3).If the given string already ends with 'ing' then add 'ly' instead. If the string length
of the given string is less than 3, leave it unchanged"""
"""def string(s):
    length = len(s)
    if length > 3:
       if s[-3:] == "ing":
          s += 'ly'
       else:
         s += 'ing'
    return s
s = input("Enter the string: ")
print(string(s))"""

#Q4.Write a Python function that takes a list of words and returns the length of the longest one.
"""def string(s):
    max = 0
    for i in s.split():
        if max < len(i):
            max = len(i)
            word = i
    print("longest word is",word,"with a length of",max)
s = input("Enter words of your choice: ")
print(string(s))"""

#Q5.Write a Python program to remove the nth index character from a non empty string.
"""s = input("Enter a string: ")
n = int(input("Enter the index number of the element that you want to remove: "))
s = s.replace(s[n],"")
print(s)"""

#Q6.Write a Python program to remove the characters which have odd index values of a given string.
"""s = input("Enter a string: ")
s1 = ""
for i in range(len(s)):
    if i % 2 == 0:
        s1 = s1 + s[i]
print("Original string: ",s)
print("Final string: ",s1)"""

#Q7. Write a Python program to count the occurrences of each word in a given sentence.
"""def string(s):
  d = {}
  for i in s:
    keys = d.keys()
    if i in keys:
       d[i] += 1
    else:
      d[i] = 1
  return d
s = input("Enter string: ")
print(string(s))"""

"""Q8. Write a Python program that accepts a comma separated sequence of words as input and 
prints the unique words in sorted form (alphanumerically)."""
"""s = input("Input comma separated sequence of words: ")
w = sorted(set(s.split(',')))
print(w)"""

"""Q9. Write a python program to reverse string without affecting special characters if
present in string."""
"""def reverseString(text):
  index = -1

  # Loop from last index until half of the index
  for i in range(len(text) - 1, int(len(text) / 2), -1):
    # match character is alphabet or not
    if text[i].isalpha():
      temp = text[i]
      while True:
        index += 1
        if text[index].isalpha():
          text[i] = text[index]
          text[index] = temp
          break
  return text
string = input("Enter a string with special characters in it: ")
print("Input string: ", string)
string = reverseString(list(string))
print("Output string: ", "".join(string))"""

#############################################################################################
                               #LIST

#1. Write a Python program to sum all the items in a list.
"""l = []
for i in range(5):
     a = int(input("Enter the list elements: "))
     l.append(a)
print(l)
s = 0
for j in l:
    s += j
print("Sum of list elements: ",s)"""

#Q2. Write a Python program to get the largest number from a list.
"""l = []
for i in range(5):
   a = int(input("Enter the list elements: "))
   l.append(a)
print(l)
max = l[0]
for i in range(len(l)):
    if max < l[i]:
         max = l[i]
print("Max element: ",max)"""

"""Q3. Write a Python program to count the number of strings where the string length is 2 or
more and the first and last character are same from a given list of strings"""
"""l = []
for i in range(5):
      a = input("Enter the string elements of the list: ")
      l.append(a)
print("list: ",l)
c = 0
for i in l:
     if len(i) >= 2 and i[0] == i[-1]:
          c += 1
print("Number of strings: ",c)"""

"""Q4.Write a Python program to get a list, sorted in increasing order by the last element in 
each tuple from a given list of non-empty tuples."""
"""l = [(2, 5), (3, 4), (8, 7), (8, 1), (4, 3), (2, 0)]
print("Original list: ",l)"""
"""for i in range(0,len(l)):
    for j in range(0,len(l)):
         if(l[i][-1] < l[j][-1]):
             temp = l[i]
             l[i] = l[j]
             l[j] = temp
print("Sorted list: ",l)"""
#OR
"""l.sort(key = lambda x : x[-1])  #an optional parameter to specify how the items is sorted.
print("Sorted list: ",l)"""

#Q5. Write a Python program to remove duplicates from a list.
"""l = [1, 2, 3, 4, 5, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
print("Original list: ",l)"""
#print("List without duplicate elements: ",list(set(l)))
#OR
"""def hello(l):
     l1 = []
     for i in l:
        if i not in l1:
            l1.append(i)
     return l1
print("List without duplicate elements: ",hello(l))"""

#Q6.Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""arr = [[['*' for col in range(6)] for col in range(4)] for col in range(3)]
print(arr)"""

##########################################################################################
                              # Dictionary

# Q1. Write a Python script to sort (ascending and descending) a dictionary by value
"""dict = {'a': 1, 'b': 3, 'c': 4, 'd': 2, 'e': 7, 'f': 5 }
for i in sorted(dict.values()):
    print(i,end=" ")"""
#OR
"""import operator
dict = {'a':12,'b':13,'c':16,'d':14,'e':15}
print("Original dictionary: ",dict)
asc = sorted(dict.items(),key=operator.itemgetter(1))
print("Ascending order:",asc)
desc = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
print("Descending Order:",desc)"""

# Q2. Write a Python script to add key to a dictionary.
"""d = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:",d)
x = d.update({'d': 4})
print("Updated dictionary:",d)"""

# Q3. Write a Python script to concatenate following dictionaries to create a new one.
"""d1 ={'a': 1, 'b': 2}
d2 ={'c': 3, 'd': 4}"""
# x = d1 | d2
# x = {**d1, **d2}
# print(x)
# d1.update(d2)
# print(d1)

# Q4. Print anagrams together in python using list and dictionary.
"""def anagram(l):
  d = {}
  for i in l:
    key = ''.join(sorted(i))
    if key in d.keys():
      d[key].append(i)
    else:
      d[key] = []
      d[key].append(i)
  output = " "
  for key,value in d.items():
      output = output + ' '.join(value) + ' '
  return output
l = ['cat','dog','man','ant','tac','tan','anm','odg']
print(anagram(l))"""

# Q5. WAP to find HCF and LCM of two numbers?
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
hcf = 1
for i in range(2, a+1):
    if a % i == 0 and b % i == 0:
        hcf = i 
print("HCF:",hcf)
lcm = (a*b)//hcf
print("LCM:",lcm)"""

#############################################################################################
                                 # Functions
# Q1. Write a Python function to find the Max of three numbers
"""def max(a,b,c):
  if a > b and a > c:
    print(a," is max")
  elif b > c and b > a:
    print(b," is max")
  else:
    print(c," is max")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
max(a,b,c)"""

# Q2. Write a Python function to sum all the numbers in a list.
"""def sum(l):
  s = 0
  for i in l:
    s += i
  print("Sum of elements: ",s)

l = []
for i in range(5):
  a = int(input("Enter element of the list: "))
  l.append(a)
print("List: ",l)
sum(l)"""

"""Q3.Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"""
"""def string(s):
     c = len(s)-1
     while c >= 0:
         print(s[c],end="")
         c -= 1
s = input("Enter a string: ")
string(s)"""


"""Q4.Write a Python function that accepts a string and calculate the number of upper case 
letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""
"""def string(s):
    u = l = 0
    for i in s:
      if i.isupper():
        u += 1
      elif i.islower():
        l += 1
    print("No. of Upper case characters: ",u)
    print("No. of Lower case characters: ",l)

s = input("Enter a string: ")
string(s)"""


"""Q5.Write a Python function that takes a list and returns a new list with unique elements of
the first list. 
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]"""
"""def unique(l):
     l1 = []
     for i in l:
       if i not in l1:
         l1.append(i)
     return l1

l = [1,2,3,3,3,3,4,5]
print("Sample List: ",l)
print("Unique List: ",unique(l))"""


"""Q6. Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]"""
"""def even(l):
  l1 = []
  for i in l:
    if i % 2 == 0:
      l1.append(i)
  return l1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sample List: ",l)
print("Expected Result: ",even(l))"""


"""Q7. Write a Python function that takes a number as a parameter and check the number is 
prime or not"""
"""def prime(a):
  flag = 0
  for i in range(2,a):
    if a % i == 0:
      flag = 1
      break
  if flag == 0:
    print(a,"is prime")
  else:
    print(a,"is not prime")

a = int(input("Enter a number: "))
prime(a)"""


# Q8. Write a Python function that checks whether a passed string is palindrome or not.
"""def string(s):
    if s[::-1] == s:
      print("palindrome")
    else:
      print("not palindrome")


s = input("Enter a string: ")
string(s)"""


# Q9. Write a Python function to check whether a number is perfect or not.
"""def perfect(n):
  s, i = 1, 2
  while i * i <= n:
       if n % i:
          i += 1
       else:
         if i * (n // i) == n:
              s += i + n // i
         i += 1
  return s == n and n != 1

n = int(input("Enter a number: "))
if perfect(n):
    print(f"The number {n} is a perfect number")
else:
  print(f"The number {n} is not a perfect number")"""
"""In this Python function, we iterate from 2 to sqrt(n). For every number we find that divides 
evenly into n, we add it to the sum. If the number is its own pair (i.e., if n is a perfect 
square), we only add it once. In the end, if the sum is equal to n, and n is not 1, we return 
True (because the number is perfect). Otherwise, we return False."""


"""Q10.Write a Python function to create and print a list where the values are square of 
numbers between 1 and 30 (both included)."""
"""def square(n):
    l = []
    for i in range(1,n+1):
            l.append(i**2)
    print("List of square: ",l)

n = int(input("Enter the limit: "))
square(n)"""

###########################################################################################
                             # Lambda Functions
# Q1.Write a Python program to square and cube every number in a given list of integers using Lambda.
"""l = [1,2,3,4,5,6]
print("List: ",l)
x = map(lambda x : x**2, l)
y = map(lambda y : y**3,l)
print("Square: ",list(x))
print("Cube: ",list(y))"""

"""Q2.Write a Python program to create a lambda function that adds 15 to a given number passed
in as an argument, also create a lambda function that multiplies argument x with argument y 
and print the result."""
"""x = lambda x : x+15
print(x(3))

y = lambda a,b : a * b
print(y(4,3))"""


"""Q3. Write a Python program to create a function that takes one argument, and that argument 
will be multiplied with an unknown given number."""
"""def multiply(a):
    b = 5
    return a * b
print(multiply(5))
print(multiply(9))"""


# Q4. Write a Python program to check whether a given string is number or not using Lambda.
"""num = lambda x : x.replace('.','',1).isdigit()
# print(num('33e33'))
num1 = lambda y : num(y[1:]) if y[0] == '-' else num(y)
print(num1('-393802'))"""

###########################################################################################
                               # OOPS concepts
"""Q1.Create a below structure as mentioned in image-
a) Create Company class with a parameterized constructor with companyName
b) Create Department class with Parameterized constructor having dname."""
"""class Company:
  def __init__(self,cname):
    self.cname = cname


class Department(Company):
  def __init__(self,cname,dname):
    self.dname = dname
    super().__init__(cname)

  def show(self):
    print("Company name: ",self.cname,"\n","Department name: ",self.dname)"""


"""d = Department("Apple","IT")
d.show()"""

# Q2. Create Developer class with parameterized constructor language
"""class Developer(Department):
    def __init__(self,cname,dname,language):
      self.language = language
      super().__init__(cname,dname)
    def show(self):
      print("Company name: ", self.cname, "\n", "Department name: ", self.dname,"\n","Developer: ",self.language)"""

"""d = Developer("Apple", "IT", "Python")
d.show()"""

# Q3. Write a function to print CompanyName, Id, and language
"""def display(Developer):
  d = Developer("Apple", "IT", "Python")
  d.show()

display(Developer)"""


# Q.Write a program in Python to find prime factors of a given integer.
"""def prime(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = int(input("Enter a number: "))
print(f"Prime factors of {n} are: ",prime(n))"""


# Q. Write a program in Python to add two integer without using arithmetic operator?
"""def sum(x,y):
    while y != 0:
        temp = x & y
        x = x ^ y
        y = temp << 1
    return x

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
s = sum(a,b)
print(f"The sum of {a} and {b} is :",s)"""
"""Here we have used while loop to perform the iteration. Inside while loop there are some 
logics written to perform additions. Inside the while loop:
1. temp = x & y calculates the carry by performing a bitwise AND operation on x and y.
2. x = x ^ y calculates the sum of x and y without considering any carries. It uses the bitwise
XOR operator to perform the addition. 
3. y = carry << 1 shifts the carry to the left by 1 position, effectively preparing it to be 
added in the next iteration.
The loop continues until y becomes zero, which means there is no more carry left. Finally, the
function returns the sum, which is stored in x."""

# Q.Write a program in Python to find given number is perfect or not?
"""n = int(input("Enter a number: "))
s = 0
for i in range(1,(n//2)+1):
  r = n % i
  if r == 0:
    s += i
if s == n:
  print(f"{n} is a perfect number")
else:
  print(f"{n} is not a perfect number")"""

# Q. WAP to print prime numbers within given range:
"""import math
s = int(input("Enter the starting point: "))
e = int(input("Enter the end point: "))
for i in range(s,e+1):
  if i > 1:
    for j in range(2,int(math.sqrt(i))+1):
      if i % j == 0:
        break
    else:
      print(i,end=" ") """


# Q. LCM of two numbers:
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    greater = a
else:
    greater = b
while(True):
    if ((greater % a == 0) and (greater % b == 0)):
        lcm = greater
        break
    greater += 1
print("LCM:",greater) """

# Q. HCF of two numbers:
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
hcf = 1
for i in range(2,a+1):
    if a %  i == 0 and b % i == 0:
        hcf = i
print("HCF:",hcf)"""
# OR
"""num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    minimum = num2
else:
    minimum = num1
for i in range(1, minimum+1):
    if((num1 % i == 0) and (num2 % i == 0)):
        hcf = i
print("hcf/gcd of",num1,"and",num2,"=",hcf)"""


# Q. Replace the space in a string with a character without using replace():
"""s = input("Enter the string: ")
ch = input("Enter the character that you want to replace with spaces: ")
new = " "
for i in s:
    if i == " ":
        i = ch
    new += i
print(new) """

# Q. Python program to delete vowels in a given string.
"""s = input("Enter a string: ")
new = " "
vowels = "AEIOUaeiou"
for i in s:
    if i in vowels:
        i = ""
    new += i
print("New string:",new)"""


# Q. Python program to count the Occurrence Of Vowels & Consonants in a String.
"""def string(s):
    v = c = 0
    for i in s:
        if i in "AEIOUaeiou":
            v += 1
        elif i.isalpha():
            c += 1
    print("Vowel count: ",v)
    print("Consonant count: ",c)

s = input("Enter a string: ")
string(s) """


# Q.Python program to print the highest frequency character in a String.
"""s = input("Enter the string: ")
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
max = max(d.values())
for i in d:
    if d[i] == max:
        print(i,end=" ")"""


# Q.Python program to Replace First Occurrence Of Vowel With "-" in String.
"""def string(s):
    vowel = "AEIOUaeiou"
    for i in range(len(s)):
        if s[i] in vowel:
            s = s[:i] + '-' + s[i+1:]
            break
    return s

s = input("Enter a string: ")
print("Original string: ",s)
print("Modified string: ",string(s)) """


# Q. Python program to remove blank space from string.
"""s = input("Enter string: ")
new = " "
for i in s:
    if i != " ":
        new += i
print(new) """

# Q. Python program to concatenate two strings using join() method.
"""s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(" ","".join([s1,s2])) """

# Q. Python program to remove repeated character from string.
"""def string(s):
    unique = set()
    new = " "
    for i in s:
        if i not in unique:
            unique.add(i)
            new += i
    return new

s = input("Enter a string: ")
print("New string:",string(s))"""

# Q. Python program to calculate sum of integers in string.
"""s1 = input("Enter a string: ")
s = 0
for i in s1:
    if i.isdigit():
        s += int(i)
print(s) """

# Q. Python program to print all non-repeating characters in string.
"""s = input("Enter a string: ")
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
new = " "
for i in s:
    if d[i] == 1:
        new += i
print(new) """

# Q. Python program to copy one string to another string.
"""s1 = input("Enter a string: ")
s2 = " "
for i in s1:
  s2 += i
print("Original string: ",s1)
print("Copied string: ",s2)"""
# OR
"""s1 = input("Enter a string: ")
s2 = s1[:]
print("Original string: ",s1)
print("Copied string: ",s2)"""
# OR
"""s1 = input("Enter a string: ")
s2 = str(s1)
print("Original string: ",s1)
print("Copied string: ",s2)"""


# Q. Python Program to sort characters of string in ascending order.
"""s = input("enter a string: ")
l = list(s)
sort = "".join(sorted(l))
print(sort) """

# Q. Python Program to sort character of string in descending order.
"""s = input("Enter a string: ")
l = list(s)
sort = ''.join(sorted(l, reverse=True))
print(sort) """


"""Q. Given the participants' score sheet for your University Sports Day, you are required to
find the runner-up score. You are given  scores. Store them in a list and find the score of 
the runner-up."""
"""n = int(input("Enter the list size: "))
arr = map(int, input("Enter the scores: ").split())
l = [i for i in arr]
unique = []
for x in l:
  if x not in unique:
      unique.append(x)
sort = sorted(unique)
print("Runner up:",sort[-2])"""


"""Q. Given the names and grades for each student in a class of N students, store them in a 
nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names 
alphabetically and print each name on a new line."""
"""lists = []
listscore = []
for _ in range(int(input("Enter size: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    listscore.append(score)
    lists.append([score, name])

listscore = list(set(listscore))
scored = sorted(listscore)
secondmin = scored[1]

newlist = []
for i in lists:
  if secondmin == i[0]:
    newlist.append(i[1])
newlist.sort()

for name in newlist:
   print(name)"""

"""Q.The provided code stub will read in a dictionary containing key/value pairs of name:[marks]
for a list of students. Print the average of the marks array for the student name provided, 
showing 2 places after the decimal.
Example:
marks key : value pairs are
'alpha' : [20,30,40]
'beta' : [30,50,70]
query_name = 'beta'
The query_name is 'beta'. beta's average score is 
(30+50+70)/3 = 50.0 ."""
"""n = int(input("Enter the total number of students: "))
student_marks = {}
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
query_name = input("Enter the name of the student: ")
sum = 0
for name in student_marks.keys():
  if name == query_name:
     marks = student_marks[name]
     for i in range(0, len(marks)):
         sum += marks[i]
avg = sum / len(marks)
print("%.2f" % avg)"""


"""Q. Bob has a playlist of N songs, each song has a singer associated with it (denoted by an 
integer).Favourite singer of Bob is the one whose songs are the most on the playlist.
Count the number of Favourite Singers of Bob"""
"""def singer(l):
  d = {}
  res = 0
  for i in l:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  freq = max(d.values())
  for k, v in d.items():
    if v == freq:
      res += 1
  return res


N = int(input())
l = list(map(int, input().split()))
print(singer(l))
"""

# Square root of any number
"""def findsqrt(x):
    if x < 2:
        return 2

    y = x
    z = (y + (x/y))/2

    while abs(y-z) >= 0.00001:
        y = z
        z = (y + (x/y))/2
    return z

n = float(input("Enter a number: "))
print(findsqrt(n))"""

"""Q. the user enters a string and a substring. You have to print the number of times that the 
substring occurs in the given string. String traversal will take place from left to right, not 
from right to left."""
"""def count_substring(string, sub_string):
  count = 0
  start = 0
  while start < len(string):
    pos = string.find(sub_string, start)
    if pos != -1:
      count += 1
      start = pos + 1  # move just one character ahead
    else:
      break
  return count

if __name__ == '__main__':
  string = input("Enter string: ").strip()
  sub_string = input("Enter the substring that you want to count: ").strip()
  count = count_substring(string, sub_string)
  print(count)"""