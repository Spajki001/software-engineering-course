# Create a program that asks the user
# to enter their name and their age.
# Print out a message addressed to them
# that tells them the year that they will
# turn 100 years old.

name = input("Upisi ime: ")
age = int(input("Upisi godine: "))
repeat = int(input("Koliko puta da ponovim poruku? "))

age100 = 2023 - age + 100

name_age = "Bok %s, godine %d imat ces 100 godina."%(name, age100)

for i in range(repeat):
    print(name_age)