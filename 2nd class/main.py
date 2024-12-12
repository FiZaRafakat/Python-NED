# Built-in module
import random
random_number = random.randint(1,10)
print(random_number)

# External module
import pyjokes 
joke = pyjokes.get_joke()
print(joke)


# 2nd Miss

# Pyhton datTypes
# a = 10 #  intager data types
# b= "Ptyhon" #  string data types
# c= True  # boolean sdata type
# d = 5.24 # float (decimal) 
# e = complex(2,3) #complex(imaginary number)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# type_casted = int(d)
# type_casting = float(a)
# type_cast = str(a)
# type_cast2 = int(b)
# print(type_casted)
# print(type_cast)
# print(type(type_cast))
# print(type_casting)
# print(type_cast2) #Value Error
# print(a+ type_cast) # type error


# Basic Operatirs
#Arithmetic Operator

a= 15 
b = 10 
addition = a + b
multiplication = a * b 
substraction = a-b
division = a / b
power = a ** 2
floor_division = b//a
modulus = a % b
print(addition)
print(multiplication)
print(substraction)
print(division)
print(power) # power
print(floor_division) # returns quotient 
print(modulus) # returns reminder if any 


# String functions
name = "Python"
# legth method
nameshort = len(name)
print(nameshort)
#Index => Alphabet Address
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6]) throw an error
# find
print(name.find("t"))
# replace
print(name.replace("n","r"))
# count
print(name.count("o"))
# upper
print(name.upper())
#  lower
print(name.lower())
#  starts with ?
print(name.startswith("t"))
#  Ends with ?
print(name.endswith("n"))

