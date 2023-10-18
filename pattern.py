#1.Square Pattern
"""n = 6
for i in range(0,n):
    for j in range(0,n):
        print(" * ",end=" ")
    print()"""

#2. Hollow Square Pattern
"""n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("* ",end="")
        else:
            print(" ",end=" ")
    print()"""

#3. Left Triangle Star Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()"""

#4. Right Triangle Star Pattern
"""n = 5
for i in range(n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()"""

#5. Left Downward Triangle Pattern
"""n = 5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()"""

#6. Right Downward Triangle Pattern
"""n = 5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n,i,-1):
        print("*",end="")
    print()"""

#7. Hollow triangle star Pattern
"""n = 6
for i in range(1,n+1):
    for j in range(i):
        if j == 0 or j == i-1:
            print("*",end="")
        else:
            if i != n:
                print(" ",end="")
            else:
                print("*",end="")
    print()"""

#8. Pyramid Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()"""

#9. Hollow Pyramid Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k == 0 or k == 2*i-2:
            print("*",end="")
        else:
            if i != n:
                print(" ",end="")
            else:
                print("*",end="")
    print()"""

#10. Reverse Pyramid Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*(n-i)+1):
        print("*",end="")
    print()"""

#11. Diamond Star Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(2*(n-1-i)+1):
        print("*",end="")
    print()"""

#12. Hollow Diamond Star Pattern
"""n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        if k == 0 or k == 2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
    for k in range(2*(n-i-1)+1):
        if k == 0 or k == 2*(n-i-1)-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""

#13. Hourglass Star Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*(n-i)+1):
        print("*",end="")
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*(i-1)+1):
        print("*",end="")
    print()"""

#14. Right Pascal Star Pattern
"""n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end="")
    print()"""

#15. Left Pascal Star Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("*",end="")
    print()"""

# 16. Heart pattern
"""n = 6
# upper part of the heart
for i in range(n//2,n,2):
    # print first spaces
    for j in range(1,n-i,2):
        print(" ",end="")
    # print first stars
    for k in range(1,i+1,1):
         print("*",end="")
    # print second spaces
    for l in range(1,n-i+1,1):
        print(" ",end="")
    # print second stars
    for m in range(1,i+1,1):
        print("*",end="")
    print()
# lower part of the heart
for i in range(n,0,-1):
    for j in range(i,n,1):
        print(" ",end="")
    for k in range(1,i*2,1):
        print("*",end="")
    print()"""

# 17. Plus pattern program
"""n = 5
for i in range(n):
    for j in range(n):
        if i == n//2:
            print("*",end="")
        else:
            if j == n//2:
                print("*",end="")
            else:
                print(" ",end="")
    print()"""

# 18. Cross pattern program
"""n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""

# 19.Left Number Triangle Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""

# 20. Right Number Triangle Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()"""

# 21. Number Pyramid Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(k,end="")
    print()"""

# 22. Reverse Number Pyramid Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*(n-i)+1):
        print(k+1,end="")
    print()"""

# 23. Hollow Number Pyramid Pattern
"""n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    c = 1
    for k in range(2*i+1):
        if i == 0 or i == n-1:
            print(c,end="")
            c += 1
        else:
            if k == 0 or k == 2 * i:
                print(c,end="")
                c += 1
            else:
                print(" ",end="")
    print()"""

# 24. Number Diamond Pattern
"""n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    c = 1
    for k in range(2*i-1):
        print(c,end="")
        c += 1
    print()
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    c = 1
    for k in range(2*(n-i)-1):
        print(c,end="")
        c += 1
    print()"""

# 25. Hollow Number Diamond Pattern
"""n = 5
c = 1
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        if k == 0 or k == 2*i:
            print(c,end="")
            c += 1
        else:
            print(" ",end="")
    c = 1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(2*(n-i-1)-1):
        if k == 0 or k == 2*(n-i-1)-2:
            print(c,end="")
            c += 1
        else:
            print(" ",end="")
    c = 1
    print()"""


# 26.Alphabet Pyramid Pattern
"""n = 5
a = 65
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i+1):
        print(chr(a + k),end="")
    print()"""

# 27. Reverse Alphabet Pyramid Pattern
"""n = 5
a = 65
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*(n-i)-1):
        print(chr(a + k),end="")
    print()"""

# 28. Hollow Alphabet Pyramid Pattern
"""n = 5
a = 65
x = 0
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        if i == 0 or i == n - 1:
            print(chr(a + x),end="")
            x += 1
        else:
            if k == 0 or k == 2*i:
                print(chr(a + x), end="")
                x += 1
            else:
                print(" ", end="")
    print()"""

# 29. Alphabet Diamond Pattern
"""n = 5
a = 65
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print(chr(a + k),end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(2*(n-i-1)-1):
        print(chr(a + k),end="")
    print()"""

# 30. Hollow Alphabet Diamond Pattern
"""n = 5
a = 65
c = 0
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        if k == 0 or k == 2 * i :
            print(chr(a + c),end="")
            c += 1
        else:
            print(" ",end="")
    c = 0
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(2*(n-i-1)-1):
        if k == 0 or k == 2*(n-i-1)-2:
            print(chr(a + c),end="")
            c += 1
        else:
            print(" ",end="")
    c = 0
    print()"""


# 31. Number inverted Half Pyramid Pattern
"""n = 5
for i in range(1,n+1):
   for j in range(1,n-i+2):
       print(j,end=" ")
   print()"""