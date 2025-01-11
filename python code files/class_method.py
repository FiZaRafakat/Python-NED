"""
NonStatic/ Class Method: @classmethod
Key Points: If data is given in some different format when parsing or splitting is needed use class methods.

 """

class Employee :
    company = 'Google'
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    def show (self):
        print(f'Name: {self.name}\nSalary: {self.salary}\nCompany: {self.company}')
e = Employee('Ali', 2000)
e.company = 'Tesla'
e.show()
print(Employee.company)

#above the class variable remains unchanged, for manipulating/interacing with class variables user class methods
class Employee :
    company = 'Google'
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    def show (self):
        print(f'Name: {self.name}\nSalary: {self.salary}\nCompany: {self.company}')
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
e = Employee('Ali', 2000)
e.company = 'Tesla'
e.show()  
e.change_company('Apple') ##ab change hogi after using decorator, #setter
print(Employee.company)

#class methods as alternative constructors
class Person :
    def __init__(self,name,salary,age,company):
        self.name = name
        self.salary = salary
        self.age = age
        self.company = company
        pass
    @classmethod
    def splitting_input (cls, my_data):
        name, salary, age, company = my_data.split('$')

        return cls(name, int(salary), int(age), company)
    def info(self):
        print(f'Name:{self.name}\
              \nSalary: {self.salary}\nAge:{self.age}\nComapny: {self.company}')

my_str = 'Ali$120000$20$Google'
obj = Person.splitting_input(my_str)
obj.info()
print(obj.name)
