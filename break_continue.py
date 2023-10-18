"""l=[10,23,46,53,78,90,65,36,45]
for i in l:
    if i==78:
       # break      break will terminate the iteration after 78
       continue     # continue will skip 78 and continue the iteration to the end.
    print(i)     """   #break and continue comes under branching/jumping statement.

#list of 5 elements.User will enter an element,find the index of its first occurence:
"""l=[12,13,14,15,16]
a=int(input("Enter any element: "))
flag=0
count=0
while count<len(l):
    if a==l[count]:
        flag=1
        break
    count=count+1
if flag==0:
    print("Element is not present")
else:
    print("Element is present at ",count)  """

#wap to find how many times the entered element is present in list (homework)
"""l=[12,11,13,14,11,13,13,14,15,12,11,16]
a=int(input("Enter the element: "))
c=0
for i in l:
    if i == a:
      c=c+1
print("Number of occurence: ",c)"""

