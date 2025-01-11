"""Polymorphism: The existance of an 
object into different forms
- Polymorphism is a concept in OOP but
 has no discrete syntax, unlike Inheritence.

Concepts in Polymorphism: 
1) Method Overriding (as discussed in inheritence)
2) Method Overloadig
3) Operator Overloading
"""

#Understanding Method Overriding
# class Parent:
#     def __init__(self, age , name):
#         self.age = age
#         self.name =name
#     def show(self):
#         print('I am a parent class')
# class Child (Parent):
#     def __init__(self, age, name, sal):
#         super().__init__(age, name)
#         self.sal = sal
#     def showinfo(self):
#         # super().showinfo()
#         print('I am a child class')

# obj = Child(10,  'abc', 3000)
# obj.showinfo()
# obj.show() #output: i am child class
# # obj.showinfo()

"""Method Overloading: Python doesn't support 
direct method (function) overlaoding
i.e If we use a function/ method with 
same name twice or more times in a class
it is known as method(function) overloading.

How to treat method overloading?
    1) By default arguments
    2) By VLA (variable length arguments) *args 
"""
# #Understanding Method Overloading (extended functionality)
# #overwriting + overloading
# class A:
#     def addition (self, a , b):  #overwritten by latest method
#         return a + b
#     def addition (self, a , b, c):  
#          return a + b + c
# #method is overloading with multioperands functionality

# obj = A()
# # print(obj.addition (2 , 3))
# print(obj.addition(2 ,3 ,4))

#overload only without overwriting it
#Treating overwriting with VLA (arbitrary pos arg)
# class A :
#     def addition (self, *args):
#         sum = 0
#         for i in args:
#             sum = sum + i 
#         return sum
# obj = A ()
# #now it is working on variable lenght argument
# print(obj.addition(1,2,3,5,7))
# print(obj.addition(22, 33, 44, 2, 4, 9, 80, 0, 5, 6))


# class A: 
#     def addition (self, a , b, c = 0):
#         return a + b + c
# obj = A()
# print(obj.addition(1 , 2))

"""Operator Overlaoding: 
Operators: Arithmetic ( +, - , * , / etc)
Comparison(<, >, ==), Bitwise (and, or etc) 
If some operator is overloaded beyond
its operations or capabilities is operator overloading.
How to treat it? 
    1) using dunder method (magic dunder method) 
    inside class, exclusively
    for the certain operator
"""

# #functionality of add (operator is extended here)
# print(2 + 3)  #used as sum
# print('2'+ '9') #used in concatenation
# print(int.__add__(1 ,2))
# print(str.__add__('A','B'))

"""
class A:
    pass
obj1 = A()
obj2 = A()
print(obj1 + obj2) == ??

"""
"""obj1 = 2 + 3i
    obj2 = 1 + 4i
    print(obj1+obj2)= 3 + 7i"""

# print(int.__add__(2 , 3))
# print(2 + 3)
class ComplexNum :
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(obj1 , obj2):
        return f'{obj1.real + obj2.real} + {obj1.imag + obj2.imag}i'
obj1 = ComplexNum(1 , 2)
obj2 = ComplexNum(2 , 3)
print(obj1 + obj2)  #3 + 5i


'''

Qs: Illustrate operator overloading on vector addition
vector 1 ( 2 , 3, 5) ==> 2i + 3j + 5k
vector 2 ( 1 , 4, 7) ==> i + 4j + 7k
(vector1 + vector2) ===> (2 + 1)i + (3 + 4)j + (5 + 7)k


Qs: Make employee eligible for bonus, if his salary is less.
obj1 = employee(sal=6666)  (make dunder method using __gt__/__lt__)
obj2 = employee(sal===8888)
if
    obj1>obj
    print(obj2 is valid for bonus)
else:
    print(obj1 is valid for bonus)

'''
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"
class Animal:
    def sound (self):
        return 'ABC'

d = Dog()
c = Cat()
e = Animal()
print(e.sound())
print(d.sound())
print(c.sound())


##created interface 
animal = [d , c, e]
animal = [Dog(), Cat(), Animal()]

for i in animal:
    print(i.sound())

# class Dog:
#     def sound(self):
#         return "Bark"

# class Cat:
#     def sound(self):
#         return "Meow"

# def test (animal):
#     print(animal.sound())

# animal1 = Dog()
# animal2 = Cat()

# test(animal1)
# test(animal2)