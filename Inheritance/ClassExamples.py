class Employee:

    employee_number = 0
    
    def __init__(self, name):
        self.name = name
        Employee.employee_number += 1
        self.employee_number = Employee.employee_number

    def print_information(self):
        print(f"Employee {self.name} - # {self.employee_number}")

class HourlyPaid(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.hourly_salary = salary
        self.has_free_coffee = False

    def print_information(self):
        super().print_information()
        print(f"Salary {self.salary} per hour")

    def can_use_employee_lounge(self):
        return False

class MonthlyPaid(Employee):
    def __init__(self, name, salary, benefits):
        super().__init__(name)
        self.monthly_salary = salary
        self.benefits = benefits

    def print_information(self):
        super().print_information()
        print(f"- Monthly: {self.monthly_salary} per month")
        print(f"- Benefits: {self.monthly_salary} ")

    def use_benefits(self):
        print(f"{self.name} uses benefit {self.benefits}")



employee1 = Employee("Juha")
employee1.print_information()

employee2 = HourlyPaid("John", 12)
employee2.print_information()

employee3 = MonthlyPaid("Peter", 2000, "dental")
employee3.print_information()
employee3.use_benefits()

employee4 = MonthlyPaid("Anna", employee2.hourly_salary * 80, "healthcare")

for employee in [employee1, employee2, employee3, employee4]:
    employee.print_information()
    if callable (employee.use_benefits()):
        employee.use_benefits()