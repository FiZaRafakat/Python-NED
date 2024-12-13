str1 = 'introDuction tO Python Programming'

# print(str1.split())

splitted = str1.split()
print(splitted) #splitting string

joined = " ".join(splitted) #joining the splitted string
print(joined)

print(str1.count('o'))

# """TASK 1: s = 'ComPutEr'
# output: retupmoC
# output: OMPU
# output: op
# output: tupm

comp = 'comPutEr'
comp1 = comp.title()
print(comp1[::-1])
comp2 = comp.upper()
print(comp2[1:5])
comp3 = comp.lower()
print(comp3[1:4:2])
print(comp3[5:1:-1])

# TASK 2: Extract a substring from: 'Hello, World!'
String = 'Hello, World'
print(String[7:12])
# TASK 3: Reverse a string 'abcdefgh'
revString = 'abcdefgh'
print(revString[::-1])
# TASK 4: Generate a list from the following strings:
# 'apple banana grapes'
List = 'apple banana grapes'
print(List.split())
# TASK 5: Display Output of apple banana grapes as 
# 'apple-banana-grapes'
print(List.replace(" ",'-'))
# TASK 6: Extract only digits from 'a1b2c3d4e5f6'
String = 'a1b2c3d4e5f6'
digits = String.replace('a','').replace('b','').replace('c','').replace('d','').replace('e','').replace('f','')
print(digits)
# TASK 7: Swap the two strings in pyton: 'PythonProgramming' as 
# 'ProgrammingPython'
Python = "PythonProgramming"
print(Python[6:] + Python[0:6])

# TASK8: Reverse every word in a string: "python is fun" as:
# nuf si nohtyp 
# nohtyp si nuf

my_str = "python is fun"
print(my_str[::-1]) #output : nuf si nohtyp
print(my_str[0:6][::-1]+" "+ my_str[7:9][::-1]+ " " \
      + my_str[10:][::-1]) # output: nohtyp si nuf

print(my_str[-8:-14:-1], my_str[-5:-7:-1], my_str[-1:-4:-1])


# my_str2 = 'This is Introduction to Python Programming'
# #replacing the string/character
# replaced = my_str2.replace("Python", "JavaScript")
# print(replaced)

# #finding a character in a string
# find_char = my_str2.find("is")
# print(find_char)

""" 
Task 9: Implement 5 other string methods in your code.

Task 10: write a python program to eliminate 
vowels from the following string:
str = 'It's A beautiful Dayy!!

"""
# str = "It's A beautiful Dayy!!".lower()
# replaced_vowels = str.replace('a', "").replace('e', "").replace('i',"").replace('o',"").replace('u',"")
# print(replaced_vowels)