'''
Functions in Class is called a Methods
There are types of Methods:
1) Instance Method
2) Static Method 
3) Class Method
'''
# #Instance Method

# class Employee:
#     def info(self):
#         print(f"{self.name} , {self.age}")

# p = Employee()
# p.name = "ABC"
# p.age = 10
# p.info()

# # Static Method

# class Employee:
#     @staticmethod
#     def info(name, age):
#         print(f"{name} , {age}")

# p = Employee()
# p.info("ABC",10)

# class Email:
#     @staticmethod
#     def isValid(user_email):
#         if "@" and ".com" in user_email:
#             return True
#         else : 
#             return False
        
# email = Email()
# user_email = input("Enter your Email : ")
# print(email.isValid(user_email))

# class Employee:
#     company = "Google"
#     def __init__(self,name):
#         self.name = name 
#         self.salary = 2000
#     def info(self):
#         print(f"{self.name} , {self.salary} , {self.company}")

# e1 = Employee("ABC")
# print(e1.name) #--> ABC 
# print(e1.salary) #--> 2000

# e1.salary = 5000
# print(e1.salary) #--> 5000

# e1.name = "XYZ"
# print(e1.name) #--> XYZ


# e1.info() #--> XYZ , Google
# e1.company = "Tesla"
# e1.info() #--> XYZ , Tesla

# print(Employee.company) #--> Google
# Employee.company = "Apple"
# print(Employee.company) #--> Apple

# class Employee:
#     def __init__(self, name , age , salary , company ):
#         self.name = name 
#         self.age = age 
#         self.salary = salary 
#         self.company = company 
#     def info(self):
#         print(f"{self.name} , {self.age} , {self.salary} , {self.company}")


# user_input = input("Enter Details")
# user = user_input.split(" ")
# name = user[0]
# age = user[1]
# salary = user[2]
# company = user[3]
# p = Employee(name , age , salary , company)


'''
1) class variable ko change krny k liye class sy call krna ho ga 
'''