#wap to print day name after entering number of days(1-7):
a=int(input("Enter a day number(1-7): "))
if a==1:
    print("monday")
elif a==2:
    print("tuesday")
elif a==3:
    print("wednesday")
elif a==4:
    print("thursday")
elif a==5:
    print("friday")
elif a==6:
    print("saturday")
elif a==7:
    print("sunday")
else:
    print("invalid input!")