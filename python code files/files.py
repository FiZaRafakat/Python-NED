f = open('H:/Python_Dev_2024/abcd.txt', 'r')
print(f)  #checking the class IOWrapper call
print(f.read()) #to read a whole file content

#reading desired parts/bytes of a file cotnent
print(f.read(8))
ten_bytes = f.read(10)
twenty_bytes = f.read(20)

# # print(first_eight_bytes)
# # print(ten_bytes)
# # print(twenty_bytes)

#reading the content line by line
print(f.readline())
print(f.readline())
print(f.readline())

for i in range(3):
    print(f.readline())

#reading lines automatically
data = f.readlines()
print(data[1])
# print(data)
f.close()

#using 'with' in handling files 
with open('H:/Python_Dev_2024/abcd.txt', 'r') as my_file:
    data = my_file.read() #read
    print(data)

with open('H:/Python_Dev_2024/abcd.txt', 'w') as my_file:
   my_file.write('Good Morning') #writing to a file (erases all existing data)

with open('H:/Python_Dev_2024/abcd.txt', 'a') as my_file:
    my_file.write('Good Eveneing') #appending to an existing content

with open('xyz.txt', 'r') as my_file:
    print(my_file.read()) #File not found error

with open('xyz.txt', 'w') as my_file:
    my_file.write('abc') #Creates a new file now/ no error

with open('xyz.txt', 'a') as my_file:
    my_file.write('abc') #Creates a new file/ no error

# with open('xyz.txt', 'x') as my_file:
#     my_file.write() #creates a new file

#read a file using loop
with open('H:/Python_Dev_2024/abcd.txt', 'r') as my_file:
    data = my_file.read()
    for i in data:
        print(i, end = "")

def reading_lines (file_path):
    with open(file_path, 'r') as my_file:
        data = my_file.read()
        for i in data:
            print(i , end = "")

file_path = input('Enter file path: ')
reading_lines(file_path)

#function of writelines()
#using f.readline()
#using f.readlines()

#seek and tell
with open('H:/Python_Dev_2024/abcd.txt', 'r') as my_file:
    my_file.seek(6)  #sets python for reading purpose
    print(my_file.tell())  #tells the current pointer position
    print(my_file.read())


if my_file.closed:
    print('Closed')
else:
    print('Not closed')


"""   PRACTICE QUESTIONS 
Q: Write a python program to read first n lines of the file, 
implement the "read function" created earlier (no hardcoding)
Q: write a program to read last n lines of the file.
Q: Write a python program to count total number of lines in a file
Q; Write a python program to print longest line of the file
Q: Write a python program to print longest word of the file

"""



