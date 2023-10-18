"""l="python class"
for t in l:
    print(t) """

#wap to find how many lowercase letters are present in your name:
"""a=input("Enter your name: ")
count=0        #we give a count number to count the lowercase letters
for t in a:
     if t.islower():       #if letters are in lowercase
         count=count+1     #count will be initialized from 0 to the numbers of lowercse letters.
print(count)  """

#traversing string using while loop:
"""a=input("Enter your name: ")
count=0
while count<len(a):         count should be greater than length of string
      print(a[count])       we use slicing to separate each letter
      count=count+1       """

#wap to print your name in reverse order using while loop:
"""a=input("Enter your name: ")
count=len(a)-1
while count>=0:
    print(a[count],end="")    #we use end="" in order to print string in a single line, otherwise it'll print vertically
    count=count-1"""

#traversing string using while loop(counting lowercase letters):
"""lcount=0
a=input("Enter any name: ")
count=0
while count<len(a):
     if a[count].islower():
          lcount=lcount+1
     count=count+1
print(lcount)"""

