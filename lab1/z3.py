# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements
# of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Unesi broj: "))

newlist = []

for el in a:
    if el < number:
        newlist.append(el)

print(newlist)

newOneLineList = [el for el in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if el < number]

print(newOneLineList)