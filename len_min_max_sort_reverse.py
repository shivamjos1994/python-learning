#l=[12,13,67,34,56,89]
#print(len(l))   returns number of elements
#print(min(l))   returns min value
#print(max(l))   returns max value
"""l.sort()      first,sort elements in ascending order
print(l)       then print (changes occures in the list)"""
"""l.reverse()    first reverse the elements 
print(l)            then print it  (changes occures in the list)"""
"""m=l.copy()
print(m)  """


##create a list and print the first index of occurence of entered element
# and print how many times the element is present(count(),index())
l=[10,12,13,14,15,16,10,12,13,10,16]
a=int(input("Enter an element: "))
i=l.index(a)
print("First occurence of element at ",i)
c=l.count(a)
print("Number of times element occured is ",c)



