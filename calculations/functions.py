def add(a,b):
    return a + b

def sub(a,b):
    if a > b:
        return a - b
    else:
        return b - a

def mul(a,b):
    return a * b

def div(a,b):
    if a > b:
        return a//b
    else:
        return b//a

def square(a,b):
    print("Square of first number:",a**2)
    print("Square of second number",b**2)

def cube(a,b):
    print("Cube of first number:",a**3)
    print("Cube of second number:",b**3)