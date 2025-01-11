"""
CLASS METHODS: Defined under class scope
1) Instance Methods (self based)
2) Static --> @staticmethod  (no constructor needed)
3) Non-static --> @classmethods  ()

"""

"""
Static Methods: @staticmethod
Key Points:
---> No need for constructor for it, therefore no self is used.
---> It is a method that doesn't depend on object(or instance) but it is DEFINED inside the class
---> If method needs to access or modify the class's/object's atrributes it should be a class method not static
----> used in making utility programs (counter, v small checks, v simple processing (+), print)
"""
class Car:
    @staticmethod  #without using this 2 positional args given wala error aega
    def email_validation (user_email):
        # if '@' and '.com' in user_email:
        #     return True
        # else:
        #     return False
        return '@' and '.com' in user_email
c = Car()
print(c.email_validation('areeba@gmail.com'))
Car.email_validation(c)  #this is possible too if static dec is used

class Addition:
    @staticmethod
    def add(a , b):  #no self is needed
        return a + b
a = Addition()
print(a.add(2 , 4))  #output = 6
print(Addition.add(a))






