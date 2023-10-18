#Q1.Write a Python script to check whether a given key already exists in a dictionary
"""emp={'ename':"abc",'eid':101,'esal':20000}
a=input("Enter the key: ")
k=emp.keys()
if a in k:
    print("Key is present is the dictionary")
else:
    print("Key is not present in the dictionary")  """


#Q2.Write a Python program to sum all the items in a dictionary.
"""sal={'sal1':1000,'sal2':2000,'sal3':3000}
i=sal.values()
s=0
for j in i:
    s=s+j
print(s)   """


#Q3.Write a Python program to multiply all the items in a dictionary.
"""s={'s1':10,'s2':20,'s3':3,'s4':6}
i=s.values()
m=1
for j in i:
    m=m*j
print(m)          """


#Q4.Write a Python program to sort a given dictionary by key.
"""s={'s1':21,'s6':20,'s4':30,'s5':19,'s3':5,'s2':23}
for k in sorted(s):
    print(k,s[k])     """

#Q5.Write a Python program to get the maximum and minimum value in a dictionary.
"""s={'s1':20,'s2':29,'s3':87,'s4':54,'s5':43,'s6':90}
k=s.values()
print("Minimum value in the dictionary: ",min(k))
print("Maximum value in the dictionary: ",max(k))"""
