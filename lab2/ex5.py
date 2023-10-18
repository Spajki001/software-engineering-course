import json

class Employee:

    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"

# Load the employees from the JSON file
with open("./lab2/ex4-employees.json", "r", encoding="utf-8") as f:
    employees = json.load(f)

# Create a list to store the Employee objects
employees_list = []

# Iterate over the employees and create an Employee object for each one
for employee in employees:
    employee_object = Employee(employee["employee"], employee["title"], employee["age"], employee["office"])
    employees_list.append(employee_object)

for e in employees_list:
    print(e)
