# '''Instance and class Variables'''

# class  Person:
#     company = "Google" # class variable jo instance per check hota 
#     employee_count = 0  #to track the employee count 
#     def __init__(self):
#         # pass
#         Person.employee_count  +1 #hr insatnce py increment
#     def show_company(self):
#         print(f"Name : {self.name} ,\nSalary : {self.salary} ,\nCompany : {self.company}")

# p = Person()  # init runs for once ---> counter 1 
# p.name = "Ali"
# p.salary = 20000
# p.company = "Apple"
# p.show_company()  
# print(p.company)
# print(Person.company)  # class mei jo hai wohi variable Aye ga / class wala variable change nhi ho ga

# p1 = Person()  
# p1.name = "Fiza"
# p1.company = "Tesla"

# # class Person:
# #     def __init__(self): #is k ander k sary attr instance k hain
# #         self.name = "Ali"
# #         self.salary = 29000
# #         self.company = "Google"
# #     def show(self):
# #         print(f"Name : {self.name} ,\nSalary : {self.salary} ,\nCompany : {self.company}")

# # p = Person()
# # p.show()
# # p.name = "Ahmed"
# # p.show()
# # print(Person.name) # error coz it was not a class variable

# # Self is not a keyword / its a good practice
# '''
# Static Method

# '''

# #above the class variable remains unchanged , for manipulating/interacting with 
# class Employee:
#     company = "Google"
#     def __init__(self,name , salary):
#         self.salary = salary
#         def show(self):
#             print(f"Name : {self.name} , \nSalary : {self.salary} ,\n Company : {self.company}") 
            
                    
'''
CLASS METHODS : defined under class scope
1) Instance Methods (self based)
2) Static Methods --> @staticmethod (no constructor needed)
3) Non_Static --> @classmethods ()
'''

'''TASk'''


class Person:
    def __init__(self, name , salary, age, company):
        # self.name = name 
        # self.salary = salary
        # self.age = age
        # self.company = company
        pass
    @classmethod
    def splittingInput (cls, New_Data):
        name, salary,age, company = New_Data.split("$")
        return cls(name , int(salary), int(age) , company)
    
    def info(self):
        print(f"Name : {self.name}\
            \nSalary : {self.salary}\
            \nAge : {self.age}\
            \nCompany : {self.company}")
  
 
p = Person()
p.info()
data = "Ali$20000$27$Google"
p.splittingInput(data)

# name , salary , age , company = "Ali$20000$27$Google".split("$")
# # name = a[0]
# # salary = a[1]
# # age = a[2]
# # company = a[3]
# print(name , salary , age , company)
