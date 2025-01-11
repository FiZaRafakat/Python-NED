#creating a tuple
tup = (1 , 2, 3, 4, 5, 6, 8, 10) 
print(tup)
print(type(tup))  #datatype: tuple 
print(len(tup))   #length : 05

#accessing elements of tuple
print(tup[0]) #output : 1
print(tup[1]) #output : 2
print(tup[2]) #output : 3
print(tup[3]) #output ; 4
print(tup[4]) #output : 5
print(tup[-5]) #output : 4
#understanding slicing
print(tup[1:5])  #output : 2 3 4  5
print(tup[-7:-3])  #output : 2 3 4 5
print(tup[len(tup)-7:len(tup)-3]) #output: 2 3 4 5
print(tup[::-1])  #reverses the tuple
print(tup[5:0:-1])  #output 6 5 4 3 2
print(tup[-3:-8:-1])  #output 6 5 4 3 2 

#understanding creating tuple in different ways
l = [1]
print(type(l))
tup1 = (1, ) #create a single value tuple
tup2 = 1, 2, 3, 4 #creating tuple without round brackets
print(type(tup2))
tup3 = 1 , #create the single value tuple
tup4 = ()  #created empty tuple
print(type(tup4))
tup5 = ('KHI', [1 , 2])
print(type(tup5))
print(tup5)
print(len(tup5))
print(tup5[0]) #output : KHI
print(tup5[1]) #output : [1 , 2]
print(tup5[1][0]) #output 1
print(tup5[1][1]) #output 2

#creating a tuple using tuple constructor
my_tuple = tuple(('KHI', 'LHR', 'ISL'))
print(type(my_tuple)) 

#understanding type casting in tuples
my_tuple1 = 1 , 2 , 3, 4
# print(int(my_tuple1)) #typecasting to int not possible
type_casted = str(my_tuple1) #typecasting into str
print(type(type_casted)) #possible

# type_casted1 = complex(type_casted) #not possible
# print(type_casted1)
typecasted1 = list(my_tuple1) #typecasting to list
print(type(typecasted1))
print(typecasted1)

#checking if 11 is in tuple

if 11 in tup:
    print('Yes it is in tuple')
else: 
    print('not in tuple') 

# if 11 not in tup:
#     print('No, it is not')
# else: 
#     print ('yes')

#consecutively printing values in tup
# for i in tup:
#     print(i, end = " ") #to have output in single line

#there are 2 methods to insert/update element in tuple
#1. is to concatenate/ add tuple to a tuple
my_tup1 = (1 , 2, 3)
my_tup2 = ('a', 'b')
print(my_tup1 + my_tup2)

#2. is to use .append indirectly
#first convert your tuple into list
x = list(my_tup1) # [ 1 , 2, 3]
y = x.append(10)
print(x)
print(tuple(x))

#unpacking tuple
t = ('apple', 'banana', 'orange')
(fruit1, fruit2, fruit3) = t
(fruit_first , *fruit_second) = t
print(fruit1) #output apple
print(fruit2) #output banana
print(fruit3) #output orange
print(fruit_first)  #output apple
print(fruit_second) #output banana orange


