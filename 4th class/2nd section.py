# Miss Areeba

# Negative Indexing
name = "python"
print(name[-4:-1]) # => tho
# task ===> nohtyp

#StepSizing
print(name[0:6:2])  # Jump 2 multiply
# print(name[0:6:0])  # slice cannot be  zero => value error
print(name[0:6:]) # Write by default one 
print(name[::-1])  # for ltr => only one rtl => -1 

# String Methods 

str1 = "IntrOductiOn tO pythOn prOgraMminG"
str2 = " Hello World"
print(len(str1))  # =>> Length includes space as well
print(str1.upper())
print(str1.lower())
print(str1.title()) # returns title case => every words start from capital alphabet
print(str1.capitalize()) # returns only 1st words , 1st alphabet capital
print(str1.casefold()) # Converts string into lower case
print(str1+str2)
print(str1,str2)
print(str1, end=" Group 1" '\n')
print(str1 , str2 , sep=":")
str3 = "yes"
print(str3 * 4) # mutlipy 4 times yes 
print(f'This is a message from me :: {str1}')


'''
Task 
s = ComPuTer ;
output = > retupmoc
output => OMPU
output => op
output => tump
'''