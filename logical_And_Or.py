"""ch=input("Enter a character: ")
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("Vowel")
else:
    print("Consonant")  """

#wap to print  weekdays and weekend by entering the days number:
"""d=int(input("Enter a day number: "))
if d==1 or d==2 or d==3 or d==4 or d==5:
    print("Weekday")
elif d==6 or d==7:
    print("Weekend")
else:
    print("Invalid Input")  """


#Find the greatest among three numbers:
"""a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
    print("First is greatest")
elif b>a and b>c:
    print("Second is greatest")
elif c>a and c>b:
    print("Third is greatest")  """


#Candidate is recruited based on following criteria:If male, age should be above 30 yrs and height above 160.
# If female, age should be above 25yrs and height above 155.
ch=input("Enter your gender: ")
a=int(input("Enter your age: "))
h=int(input("Enter your height in cm: "))
if ch=="male" and a>30 and h>160:
    print("You are selected!")
elif ch=="female" and a>25 and h>155:
    print("You are selected!")
else:
    print("Your are not eligible")
