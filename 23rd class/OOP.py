#UNDERSTANDING OOPS USING CONSTRUCTOR
'''
Why to use Contructor?Intead of directly attribute within a class.
Constructors are used within a class defining before describing any method.
They are written with def __init__ dunder(double underscore) method.
They are used for :
1) Tracking multiple user defined attributes(input/variable)
2) Number of attribiutes can be given to a class instance, by not directly changing the class,
This save us from hardcoding , and modifying classes directly(incapsulations) 
'''

class Car:
    brand = "Suzuki"
    name = "Toyota"
    speed = 120
    color = "White"
    engine = '680cc'
    def CarDetails(self):
        print(f"BrandName : {self.brand}  \nCarName : {self.name}  \nSpped : {self.speed}  \nColor : {self.color}\n Engine : {self.engine}")

car1 = Car()
car1.CarDetails()

'''What if i create more than one brand/cars , then defining class in every time for brand call is a tricky way , and therefore , we use constructor'''

class Car:
    def __init__(self,brand, name, speed, color, engine):
        self.brand = brand
        self.name = name 
        self.spped = speed 
        self.color = color 
        self.engine = engine
    def CarDetails(self):
        print(f"BrandName : {self.brand}  \nCarName : {self.name}  \nSpped : {self.speed}  \nColor : {self.color}\n Engine : {self.engine}")

car1 = Car("Toyota","Fortuner",350,"Black","280cc")
car1.CarDetails()

'''Calculate area of circle with OOPs
must use constructor
'''
# class AreaOfCircle:
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         area_of_circle = (r**2)*3.142
#         return area_of_circle
    

# r  = int(input("Enter a value for r  \n"))
# Obj = AreaOfCircle(r)
# print(Obj.area())


'''Calcluate the annual salary of an employee, Initially having details of 
Name 
Salary/month 
Id
'''

# class Employee:
#     def __init__(self, name, id, salary):
#       self.Name = name
#       self.id = id 
#       self.salary = salary
#     def AnnualSalary(self):
#        annualSalary = self.salary*12
#        return annualSalary
#     def EmplyeeDetail(self):
#        print(f"The name of Employee : {self.Name}\nId : {self.id}\nMonthly Salary of {self.Name} is {self.salary} and Earned in a year {self.AnnualSalary()}")


# name = input("Enter a name Of Employee\n")
# id = int(input("Enter Id here:\n"))
# Salary = int(input("Enter Slaray Here : \n"))
# employee1 = Employee(name, id , Salary)
# employee1.EmplyeeDetail()


'''
Title 
author
isBorrowed 

The class should have following functions:
borrow() Set is isBorrowed to True (if, else)
return_book() set isBorrowed to false
display_info() display Book info 

and then, create another class library with following attributes:
book(list of book object)
the class should have :
add_Book() => Add book to the library
list_Book() => Print all details of the book  
search_book() => Search for a book by title 
'''

# class Book :
#     def __init__(self, title , author, isBorrowed):
#         self.Title = title
#         self.Author = author
#         self.IsBorrowed = isBorrowed
#     def CheckBookStatus(self):
#         if self.IsBorrowed == True:
#             return "Book is available"
#         else :
#             return "Book is not available"
#     def info(self):
#         print(f"Book Title : {self.Title}\nBook Author : {self.Author}\nBook Available : {self.CheckBookStatus()}")


# title = input("Enter a title for Book\n")
# author = input("Enter a Author Name\n")
# borrow_return = input("Type What you want , Here 1) Borrow 2) Return\n").lower()
# if borrow_return == "borrow":
#     Obj = Book(title , author, True)
#     Obj.info()
# else :
#     Obj = Book(title, author, False)
#     Obj.info()

