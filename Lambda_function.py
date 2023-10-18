"""func = lambda s: ''.join([chr for chr in s if not chr.isdigit()])
print("String without digits: ", func("hey1028there67"))"""   # string without digits

"""func = lambda s: s + '!'
print("String with exclaimation: ", func("hi there"))"""  # top add ! at the end of string

"""func = lambda n: sum([int(x) for x in str(n)])
print(func(15689))"""



"""l = ["1", "2", "9", "0", "-1", "-2"]
print(sorted(l))
x = list(filter(lambda x: int(x) % 2 == 0 and int(x) > 0, l))  # filtered out the positive numbers
print(x)
x = list(map(lambda x : str(int(x)+10), l))    # add 10 to each element and make them string again
print(x)"""


# intersection of two arrays:
"""l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = [20, 10, 3, 7, 9, 23, 34, 2, 56]
x = list(filter(lambda x: x in l, l1))    # filter the elements that are present in both lists.
print(x)"""

