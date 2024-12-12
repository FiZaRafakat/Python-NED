#Task
# extract python form the following string.... 

pythonString = "I am learning python programming"
print(pythonString[14:21])

# extract first five charcters from 

welcome = "Welcome to python"
print(welcome[0:6])

# slice first 7 characters from "python Programming" and convert them to uppercase

string = "Python Programming"
sliceString = string[0:7]
print(sliceString.upper())

# find the word "python" from the above string

print(pythonString.find("python"))


# split the string "apple, cherry"

fruits = "apple , cherry"
print(fruits.split(" , "))