import re
"""Q1.Write a Python program to check that a string contains only a certain set of characters
(in this case a-z, A-Z and 0-9)."""
"""str = input("Enter a string: ")
reg = "[\W]"
if re.search(reg,str):
    print("String not matched,contains special character")
else:
    print("String matched!")"""


#Q2.Write a Python program to find sequences of lowercase letters joined with a underscore.
"""str = input("Enter a string: ")
reg = "[a-z]+[_][a-z]+"
if re.search(reg,str):        #NOT DONE
    print("matched")
else:
    print("not matched")"""


#Q3.Write a Python program that matches a word at the beginning of a string.
"""str = input("Enter a string: ")
print(str)
reg = input("Enter any letter: ")
if re.match(reg,str):
    print("First word matched!")
else:
    print("Try Again") """


#Q4. Write a Python program where a string will start with a specific number.
str = input("Enter a string starting with number 9: ")
reg = "[9][\w]{0,8}"
if re.match(reg, str):
    print("String is correct")
else:
    print("Try again!")


#Q5. Write a Python program to check for a number at the end of a string
"""str = input("Enter a string with a number at the end: ")
reg = "[a-z A-Z]+[\d]+?"
if re.search(reg,str):
    print("String is correct")
else:
    print("Try again!")"""


"""string = "Hdjsh asd2324234jghjsd hjsdg sdhk 12/21/2021 idf32432 32423 d34234jh df"
date = r'\d{2}/\d{2}/\d{4}'
dates = re.findall(date, string)
for date in dates:
    print(date) """


# finding email in a string:
"""str = "Welcome to the Jungle. my mail id is sam@gmail.com and gam@yahoo.com"
m = re.findall(r'\S+@\S+', str)
print(m)"""

