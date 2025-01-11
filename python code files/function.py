# # # #understanding basic structure of functions

# # def my_sum (a,b):
# #     'This function calculates sum'  #this is a docstring
# #     addition = a + b 
# #     return addition

# # print(my_sum.__doc__)
# # print(my_sum(1 , 9))



# # def my_func():
# #     print('Hello')

# # # print() #new line \n

# # my_func()

# # print(len())

# #understanding default parameters
# def my_function(a = 5):
#     print(a)

# num1 = 7
# my_function(num1) #it will work bydefault a = 5

# #understanding types of arguments
# """1) Positional Arguments"""
# """2) Keyword Arguements"""
# def circle (r, a = 3.142):
#     circumference = 2 * a * r
#     return circumference

# print(circle(2))


# #Arbitrary Positional Argument
# def kids_name(*kids): #kids might be some list (iterative object)
#     print('The last name of kid is', kids[len(kids)-1])

# # a = ['abc', 'xyz', 'jkl']
# kids_name('abc', 'xyz', 'jkl')

# understanding arbitrary keyword arguments
def my_names (**f_l_names):
    print('My first and Last Name is',f_l_names["fname"], f_l_names["lname"])

my_names(lname = 'abc', fname = 'xyz')


