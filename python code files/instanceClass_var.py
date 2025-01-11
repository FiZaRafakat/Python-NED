"""Instance and Class Variables"""
"""KeyPoints:
1) Class Variable is written outside constructor and has no reference with self.
2) But Class variable is checked first on instance, is it is called on any instance it will beahve like an instance
variable.
3) All instance variables are changeable instance to instance and are written inside constructor,
explicitly mentioned with self. """
class Person:
    company = 'Google'  #class variable jo instance per check hota hai warna default ho /class se access ho
    employee_count = 0   #to track the employee count on every instance/ no of instances made
    def __init__(self):
        Person.employee_count += 1  #har instance per increment
    def show_company (self):
        print(f'Name: {self.name}\nSalary: {self.salary}\nCompany: {self.company}')
p = Person()  #init runs for once ---> counter = 1
p.name = 'Ali'
p.salary = 2000
p.company = 'Apple'
p.show_company()  
print(p.company)  #apple
print(Person.company)   #google
print(Person.employee_count)
Person.company = 'TESLA'
print(Person.company)
p1 = Person()  #init runs for once ---> counter = 2
p.name = 'Areeba'
p.salary = 100000
p.show_company()
print(Person.employee_count)

class Person:
    def __init__(self): #is k ander k saare attr instance k hain
        self.name = 'Ali'
        self.salary = 29000
        self.company = 'Google'
    def show(self):
       print(f'Name: {self.name}\nSalary: {self.salary}\nCompany: {self.company}')
p = Person()
p.show()
p.name = 'AHMED'
Person.name = 'Ahmed'
p.show()

print(Person.name) #error bcoz it was not a class variable