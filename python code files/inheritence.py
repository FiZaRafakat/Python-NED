"""
Explanation of Python Inheritance

Parent Class:
This is the base class from which other classes inherit.
It contains attributes and methods that the child class can reuse.

Child Class:
This is the derived class that inherits from the parent class.
The syntax for inheritance is class ChildClass(ParentClass).
The child class automatically gets all attributes and methods of the parent class unless overridden.
"""
#GENERAL SYNTAX
class ParentClass:
    def __init__(self, name):
        self.name = name
    def showName(self):
        print(self.name)
class Child(ParentClass):
    def show(self):
        print('I am', self.name)
obj = Child('Ahmed')
obj.show()
print(obj.name)
obj.showName()

class Employee :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show (self):
        print(self.name, self.age)
class Programming(Employee):
    def language (self):
        print('C++')

obj = Programming('Ali', 29)
print(obj.name)
print(obj.age)
obj.show()
obj.language()

"""
Method overriding is a concept in object-oriented programming 
where a child class provides its own version of a method that 
already exists in the parent class.
When you override a method, the child class's method replaces
 the parent class's method for objects of the child class. """

class Parent:
    def sound_of_animal(self):
        print('Generic')
class Child(Parent):
    def sound_of_animal(self):
        print('Bark')

obj = Parent()
obj.sound_of_animal()
obj1 = Child()
obj1.sound_of_animal()


"""Super Keyword in action for calling parent methods explicitly in child class"""
class Parent:
    def sound_of_animal(self):
        print('Generic')
class Child(Parent):
    def animal(self):
        super().sound_of_animal()
        print('Bark')

obj1 = Child()
obj1.animal()
class Parent:
    name = 'Ali'
    def showName (self):
        print(self.name)
class Child (Parent):
    def show(self):
        super().showName()
        print(' i am a child class')
obj = Child()
# obj.name = 'ALI'
# obj.showName('Ali')
obj.show()

"""Super keyword for importing constructor of parent class into child class"""
class Employee :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show (self):
        print(self.name, self.age)
class Programming(Employee):
    def __init__ (self, name, age, id):
        super().__init__(name, age)
        self.id = id
    def details (self):
        print(self.name, self.age, self.id)

obj = Programming('ali', '10', 555555)
obj.details()



