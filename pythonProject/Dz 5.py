class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def total_salary(self):
        total = 0
        for employee in self.employees:
            total += employee.salary
        return total

if __name__ == "__main__":
    emp1 = Employee("Oleg", "Manager", 15000)
    emp2 = Employee("Max", "Manager", 10000)
    emp3 = Employee("Maria", "Manager", 13000)

    dept = Department("IT Department")
    dept.add_employee(emp1)
    dept.add_employee(emp2)
    dept.add_employee(emp3)

    for employee in dept.employees:
        print(employee)

    dept.remove_employee(emp2)

    print("Total salary of", dept.name, ":", dept.total_salary())