'''Write a program to implement an employee management system using classes, instances and inheritance.'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show(self):
        self.display()
        print("Department:", self.department)


m = Manager("Rani", 30000, "IT")
m.show()