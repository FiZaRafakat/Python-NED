# name = "Python"
# #displaying length of a string
# print(len(name))

# #Indexing in strings
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

# #String Slicing 
# print(name[0:2])
# print(name[1:6]) # output : ython
# print(name[1:len(name)]) # output : ython
# print(name[1:]) #output : ython

# print(name[0:7]) #output : Python
# print(name[:])  #output : Python
# print(name[0:len(name)])   #output : Python
# print(name[0:6])  #output : Python

# #Step Size 
# print(name[0:6:1]) #output : python
# print(name[0:6:2]) #output : pto
# print(name[0:6:3]) #output : ph
# print(name[::-1])  #output : nohtyp
# print(name[6:0:-1])  #output : nohty
# print(name[6:1:-1])  #output : noht
# #Extended Slicing (-ve indexing)
# #output: ytho
# print(name[-5:-1])
# #output : pyth
# print(name[-6:-2])
# # output: nohtyp
# print(name[::-1])

# #string methods
# str1 = 'introDuction tO Python Programming'
# print(len(str1))

# #capitalizing whole string
# print(str1.upper())

# #lowers the case of the whole string
# print(str1.lower())

# #returns the title case
# print(str1.title())

# #string multiplication/repeatition
# str2 = ' Group 2'
# # print(str2 * 10)

# #string concatenation
# print(str1 + str2)

# #using 'sep' in print
# print(str1, str2, sep =":")

# #using 'end' in print
# print(str1, end = str2)

# #
# print(str1.capitalize())

# # print(str1.split())

# splitted = str1.split()
# print(splitted) #splitting string

# joined = " ".join(splitted) #joining the splitted string
# print(joined)

# print(str1.count('o'))

# """TASK 1: s = 'ComPutEr'
# output: retupmoC
# output: OMPU
# output: op
# output: tupm

# TASK 2: Extract a substring from: 'Hello, World!'
# TASK 3: Reverse a string 'abcdefgh'
# TASK 4: Generate a list from the following strings:
# 'apple banana grapes'
# TASK 5: Display Output of apple banana grapes as 
# 'apple-banana-grapes'
# TASK 6: Extract only digits from 'a1b2c3d4e5f6'
# TASK 7: Swap the two strings in pyton: 'PythonProgramming' as 
# 'ProgrammingPython'
# TASK8: Reverse every word in a string: "python is fun" as:
# nuf si nohtyp 
# nohtyp si nuf
# """

#Task 8 : Reversing a word in a string: "python is fun"

my_str = "python is fun"
print(my_str[::-1]) #output : nuf si nohtyp
print(my_str[0:6][::-1]+" "+ my_str[7:9][::-1]+ " " \
      + my_str[10:][::-1]) # output: nohtyp si nuf

print(my_str[-8:-14:-1], my_str[-5:-7:-1], my_str[-1:-4:-1])


my_str2 = 'This is Introduction to Python Programming'
#replacing the string/character
replaced = my_str2.replace("Python", "JavaScript")
print(replaced)

#finding a character in a string
find_char = my_str2.find("is")
print(find_char)

""" 
Task 9: Implement 5 other string methods in your code.

Task 10: write a python program to eliminate 
vowels from the following string:
str = 'It's A beautiful Dayy!!

"""
str = "It's A beautiful Dayy!!".lower()
replaced_vowels = str.replace('a', "").replace('e', "").replace('i',"").replace('o',"").replace('u',"")
print(replaced_vowels)
