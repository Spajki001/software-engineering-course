# Ask the user for a number. Depending on whether
# the number is even or odd, print out an
# appropriate message to the user.

number = int(input("Unesi broj: "))

if (number % 4 == 0):
    print("Uneseni broj je dijeljiv sa 4")
elif (number % 2 == 0):
    print("Uneseni broj je paran.")
else:
    print("Uneseni broj je neparan.")