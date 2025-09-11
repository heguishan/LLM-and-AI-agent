class Employee:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    def print_info(self):
        print(f"Your name is {self.name}, ID is {self.ID}")
class FulltimeEmployee(Employee):
    def __init__(self, name, ID, salary):
        super().__init__(name, ID)
        self.salary = salary
    def cal_salary(self):
        return self.salary
class PartTimeEmployee(Employee):
    def __init__(self, name, ID, daily_salary, day):
        super().__init__(name, ID)
        self.daily_salary = daily_salary
        self.day = day
    def cal_salary(self):
        return self.daily_salary * self.day
Employee1 = FulltimeEmployee("John", 50000, 5000)
Employee2 = PartTimeEmployee("Kim", 50001, 50, 100)

Employee1.print_info()
print(f"salary:{Employee1.cal_salary()}")
Employee2.print_info()
print(f"salary:{Employee2.cal_salary()}")