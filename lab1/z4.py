# Create a program that asks the user for a number and
# then prints out a list of all the divisors of that number.

number = int(input("Unesi broj: "))
newList = []

for div in range(1,number + 1):
    if number % div == 0:
        newList.append(div)

print(newList)