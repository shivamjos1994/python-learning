#l="python class"
#print(l.capitalize())    returns first letter of the first word in capital letter
#print(l.title())    returns every first letter of every word in capital letter
#print(l.lower())    returns the string in lowercase
#print(l.upper())  returns the string in uppercase
#print(l.isupper())  returns true if string is in uppercase
#print(l.islower())   returns true if string is in lowercase


#data="1234shivam"
#print(data.isalpha())  returns true if string has only alphabets
#print(data.isdigit())   returns true if string has only digits
#print(data.isalnum())   returns true if string has both alphabets and digits without space
#print(data.isspace())  returns true only if string has space only.


#wap taking password from user
# #no. of digits
# #no.of spaces
# #no.of characters
# #no of special characters
a=input("Enter password: ")
d=ch=spa=0
for i in a:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        ch=ch+1
    elif i.isspace():
        spa=spa+1
print("Number of digits are: ",d)
print("Number of characters: ",ch)
print("Number of spaces: ",spa)

#l="hey pyt$hon is a pyt$hon langu$age"
#print(l.count("python"))     count number of occurence
#print(l.index("python"))    returns index of the first occurence substring, returns error if substring is not found
#print(l.find("python"))    returns index of the first occurence substring, returns -1 if substring is not found
#print(l.replace("python","java",1))   1 is used to replace only 1st occurence of the substring with java
"""x=l.split('$')    split according to the $, by default split on the basis of white space
print(x)  """

