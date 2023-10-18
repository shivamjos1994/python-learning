"""l1=[12,13,14]
#l1[1:3]=[34,67]  it'll replace 1st and 2nd index elements
l2=[90,76]
print(l1)
#l1.append(43)   wil add element at the last of the list
#l1.insert(2,90)  will insert element at any index, 90 inserted at 2nd index
#l1.extend(l2)   will join l2 to l1
print(l1)        #l1 will get more elements
print(l2)  """    #l2 remains same

"""l=[12,23,43,56,75,12,34]
print(l)
#l.clear()    clear all the elements from the list
#del l[2]   delete the element on the basis of index
#l.pop(2)    delete the element on the basis of index
#l.remove(12)   delete the element on the basis of value
print(l)  """

#wap taking 5 integer values from user in a list.print the sum of all the even numbers present list
l=[]
for i in range(5):
    a = int(input("Enter integer of your choice: "))
    l.append(a)
print(l)
sum=0
for i in range(5):
    if l[i] % 2 == 0:
        sum = sum+l[i]
print("Sum of even elements: ",sum)