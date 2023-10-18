#print numbers from 1 to 10:
"""for i in range(1,11):    1 is starting number and 11 is the last,excluding 11 ends with 10.
    print(i)  """

"""for i in range(1,11,2):  1 is the starting number,10 is the ending number,2 is the gap given in each number
    print(i) """

#wap to print entered name five times using for loop:
"""a=input("Enter your name: ")
for i in range(5):
    print(a)         """


#wap to print all the even numbers between 1-20:
"""for i in range(2,21,2):
    print(i)   
                OR """
for i in range(2,21):
    if i%2==0:
        print(i)