"""l1=[]
l2=[12]
l3=[11,12,"hello"]
l4=[23,2.23,"hey"]
print(type(l1))      all are lists
print(type(l2))
print(type(l3))
print(type(l4))   """

"""l=[11,23,43,54,63,23,67,53,43]
print(l)
l[2]=34   2nd index element is replaced by 34
print(l) 
l[2:6]=[2,3,4,5]   #index from 2-5 got replaced by the new elements.
print(l)   """

#wap to check the entered cityname is present in the list or not?:
l=["Indore","New Delhi","Dehradun","Mysore","Guwahati"]
a=input("Enter city name: ")
if a in l:
    print("City present in the list")
else:
    print("City not present in the list")