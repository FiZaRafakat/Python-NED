# f = open('abc.txt','r')   #row path

# print(f) # Check the class IOWrapper call
# print(f.read()) # To read a whole file content

'''Encoding => means in our file any data translate into a language for only understand for system / computer '''

# Reading Desired Parts/bytes of a file content 

# first_five = f.read(5)
# firstTen = f.read(10)
# twenty_bytes = f.read(20)
# print(first_five)
# print(firstTen)
# print(twenty_bytes)

# #Reading the line
# Lines = f.readable()
# print(Lines)
# for i in range(3):
#     print(f.readline())

# # Reading Lines automatic
# data = f.readlines()
# print(data[1])

# f.close()

'''Using "with" in handling Files'''
# with open('abc.txt', 'r') as my_file:
#     data = my_file.read()
#     print(data)

# with open('abc.tx','w') as my_file : 
#     my_file.write("Okay , let's div into the code....")    #Writing to a file and erase previous data 

# with open('abc.txt','a') as my_file:
#     my_file.write("Okay , let's div into the code....")

# with open('xyz.txt','r') as my_file:
#     my_file.read()       #this will give an error because file doesnot exist

# with open('xyz.txt','w') as my_file:
#     my_file.write("hello")

# with open('xyz.txt','a') as my_file : 
#     my_file.write("Im fiza")

# with open('edf.txt','x') as my_file : 
#     my_file.create()


'''How to write a code in line by line using loops'''

'''Simple Method'''
# f = open('abc.txt')
# for i in f:
#     print(i)
# f.close()

# with open('abc.txt','r') as f : 
#     for i in f:
#         print(i)

'''Or / Miss'''
# with open('abc.txt','r') as file :
#    data = file.read()
#    for i in data:
#       print(i , end = '')

'''Function'''

# def reading_lines(file_path):
#     with open(file_path,'r') as my_file:
#         data = my_file.read()
#         for i in data:
#             print(i , end = "")

# file_path = input('Enter a file path --- ')
# reading_lines(file_path)
'''Function using readline'''
# def reading_linesBy_readline(file_path):
#     with open(file_path,'r') as my_file:
#         data = my_file.readline()
#         for i in data:
#             print(i , end = "")

# file_path = input('Enter a file path --- ')
# reading_linesBy_readline(file_path)

'''Function using readlines'''
# def reading_linesBy_readlines(file_path):
#     with open(file_path,'r') as my_file:
#         data = my_file.readlines()
#         for i in data:
#             print(i , end = "")

file_path = input('Enter a file path --- ')
# reading_linesBy_readlines(file_path)

'''Function for writing in code'''
# def writing_line(file_path):
#     with open(file_path, 'w') as file : 
#         write = input("What's you want to write ... Write here !! \n")
#         file.writelines(write)
        
# writing_line(file_path)

'''Seek and Call'''
# with open('abc.txt','r') as file : 
#     file.seek(6)    # 6 number bit py chala jaye ga including space (To Seek ka matlab hai k yahan sy start kro) ### Set Python for seeking purpose
#     print(file.tell()) # Tells the pointer poistion
#     print(file.read()) 



'''Write a program to check if your file is opened or closed'''

# def CheckFileStatus(file_path):   
#     File = open(file_path, 'r')
#     if File.close() == True : 
#         print("File Is Close")
#     else : 
#         print("File is Open")

# CheckFileStatus(file_path)


'''Miss Solution
if my_file.closed:
print("closed")
else : 
print("Not Closed")
'''