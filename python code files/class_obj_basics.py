#class syntax
"""1) class name
2) objects instance
3) attribute
"""

"""Key Concepts: 
Class: A blueprint(template) for creating objects.
Object: An instance of a class.
Attributes: Variables that belong to a class or object.
Methods: Functions defined inside a class. """

# class My_Class:

#     #attribute
#     attribute = 'I am an attribute'

#     #method
#     def method (self):
#         print('Hello, this is method!!')

# #creating an object of my class
# obj = My_Class()

# #accessing attribute
# # print(obj.attribute)
# #calling method
# obj.method()

# #changing attribute
# obj.attribute = 'XYZ'
# print(obj.attribute)   #output: XYZ

""" Qs 1:
Create a class called Car with:
An attribute brand set to "Toyota".
A method show_brand() that prints the brand.
Create an object of the Car class and call show_brand().

Qs: 2 Create a class Person with:
its properties include name set to your_name
and the class greets the person whose name is 
(your_name). The greeting should be: 
'Hello, Good Morning (your name)'
The create instance and call greet

Qs 3: Reusing Methods
Create a class called Book with:
An attribute title set to "Python 101".
A method show_title() that prints
 "The title of the book is:" followed by the title.
A method info() that reuses show_title() and adds
 "This is a beginner's book.

Qs: 4   Create a class Book with following details: 
1- Title of book  ('Fluid Mechanics')
2- Pages of book (200 pages)
3- Author: ('XYZ')
The program must be capable of printing the summary of book 
using the following details. Code it with OOPs.

 """
# class Book:
#     title = 'Python 101'
#     def show_title (self):
#         print('The title of the book is:', self.title)
#     def info(self):
#         self.show_title()
#         print('This is a beginners book')

# obj1 = Book()
# # obj1.title = 'Freedom'
# # obj1.show_title()
# obj1.info()


#UNDERSTANDING GETTERS AND SETTERS
"""Getters retrieve and fetch the value of an attribute within a class
Setters are used to set the value of an attribute within a class

Why do we need to use them?
1- To control access to attributes 
(can't allow to set any value of attribute)
2- Validating (confirming/ checking values before checkig them)
"""
#without getters and setters
class Person:
    def __init__ (self, age, name):
        self.age = age
        self.name = name
    def person_details(self):
        print(f'Name: {self.name}\n Age: {self.age}')
obj = Person('21', 'xyz')
obj.person_details()
#setting invalid value to age
obj.age = '-3'  #NAME IS ALREADY SET 
# obj = Person ('-10', 'ABC' ) #invalid age
obj.person_details()

"""In order to control the attributes being invalid we use a check
using setters"""

#using getters and setters
class Person1:
    def __init__ (self, age, name):
        self._age = age
        self.name = name
    #getters
    def get_age(self):
        return self._age
    #setters
    #user can't directly set value of an attribute now, only valid values allowed
    def setting_age(self, age):
        if age >= 0:
            # print('Valid')
            self._age = age
        else:
            print('invalid age')


age_input = int(input('Enter age: '))
p = Person1(age_input,'ABC')

p.setting_age(age_input)  #setting age if valid (checking validity)
print(p.get_age()) #fetching valid age only keeping 