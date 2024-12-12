f = open('abc.txt','r')

# print(f) # Check the class
# print(f.read()) # For whole Code

# # Reading Desired Parts/bytes of a file content 
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

# Reading Lines automatic
data = f.readlines()
print(data[1])

f.close()

