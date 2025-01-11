#UNDERSTANDING GETTERS AND SETTERS
"""Getters retrieve and fetch the value of an attribute within a class
Setters are used to set the value of an attribute within a class

Why do we need to use them?
1- To control access to attributes ?
(can't allow to set any value of attribute)
2- Validating (confirming/ checking values before checkig them)
"""
#get: to fetch/retrieve something
#set: to place/insert a value

#without getters and setters (simple methods)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age   #special/protected attribute: positive integer
    def display_info(self):
        print(f'Name: {self.name}\nAge: {self.age}')
p1 = Person('ABC', 15)
p1.display_info()
p1.age = 9
p1.display_info()
p1.age = -8
p1.display_info()

#with getters and setters
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    def get_age (self):
        return self._age
    def set_age(self, new_age):
        if new_age >= 0: #implemented a check
            self._age = new_age
        else:
            print('enter valid age')
    def display_info(self):
        print(f'Name: {self.name}\nAge: {self._age}') 
p1 = Person('ABC', 10)
p1.display_info()
p1.set_age(-25)
print(p1.get_age())
p1.display_info()

#with using decorators
#@property ---> builtin decorator of python
#@<attribute>.setter ----> builtin setter of python

#using decorators
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    @property  #getter
    def age (self):
        return self._age
    @age.setter  #setter
    def age(self, new_age):
        if new_age >= 0: #implemented a check
            self._age = new_age
        else:
            print('enter valid age')
    def display_info(self):
        print(f'Name: {self.name}\nAge: {self._age}') 
p1 = Person('ABC', 10)
p1.display_info()
p1.age= -25
p1.display_info()

# #####example
# #calculating fractions using getters and setters

# class Fraction:
#     def __init__(self, num, den):
#         self.num = num
#         self._den = den
#     @property
#     def denominator(self):
#         return self._den
#     @denominator.setter
#     def denominator(self, denominator_):
#         if denominator_>0:
#             self._den = denominator_
#         else:
#             print('Invalid, setting denominator to 1')
#             self._den = 1
#     def calculate_fraction(self):
#         return self.num/self._den

# frac = Fraction(4,2)
# print(frac.calculate_fraction())
# frac.denominator = 0
# print(frac.denominator)
# print(frac.calculate_fraction())  #will calculate on an older value