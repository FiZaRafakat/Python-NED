'''Key Concepts:
Class : A blueprint(template) for creating objects. 
Object : An instance of a class.
Attributes : Variables that belongs to a class or object.
Methods : Fucntions defined inside a class
'''

'''Syntax'''
# class My_class:
#     #attribute
#     attribute = 'I am an attribute'
#     # method
#     def method(self):
#         print('Hello , This is method !!')

# # Creating an object of my class
# Obj = My_class()
# # accesing attribute
# print(Obj.attribute)
# # calling method
# Obj.method()
# # Changing Attribute 
# Obj.attribute = 'Attribute Change'
# print(Obj.attribute)

'''
Level 1 : Accessing attributes and methods
Creata a class called Car with 

an attribute brand set to "Toyota"
A method show_brand() that prints the brand.
Create an object of the Car class and call show_brand

'''

# class Car:
#     brand = "Toyota"
#     def show_brand(self):
#         print("Corolla is a brand of : ",self.brand)

# Object = Car()
# print(Object.brand)
# Object.show_brand()

'''
Q2 :: Create a class Person with :
it's properties include name set to your_name
and the class Greets the person whose name is (your_name). The Greeting sholud be :
'Hello , Good Morning (Your_name)' 
then create instance and call greet...
'''

# class Person:
#     my_name = "Fiza"
#     def Greeting():
#         your_name = input("Your Name : ? \n")
#         print('Hello , Good Morning',your_name)

# Instance = Person()
# Instance.Greeting()


'''
Q2 :: Reusing Methods
Create a class Book with :
An attribute title set to "Python 101"
A method show_title()  that prints 
  "The Title of the book is : " followed by the title .
A method_info() that reuses show_title() and adds 
   "This is A beginner's Book "
'''

# class Book : 
#     title = "Pyhton 101"
#     def show_title(self):
#         print("The title of the Book is :", self.title)
#     def info(self):
#         self.show_title()
#         print("This is a beginner's book")

# Class = Book()
# Class.info()

'''
Q4 ::
Create a class Book with following details:
1) Title of Book ("Fluid Mechanics")
2) Pages of Book (200pages)
3) Author (Androw L. Gerhart)
The program must be capable of printing the summary of a book using the following details, Code it with OOP; 
'''

# class Book2:
#     title = "Fluid Mechanics"
#     pages = "200 Pages"
#     Author = "Androw L. Gerhart"
#     def summary(self):
#         print(f"The title Of the Book is {self.title}\n" 
#               f"The Author of the Book is {self.Author}\n" 
#                 f"There has {self.pages} Pages\n")
        
# Summary = Book2()
# Summary.summary()