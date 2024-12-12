'''Creating a Tuple'''
tup = (1,2,3,4,5,6,8,10)
print(tup)
print(type(tup)) #datatype : tuples
print(len(tup)) # length : 05

# Accesing elements of Tupple
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-7])

# Understanding Slicing
print(tup[1:5])
print(tup[-7:-3])
print(tup[len(tup)-7:len(tup)-3])
print(tup[::-1])
print(tup[5:0:-1])
print(tup[-3:-8:-1])

# Can we store asingle value in tuple
tup1 = (1) # this is integer
tup2 = (1,) # Create a single value tuple
tup3 = 1 , 2, 3, 4, 5 # Creating tuple without ()
L = [1]
print(type(tup1))
print(type(L))
print(type(tup3))
tup5 = 1,
print(type(tup5)) 
tup4 = () #Empty tuple
print(type(tup4))

tup6 = ("Karachi",[1,2])
print(tup6)
print(len(tup6))
print(tup6[0])
print(tup6[1])
print(tup6[1][0]) # output = 1
print(tup6[1][1])

# Creating a tuple using tuple constructor
my_tuple = tuple(('KHI','LHR','ISL'))
print(type(my_tuple))

# type Casting in Tuples 
# my_tuple1 = int(my_tuple)
# # print(my)
# # print(my_tuple1) integer mei possible nhi 
my_tuple2 = str(my_tuple)
print(my_tuple2)
print(type(my_tuple2)) #Possible in string

# type_Casted = complex(my_tuple)
# print(type_Casted) Not Possible

Tuple = (1, 2,3, 4,5,6)
List = list(Tuple)
print(List) # Possible in list

# checking if 11 is in tuple``

if  11 in tup :
    print("Yes , It is Tuple")
else : 
    print("Not in tuple")

if 11  not in  tup : 
    print("Not, it is not ")
else :
    print("Yes it is not in tuple")

# Consecutively printing values in tuples
# for i in tup:
#     print(i, end = "   ",)  # To have output in one line


# Appending a Tuples
# There are two methods to insert elements in tuple 
# 1 To concetinate
myTuple = (1,2,3,4)
myTuple2 = ('a','b')
print(myTuple+ myTuple2)
# Use Append indirectly 
# First convert your tuple in a list
x = list(myTuple)
y = x.append(10)
print(x)
z = tuple(x)
print(z)


# Unpacking tuple

t = ('Apple','Mango','Banana')
(fruit1, fruit2, fruit3) = t
(fruit_first, *fruits_second) = t 
print(fruit1)
print(fruit2)
print(fruit2)
print(fruit_first)
print(fruits_second)
