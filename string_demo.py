"""l="python language"
print(l[2])  #t          this is called slicing[]
print(l[-5]) #g
print(l[2:8])  #ython l   from 2-7 index (do not include the ending index)
print(l[3:])   #hon language
print(l[:7])  #python
print(l[-6:-2])       #ngua
print(l[::-1])   #reverse
print(l[-1:-7:-1])      #egaugn      """

"""lang="my favourite programming language is python programming language"
favourite=(lang[-27:-21])
print(favourite)       """


# strings are immutable, so in order to update we have two methods:
# 1. converting string into list,update it and again convert it into string:
"""str1 = "hey there"         # creating a string
print(str1)
l = list(str1)             # converting it into list
l[1] = 'E'                 # updating list
print(l)
str2 = ''.join(l)          # converting back into string
print(str2)"""

# 2. slicing is use, here slice the string upto where yo want to update, add the sliced string to it.
"""str1 = "hey there"
print(str1)
str2 = str1[0:1] + 'E' + str1[2:]
print(str2)"""

# Updating an entire string (assign the new value to the same variable):
"""str = "hey there"
print(str)
str = "how are you?"
print(str)"""


# deleting a character from a string (del keywaord throughs an error,so we use slicing in order to delete)
"""str = "Hey there"
print(str)
str1 = str[0:1]+str[2:]    # Hy there
print(str1)  """

# r or R is used to ignore escape sequence:
"""str = "Hello \"Ram\""      # Hello "Ram"
print(str)
str = r"Hello \"Ram\""     # Hello \"Ram\"
print(str)"""


# format()
"""str = "{} {}".format("hey", "there")
print(str)"""

"""str = "{1} {0}".format("there", "hey")      # positional formatting
print(str)"""

"""str = "{x} {y}".format(x="hey", y="there")    # keyword formatting
print(str)"""


# String alignment  (<10 = 10 spaces from left; ^10 = 10 spaces to center; >10 = 10 spaces to the center)
"""String1 = "|{:<10}|{:^10}|{:>10}|".format('hey', 'there', 'hello')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)"""

# slicing: islice() can be used from the itertools module.
# itertools.islice(iterable,start,stop[,step])
"""import itertools
str = "Hey there how are you?"
#print(itertools.islice(str, 1, 14)) # it'll give an object number
print(''.join(itertools.islice(str, 1, 14)))"""

