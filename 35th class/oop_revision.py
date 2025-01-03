# Class Syntax + constructor 

class Person:
    # create constructor (initailize with self/ value)
    def __init__(self, name , age , city = "Karachi" ):
        self.name= name 
        self.age = age 
        self.occ = 'Engr' # default values
        self.city = city 
    def show_info(self, salary):
        print(f"Name : {self.name} \nAge : {self.age} \nOccupation : {self.occ} \nCity : {self.city} \nSalary : {salary}")

# obj = Person("Fiza",20)
# obj.show_info(1000000)

# implement using getters and setters (attributes are 'get' and 'set') 

class Person:
    # create constructor (initailize with self/ value)
    def __init__(self, name , age , city = "Karachi" ):
        self.name= name 
        self.age = age 
        self.occ = 'Engr' # default values
        self.city = city
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def show_info(self, salary):
        print(f"Name : {self.name} \nAge : {self.age} \nOccupation : {self.occ} \nCity : {self.city} \nSalary : {salary}")
        print("*"*8)

# obj = Person("Fiza",20)
# obj.show_info(1000000)      
# obj.setName("Shiza")
# print(obj.getName())
# obj.show_info(1200000)
# print(obj.name)  #public
# print(obj.age)   #public


# Public (same as above), private(__age) , protected()

# Private
class Person:
    # Create Constructor (initailize with self/ value)
    def __init__(self, name , age , city = "Karachi" ):
        self.name= name 
        self.__age = age 
        self.occ = 'Engr' # default values
        self.city = city
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def show_info(self, salary):
        print(f"Name : {self.name} \nAge : {self.__age} \nOccupation : {self.occ} \nCity : {self.city} \nSalary : {salary}")
        print("*"*8)

# obj = Person("Fiza",20)
# print(obj.__dir__())  # dir pyhton ka dunder method
# # print(obj.__age)  # Error / this is not a attribute of person
# print(obj._Person__age)  #Access private modifier

# MRO
# Multiple Inheritance 
class A:
    pass
class C:
    pass
class B(C,A):
    pass
obj = B()
print(B.mro())

#superclass end mei honi chahye ,
#subclass super sy pehly , 
#repeat nhi honi chahye ,
#bottom sy start ho ga , 
#and uper jany k liye left ko prefer krna hai  