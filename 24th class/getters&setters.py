# UNDERSTANDING GETTERS AND SETTERS
'''
Getters retrieve and fetch the value of an attribute within a class
Setters are used to set the value of an attribute within a class

Why do we need ot use them ?
1) To control access the attribute
(can't allow to set any value of attribute)
2) Validating (confirming/checking values before checking them)
'''
# get => to fetch /retrieve something
# set => To place / insert a value

# without getters and setters (simple method)
# class Person:
#     def __init__ (self, name, age):
#         self.name = name 
#         self.age = age #special attribute : positive integer
#     def display_info(self):
#         print(f"Name : {self.name} \n Age : {self.age}")

# p1 = Person("ABC",15)
# p1.display_info() 
# # If we want to change the one argument age and remain the name same so , we can do this like below
# p1.age = 9
# p1.display_info()
# p1.age = -7
# p1.display_info()

# With getters and setters

# class Person:
#     def __init__ (self, name, age):
#         self.name = name 
#         self._age = age #special attribute : positive integer  (thora different rkhny k liye we write _this after . )
#     def get_age(self):
#         return self._age
#     def set_age(self, new_age):
#         if new_age >= 0 : # implemented a check
#             self._age = new_age
#         else : 
#             print("Enter Valid Age:")
#     def display_info(self):
#         print(f"Name : {self.name} \n Age : {self._age}")

# p1 = Person("ABC",15)
# p1.display_info() 
# p1.set_age(15)
# print(p1.get_age())


#with using decorators 
# @property ---> Built-in decorators of python
# @<attribute>.setter ---> Built-in setter of pyhton

class Person:
    def __init__ (self, name, age):
        self.name = name 
        self._age = age #special attribute : positive integer  (thora different rkhny k liye we write _this after . )
    @property #getter
    def age (self):
        return self._age
    @age.setter #setter
    def set_age(self, new_age):
        if new_age >= 0 : # implemented a check
            self._age = new_age
        else : 
            print("Enter Valid Age:")
    def display_info(self):
        print(f"Name : {self.name} \n Age : {self._age}")

p1 = Person("ABC",15)
p1.display_info() 
p1._age = -5
