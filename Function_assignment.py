#Q1. Write a Python function to find the Max of three numbers.
"""def max(a,b,c):
    if a>b and a>c:
        print(a,"is max")
    elif b>a and b>c:
        print(b,"is max")
    else:
        print(c,"is max")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
max(a,b,c)    """

#Q2. Write a Python function to sum all the numbers in a list.
"""l=[12,13,11,14,15,16]
print(l)
def sum(l):
    s=0
    for i in l:
        s=s+i
    return s
s=sum(l)
print("Sum of all th elements in the list: ",s)   """

#Q3. Write a Python function to multiply all the numbers in a list
"""l=[1,2,3,4,5,6]
print(l)
def mul(l):
    m=1
    for i in l:
        m=m*i
    return m
m=mul(l)
print("Multiplication of all the elements: ",m)   """

#Q4.. Write a Python program to reverse a string.
"""def rev(s):
    #i=s[::-1]  #OR
    c=len(s)-1
    while c>=0:
        print(s[c],end="")
        c=c-1
s=input("Enter a string: ")
rev(s)              """

#Q5. Write a Python function to check whether a number falls in a given range.
"""def range(n):
        if n>=1 and n<=50:
            print(n,"lies in the given range")
        else:
            print(n,"doesn't lie in the given range")
n=int(input("Enter a number(1-50): "))
range(n)              """



#Q6.Write a Python function that accepts a string and calculate the number of upper case letters
#and lower case letters.
"""def even(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u=u+1
        elif i.islower():
            l=l+1
    print("Number of uppercase letters: ",u)
    print("Number of lowercase letters: ",l)
s=input("Enter a string: ")
even(s)                 """


