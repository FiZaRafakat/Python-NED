# Task 

L = [5,6,8,9,2,1]
# Converti it into :
# [1,2,5,6,8,9]
L.sort()
print(L)

# [1,2,6,8,9]
L.pop(2)
print(L)

# [1,2,6,8,9,10]
L.append(10)
print(L)

# [10,9,8,6,2,1]
print(L[::-1])

# [8]
print(L[3])

#Task :: Produce a code to get first , second best scores from the list 

L = [86,86,85,85,85,83,23,45,84,1,2,0]
L.sort()
print(max(L))


# Task :: Write a program to perform operations on the given list to generate following outputs :
List = ['this','is','simple','computer','programming','using','python']
List1 = List.copy()
List2 = List.copy()
# print ['this','is','computer','programming']
List.pop(2)
print(List[0:4])

# print ['this','is','simple']
List1 = ['this','is','simple','computer','programming','using','python']
print(List1[0:3])

# print ['this','is','programming','using','python']
List1.pop(2)
List1.remove('computer') 
print(List1)

# print ['programming','using','python']
print(List1[2:])

# print ['is','this','computer','programming']
L2 = [List2[1],List2[0],List2[3],List2[4]]
print(L2)

# Task :: From given list : gadgets =["Mobile","Laptop",100,"Camera",310.28,"Speakers",27.00,"Televsion",1000,"Laptop Case","Camera Lens"]

# a) Create separate lists of string and number
gadgets =["Mobile","Laptop",100,"Camera",310.28,"Speakers",27.00,"Televsion",1000,"Laptop Case","Camera Lens"]
Number = [gadgets.pop(2),gadgets.pop(4), gadgets.pop(6), gadgets.pop(5)]
print(Number)