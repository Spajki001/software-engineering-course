import json


class Employee:
    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def __str__(self):
        return f"{self.name} ({len(self.employees)} employees)"

    def employ(self, name, title, age, office):
        new_employee = Employee(name, title, age, office)
        self.employees.append(new_employee)

    def fire(self, name):
        for e in self.employees:
            if e.name == name:
                self.employees.remove(e)

    def load_from_json(self, path_to_json):
        with open(path_to_json, "r", encoding="utf-8") as f:
            employees = json.load(f)
            for employee in employees:
                self.employ(
                    employee["employee"],
                    employee["title"],
                    employee["age"],
                    employee["office"],
                )

    def save_to_json(self, path_to_json):
        with open(path_to_json, "w", encoding="utf-8") as f:
            employee_list = []
            for employee in self.employees:
                employee_list.append(
                    {
                        "employee": employee.name,
                        "title": employee.title,
                        "age": employee.age,
                        "office": employee.office,
                    }
                )
            json.dump(employee_list, f)

    def print_employees(self):
        """Print all employees to stdout in format:
        Company name
        ----------------
        1. Employee name (age), job_title @ office
        2. Employee name (age), job_title @ office
        ..."""
        for employee in self.employees:
            print(employee)


def main():
    nike = Company("Nike")
    print(nike)

    nike.employ("Homer Simpson", "CEO", 44, "Lobby")
    nike.employ("Marge Simpson", "CTO", 33, "Lobby")
    print(nike)

    nike.fire("Homer Simpson")
    print(nike)

    # Implement load_from_json, save_to_json and print_employees methods
    # Then uncomment the implemented methods
    adidas = Company("Adidas")
    adidas.load_from_json("./lab2/ex4-employees.json")
    # After loading from json, adidas should have all the employees from
    # json file
    print(adidas)
    # Print employees should now print all the employees
    adidas.print_employees()

    adidas.employ("Homer Simpson", "CEO", 44, "Lobby")
    adidas.employ("Marge Simpson", "CTO", 33, "Lobby")
    adidas.employ("Bart Simpson", "CEO", 44, "Lobby")
    adidas.employ("Lisa Simpson", "CTO", 33, "Lobby")
    print(adidas)
    adidas.print_employees()

    adidas.fire("Homer Simpson")
    adidas.fire("Marge Simpson")
    print(adidas)
    adidas.print_employees()

    # Saving employees db to a new file, the file should now have 2 more
    # employees (Bart and Lisa, since Homer and Marge were fired)
    adidas.save_to_json("./lab2/ex6-employees.json")


if __name__ == "__main__":
    main()
