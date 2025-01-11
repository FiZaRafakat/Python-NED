#python datatypes
a = 10 #this is an integer datatype
b = 'Python$$$' #this is a string datatype
c = True #this is a boolean datatype
d = 5.24 #this is a float(decimal) datatype
e = complex(2,3) #this is a complex(imaginary number) datatype

#printing datatype of variable 'a'
print(type(a))
#printing datatype of variable 'b'
print(type(b))
#printing datatype of variable 'c'
print(type(c))
#printing datatype of variable 'd'
print(type(d))
#printing datatype of variable 'e'
print(type(e))


#Type Casting (from one datatype into another datatype)

type_casted = int(d) #change from 5.24 to 5
type_casted2 = float(a) #change from 10 to 10.00
type_casted3 = str(a) #change from integer 10 to string '10'
# type_casted4 = int(b) #change 'python' to integer
print(type_casted)
print(type_casted2)
print(type_casted3)
print(type(type_casted3)) #10 is a string now
print(type_casted3)
# print(type(type_casted4)) #not possible (value error)
# print(a + type_casted3) #not possible (type error)

#String Concatenation
str1 = 'Python'
str2 = 'Programming'
str3 = str1+str2
print(str3)  


