import re              #we've to import the re module

#use of findall
"""language="This is python programming python"
k=re.findall("python",language)
print(k) """

#use of search()
"""language="This is python programming python"
m=re.search("python",language)   #it'll return none if the substring is not present in the string
print(m.span())            #returns (8, 14)
print(m.string)           #returns This is python programming python
print(m.group())  """        #returns python

"""it'll return an object if the substring is present in the string.And we can use various function
in the object. span(),group() are the functions, string is an attribute"""

#use of split
"""language="Th-is is pyt-hon program-ming pyt-hon"
x=re.split("-",language)         #it'll split the string into the substrings
print(x)"""

#use of sub
"""language="This is python programming python"
x=re.sub("python","java",language)         #it replaces the substring with another substring
print(x) """

#making the patterns
"""data="gygpisteje"
reg="[tpy]"
if re.match(reg,data):     #it'll match only the first word in the string,if it's there then yes.
# if re.search(reg,data):    #it'll match if any of the words(tpy) is present in the string,order is not imp.
    print("matching")
else:
    print("not matching")"""


"""username="DDD7iop"
reg="[A-Z]+[0-9][a-z]+"     #this is pattern making(+ means we can add n number of characters)
if re.search(reg,username):
    print("correct")
else:
    print("incorrect")"""

"""Q. Wap to validate the entered contact number should have first digit 8 or 9 and 
total digits should be 10"""
"""contact = (input("Enter your phone number starting with 8 or 9: "))
reg ="[8-9][0-9]{8}[0-9]?"
if re.search(reg,contact):
    print("correct")
else:
    print("incorrect")"""

# re.search
# you can name your module:
# l = "hey there today's date is 10-10-2023"
# m = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})', l)
# print(m.group('mm'))

# Can show in tuple:
# m = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})', l)
# print(m.groups())                      # ('10', '10', '2023')

# can search fo ra particular group:
# print(m.group(2))

# individual match as a dictionary:
# m = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})', l)
# print(m.groupdict())

# Negation and lookahead:
# m = re.search(r't[^e]', l)  # will match the first occurence of any word that has 't' and followed by any other word
# m = re.search(r't(?!e)', l) # will match 't' followed by 'e'. returns none if not matched
# print(m)

# lookahead looks for a character that has been followed by another character:
# print(re.search(r'n(?=e)', 'Jasmine'))

# print(re.sub('date','mate',l))   # replaces a substring with another substring
# print(re.sub(r'([\d]{4})-([\d]{4})-([\d]{4})-([\d]{4})', r'/\1/\2/\3/\4', '1111-2222-3333-4444')) # /1111/2222/3333/4444



# Compiled Regex:  (useful)
"""The Python regular expression engine can return a compiled regular expression(RegEx) object using
compile function. This object has its search method and sub-method, where a developer can reuse it when
in need."""
# date = re.compile(r'([\d]{2})-([\d]{2})-([\d]{4})')       # now we can use it multiple times
# search method
# print(date.search('10-10-2023'))
# sub method
# print(date.sub(r'\1.\2.\3', '10-10-2023'))


# other functions:
# l = "Hey there. how are you my friend?"
# m = re.search("are", l)
# print("Starting point: ", m.start())
# print("Ending point: ", m.end())

# to find a character:
# m = re.search(".", l)      # will search 'H', the first character of a string
# m = re.search("\.", l)       # add '\' before '.' in order to recognize the '.'
# print(m)

# [] brackets:
# pattern = "[a-m]"         # will print 'a-m'
# m = re.findall(pattern, l)
# pattern1 = "[^a-m]"          # will print characters excluding 'a-m'
# m = re.findall(pattern1, l)
# print(m)

# (^) Caret symbol  (matches the beginning of any string):
"""pattern = "^The"
l = ["Hey there", "The fox is so foxy", "the mangoes are so sweet", "Theodore is a mid level king"]
for i in l:
    if re.match(pattern, i):
        print(f"Matched: {i}")
    else:
        print(f"Not matched: {i}")"""

# ($) Dollar symbol (matches the end of the string):
"""string = "Hey there how are you my friend"
pattern = r"friend$"
match = re.search(pattern, string)
if match:
	print("Match found!")
else:
	print("Match not found.")"""


# (.) Dot(.) symbol matches only a single character except for the newline character (\n):
"""string = "Hey there how are you my friend>?"
pattern = r"how.are"
m = re.search(pattern, string)
if m:
    print("matched")
else:
    print("not")"""

# (|) or OR symbol:  a|b will match any string that contains a or b such as acd, bcd, abcd, etc.

"""Star (*) symbol matches zero or more occurrences of the regex preceding the * symbol. 
For example –  
ab*c will be matched for the string ac, abc, abbbc, dabc, etc. but will not be matched for abdc
because b is not followed by c."""

# (<regex>) – Group:
# (a|b)cd will match for strings like acd, abcd, gacd, etc.


"""print(re.sub('ub', '~*', 'Subject has Uber booked already',
             flags=re.IGNORECASE))                             # will consider both the 'ub' with ignoring case
print(re.sub('ub', '~*', 'Subject has Uber booked already'))   # will not ignore case, and replace the 'ub' of Subject
print(re.sub('ub', '~*', 'Subject has Uber booked already',count=1,flags=re.IGNORECASE))"""  # count=1 means it'll consider max of 1 replacement

# subn:
"""subn() is similar to sub() in all ways, except in its way of providing output. It returns a tuple 
with a count of the total of replacement and the new string rather than just the string. """
"""print(re.subn('ub', '~*', 'Subject has Uber booked already',
             flags=re.IGNORECASE))       # ('S~*ject has ~*er booked already', 2)
print(re.subn('ub', '~*', 'Subject has Uber booked already')) """ # ('S~*ject has Uber booked already', 1)


# re.escape():
"""Returns string with all non-alphanumerics backslashed, this is useful if you want to match an 
arbitrary literal string that may have regular expression metacharacters in it"""
"""print(re.escape("This is awesome even at 1 am"))
print(re.escape("Hey there what's up & man, it's been [so] long since we meet man !!"))"""


# re.search:
"""regex = r'([a-zA-z]+) (\d+)'
string = "Today the date is October 10th."
m = re.search(regex, string)
print("Pattern at the index of ",m.span())
print("Full matched string: ",m.group())
print("Month: ",m.group(1))
print("Date: ",m.group(2))"""



# re.verbose:
'''def validate_email(email):
   regex_email = re.compile(r"""
                            ^([a-z0-9\.-]+)
                            @
                            ([0-9a-z\.-]+)
                            \.
                            ([a-z]{2,6})$"""
                           ,re.VERBOSE | re.IGNORECASE)
   res = regex_email.fullmatch(email)
   if res:
     print(f"{email} is valid. Details are as follows:")
     print(f"Local: {res.group(1)}")
     print(f"Domain: {res.group(2)}")
     print(f"Top level domain: {res.group(3)}")
   else:
     print(f"{email} is invalid. Enter valid email id.")

validate_email("shivamjos1994@gmail.com")
validate_email("hi788@gmail.com@hiodu2")
validate_email("alphamale007@yahoo.com")'''