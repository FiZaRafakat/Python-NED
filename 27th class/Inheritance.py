# class Employee:
#     def __init__(self,name):
#         self.name = name 
#     def show_details(self):
#         print(self.name)

# e = Employee("ABC")
# e.show_details()

'''
Inheritance:: 
Single Inheritance
Multi Inheritance
Multilevel Inheritance
Hybrid Inheritance
'''

# #  using Inheritance
# class parentClass:
#     def __init__(self,name):
#         self.name = name 
#     def showName(self):
#         print(self.name)
# class ChildClass(parentClass):
#     def show(self):
#         print(self.name)

# obj = ChildClass("Ahmed")
# print(obj.name)
# obj.show()
# obj.showName()

# '''
# Create classes using single inheritance on the following scenerio.
# Parent Class (Employee)  {id , name , company}
# Child Class (Occupation) {occupation => Software Engineer}
# '''

# class pClass: 
#     def __init__(self, id , name , company):
#         self.name = name 
#         self.id = id 
#         self.company = company 
#     def show_Details(self):
#         print(f"Name : {self.name} \nId : {self.id} \nCompany : {self.company}")

# class childClass(pClass):
#     def show_in_Parent(self):
#         print(f"Name : {self.name} \nId : {self.id} \nCompany : {self.company} \nOccupation : Software Developer")

# obj = childClass("Fiza", "00490768","KPMG")
# obj.show_Details()
# obj.show_in_Parent()


'''
Overriding Concept:

When there is same function in parent and child , the python will not understand it's for child or parent :
and pyhton will not excute parent class method , it will always execute child class method ...

If it's required to give a same method in a parent and child class , then from saveside we use super keyword to override this concept......
'''

# class Parent:
#     name = "abc"
#     @classmethod
#     def show_name(cls):
#         print(cls.name)
# class Child(Parent):
#     @classmethod
#     def show_name(cls):
#         print(cls.name)

# obj = Parent()
# obj.show_name()
# Parent.name = "XYZ"
# obj.show_name()
# print(obj.__dir__())
# Parent.show_name()

# obj1 = Child()
# obj1.name = "fiza"
# obj1.show_name()

# class Parentclas:
#     def show_name(self):
#         print(self.name)
# class Child(Parentclas):
#     def show_name(self):
#         print(self.name)

# obj2 = Child()
# obj2.name = "Nazia"
# obj2.show_name()

# '''Using Super Keyword'''

# class Parent:
#     def show_name(self):
#         print("Python")
# class Child(Parent):
#     def info(self):
#         super().show_name()
#         print("I am a child class")

# obj1 = Child()
# obj1.name = "XYZ"
# obj1.info()

# '''With the same name as parent method'''

# class Parentclass:
#     def show_name(self):
#         print("Python")
# class Childclass(Parent):
#     def show_name(self):
#         super().show_name()
#         print("I am a child class")

# obj1 = Childclass()
# obj1.name = "XYZ"
# obj1.show_name()


'''Super keyword on constructor'''

# class PRclass:
#     def __init__(self,name,id):
#         self.name = name 
#         self.id = id
# class CHclass(PRclass):
#     def __init__(self, name , id , company , occupation):
#         super().__init__(name , id)
#         self.occupation = occupation
#         self.company = company
#     def display(self):
#         print(f"Name : {self.name}  \nId : {self.id} \nOccupation : {self.occupation} \nCompany : {self.company}")

# obj = CHclass("ABC",120, "Developer","Facebook")
# obj.display()

'''
Public (Acces outside class)
Private (write by double underscore , not accesed outside class)
Protected (single underscore , child classes sy hi access ho skty hain)
'''

# Public Modifiers

# class Person:
#     def __init__(self,id):
#         self.id = id

# obj = Person(56327)
# print(obj.id) # attribute is publicly accessible 
# print(obj.__dir__())

# Protected Modifiers

# class Person:
#     def __init__(self,id):
#         self._id = id  # attribute is protected

# obj = Person(78645)
# print(obj._id)  #to modify and access it is ethically wrong
# print(obj.__dir__())

# Private Modifiers 

'''
(When we use _varName then python does name mangling)

'''

# class Person:
#     def __init__(self,id):
#         self.__id = id  # attribute is protected

# obj = Person(78645)
# print(obj.__dir__())  
# # print(obj.__id) # This will giving us an error
# print(obj._Person__id)  # It will Work : Access private variable via this..........