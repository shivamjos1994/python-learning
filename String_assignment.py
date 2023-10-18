#1. Write a program to print your entered name in reverse order.
"""a=input("Enter your name: ")
c=len(a)-1
while c>=0:
    print(a[c],end="")
    c=c-1             """

#2.Write a program to print every third character of entered string.
"""a=input("Enter string: ")
print(a[2::3])    """

#3.. Write a program to find the number of characters present in string without using len()
"""a=input("Enter string: ")
c=0
while c<=len(a)-1:
     c=c+1
print("Number of characters: ",c)   """

#4.Write a program to print the number of vowels present in entered string.
"""a=input("Enter a string: ")
c=0
for i in a:
    if i in "AEIOUaeiou":
        c=c+1
print("Number of vowels: ",c) """

#5. Write a program to find a character present in string or not?if present in which index it is
#present .and how many times it is present
"""a=input("Enter a string: ")
b=input("Enter the character: ")
for i in a:
    if b in a:
       print(b,"is present in the string")
       break
else:
  print(b,"is not present")
for c in range(0,len(a)):
    if b==a[c]:
      print("Character first occurence at ",c)
print("Number of times character present is ",a.count(b))"""


