'''Q : Write a python program to read first n lines of the file, implement the "read function" created earlier (no hardcoding)....'''

file_path = input('Enter a file path --- \n')

def ReadFirstLines(file_path,n):
    with open(file_path,'r') as my_file:
        lines = my_file.readlines()
        print(lines[:n])

# n = int(input("Write lines for read \n")) 

# ReadFirstLines(file_path,n)

'''Write a program to read last n lines of the file'''

def ReadLastLines(file_path,n):
    with open(file_path,'r') as my_file:
        lines = my_file.readlines()
        print(lines[n:])

n = int(input("Write lines for read \n")) 

ReadLastLines(file_path,n)

'''
Q :: Write a python program to count total number of lines in a file
Q :: Write a python program to print longest line of the file
Q :: Write a python program to print longest word of the file 
'''