'''Create an Employee class that stores an employee's name, basic salaery, house rent allowance (HRA) percentage, 
travel allowance, and deducations. Add instance methods to calculate gross salary and net salary. 
Gross salary is the basic salary plus HRA and travel allowance. Net salary is gross salary minus deductions. 
display the employee's name.gross salary, and net salary.'''

class Employee:
    def __init__(self, name, basic_salary, hra_percentage, travel_allowance, deductions):
        self.name = name
        self.basic_salary = basic_salary
        self.hra_percentage = hra_percentage
        self.travel_allowance = travel_allowance
        self.deductions = deductions

    def calculate_gross_salary(self):
        
        hra_amount = (self.hra_percentage / 100) * self.basic_salary
        
        gross = self.basic_salary + hra_amount + self.travel_allowance
        return gross

    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        
        net = gross - self.deductions
        return net

    def display_details(self):
        gross = self.calculate_gross_salary()
        net = self.calculate_net_salary()
        print("\n--- Employee Salary Details ---")
        print(f"Employee Name : {self.name}")
        print(f"Gross Salary  : ₹{gross:.2f}")
        print(f"Net Salary    : ₹{net:.2f}")


emp1 = Employee("Rohit Verma", 50000, 20, 5000, 3000)
emp1.display_details()