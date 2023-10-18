#1. Write a program to print the sum of integer values present in list.
"""l=[1,2,3,4,5,6,7]
s=0
for i in l:
    s=s+i
print("Sum of values: ",s)     """

#2. Write a program to find entered name is present in list of employees name or not.
"""l=["Sohan","Rohan","Mohan","Rohit"]
a=input("Enter an employee name: ")
if a in l:
    print("Employee name is in the list")
else:
    print("Employee name not in the list")"""

#3. Write a program that accepts a list from user and print the alternate element of list.
"""l=[]
for i in range(5):
    a = int(input("Enter the list elements: "))
    b = l.append(a)
print("Elements of the list are: ",l)
c = l[:5:2]
print("Alternate elements of the list are: ",c)"""

#4.. Write a program that accepts a list from user. Your program should reverse the content of list
#and display it. Do not use reverse() method.
"""l=[]
for i in range(5):
    a = int(input("Enter list elements: "))
    b = l.append(a)
print("Elements of the list are: ",l)
c=l[::-1]
print("Reversed elements of the list are: ",c)"""

#5.Find and display the largest number of a list without using built-in function max(). Your
#program should ask the user to input values in list from keyboard.
"""l=[]
for i in range(5):
    a=int(input("Enter the list elements: "))
    b=l.append(a)
print("Elements of the list are: ",l)
m=l[0]
for c in l:
    if m<c:
        m=c
print("The max element in the list is: ",m)"""

#6.Write a program that rotates the element of a list so that the element at the first index moves
#to the second index, the element in the second index moves to the third index, etc., and the
#element in the last index moves to the first index.
"""l=[11,12,13,14,15,16]
l=l[-1:]+l[:-1]     
print("Rotated list: ",l) """

#7. Write a program that input a string and ask user to delete a given word from a string.
"""s = input("Enter a string: ")
a=input("Enter the word that you want to delete: ")
print("String Now: ",s.replace(a,"")) """


#8. Write a program with a function that accepts a string from keyboard and create a new string
#after converting character of each word capitalized. For instance, if the sentence is "stop and
#smell the roses." the output should be "Stop And Smell The Roses"
"""def cap(a):
    b = a.title()
    return b

a=input("Enter a string: ")
c = cap(a)
print("New String: ",c) """