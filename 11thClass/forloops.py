# fruits = ['Apple','Banana','Cherry']
# for x in fruits:
#     print(x)


# # Iterate over a string
# for x in 'Banana':
#     print(x)

# str = "Pyhton is a programming language"
# for i in str:
#   print(i)


# # Exit the loop when x is "banana":

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
  
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
  
# #Continue Statement 

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# ## Range

# # Default
# for x in range(6):
#   print(x)

# # Starting Index
# for x in range(2, 6):
#   print(x)

# # Increment Sequence
# for x in range(2, 30, 3):
#   print(x)

# # Print all numbers from 0 to 5, and print a message when the loop has ended:

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# # Break the loop when x is 3, and see what happens with the else block:

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# # Nested Loop 

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)


# # pass Statement 

# for x in [0, 1, 2]:
#   pass

# Loops through a dictionaries

# Keys
std = {'name':"Fiza", 'Age':20}
# For Keys
for x in std:
  print(x)
for x in std.keys():
   print(x)
# values
for x in std:
  print(std[x])
for x in std.values():
  print(x)
# Complete Items 
for x in std.items():
  print(x)
for x,y in std.items():
  print(x,y)

# Task Questions :: 
'''Print the even number in range '''

# for number in range(1, 11):
#   if number%2 == 0 :
#     print(number)
#   else : print("The number is odd")

'''use input function and find it's odd or even '''

# user_input = int(input("Enter a number -------"))
# if user_input%2==0: 
#   print(f"The number {user_input} is even.")
# else : 
#   print(f"The number {user_input} is odd.")

'''Table of 5'''

# for i in range(1, 11):
#   res = 5 * i
#   print(f"5 * {i} = {res}")

'''Mutliple 2'''
for i in range(0, 21, 2):
  print(i)