# factorial:
"""def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)
n=int(input("Enter the number: "))
print(fact(n))"""

# Power:
"""def power(b,e):
    if e == 1:
        return b
    else:
        return b * power(b,e-1)

b = int(input("Enter base: "))
e = int(input("Enter exponant: "))
print("Power: ",power(b,e))"""


# HCF:
"""def hcf(a,b):
    if b == 0:
        return a
    else: 
        return hcf(b, a % b)
a = int(input("Enter first number: "))
b = int(input("Enter two numbers: "))
print(hcf(a,b))"""


#Sum of digits:
"""def sum(a):
    if a == 0:
        return 0
    else:
        return (a % 10) + sum(a//10)
a = int(input("Enter a number: "))
print("Sum of digits:",sum(a))"""

# Fibonacci Series:
"""def fib(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n =  int(input("Enter the limit: "))
for i in range(1,n+1):
     print(fib(i),end=" ") """


# Palindrome:
"""n = int(input("Enter a number: "))
def reverse(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse(n // 10)))
def pal(n):
    if n == reverse(n):
        return 1
    return 0
if pal(n) == 1:
    print(f"{n} is palindrome")
else:
    print(f"{n} is not palindrome") """



# Sum of digits:
"""def sum(n):
    if n == 0:
        return 0
    else:
        return ((n % 10) + sum(n // 10))

n = int(input("Enter a number: "))
print(sum(n)) """


