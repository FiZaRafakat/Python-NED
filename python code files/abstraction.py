"""Abstraction: 
Hiding code details, delivering functionality 
and generalized functions of program.
Encapsulation: 
Data Hiding, showing up necessary 
methods and attr , wrapping programs into reusable classes. 
--> abstract method
--> concrete methods (class, instance, static)
"""
from abc import ABC, abstractmethod

class Shape (ABC):
    @abstractmethod
    def area(self):
        pass
    def primeter (self):
        pass
#concrete class
class Square (Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area (self):
        return self.length * self.width
    def primeter(self):
        return self.length + self.width00

obj = Square (2 , 5)
print(obj.area())
print(obj.primeter())

class Payment (ABC):
    @abstractmethod
    def processPayment (self, amount):
        pass
class CreditCardPayment (Payment):
    def __init__(self, amount):
        self.amount = amount
    def processPayment(self):
        return f'{self.amount} paid via credit card'
class OnlinePayment (Payment):
    def __init__(self, amount):
        self.amount = amount
    def processPayment(self):
        return f'{self.amount} paid via online source'
c = CreditCardPayment(2000)
o = OnlinePayment(40000)
print(c.processPayment())
print(o.processPayment())

#created an automated interface
my_list = [CreditCardPayment(2000), \
           OnlinePayment(40000)]
for i in my_list:
    print(i.processPayment())



# def makePayment(paymentMethod, amount):
#     return paymentMethod.processPayment(amount)
    

# creditCard = CreditCardPayment()
# online = OnlinePayment()
# print(makePayment(creditCard, 2000))
# print(makePayment(online, 500))

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass  # Abstract method

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# def describe_animal(animal):
#     print(f"The animal says: {animal.sound()}")

# animal = [Dog(), Cat()]

# for i in animal:
#     print(i.sound())


"""

Question 1:

Create an Abstract class Shape with an abstract method
calculateArea() that can be implemented by any subclass.
Make 2 sub classes of the above class Square and Circle
each having 2 instant variables for calculating the 
area.

Question 2:

Create a Parent Abstract class with an abstract, 
method that can be implemented by any subclass,
used in calculating the cost of appliance.
Make 2 sub classes for each appliance of the above 
abstract class each having their own instant 
variables for calculating thier total_cost(Price).

Output: 
First Step Display this:
*****Welcome*****
# What do you want to buy?
# 1. Coffee Maker
# 2. Dish Washer
# 3. Microwave

2nd step display this: 
# Pick a Manufacturer:  (User Inputs the appliance)
# 1. Dawlence
# 2. Kenwood
# 3. Westpoint

Final Processed Output:
your selected appliance {appliance name} 
from {company name} costs {cost}

"""