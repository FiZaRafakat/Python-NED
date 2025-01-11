# n = int(input('ENTER A NUMBER: '))  #value error canbe raised
# for i in range(1 , 11):
#     print(f'{n} x {i} = {n * i}')


"""Exception Handling: Process of responding to 
unwanted/unexpected events/errors when a computer program
runs. 
When error occurs python interpreter stops
the execution. until it is handled by a programmer
"""
# try:
#     n = int(input('ENTER A NUMBER: '))
#     for i in range(1 , 11):
#         print(f'{n} x {i} = {n * i}')

# except:
#     print('Enter Valid Value')


# try:
#     n = int(input('ENTER A NUMBER: '))
#     for i in range(1 , 11):
#         print(f'{n} x {i} = {n * i}')

# except ValueError:
#     print('Enter Valid Value')

# try:
#     n = int(input('ENTER A NUMBER: '))
#     for i in range(1 , 11):
#         print(f'{n} x {i} = {n * i}')

# except ValueError as e:
#     print(e)

# amount = 10000
# if(amount > 2999)
# print("You are eligible to purchase Dsa Self Paced")


#exception handling is only done when the code is syntatically correct
# try: 
#     amount = 10000
#     if(amount > 2999)
#         print("You are eligible to purchase Dsa Self Paced")

# except:
#     print('correct the syntax')

# understanding finally keyword
# try : 
#     n= int(input('Enter an index: '))
#     l = [ 1 , 3, 5 , 6]
#     print(l[n])
# except:
#     print('enter valid index')

# finally: 
#     print('Finally!!!')


def a(l,n):
    try : 
        print(l[n])   

    except:
        print('enter valid index')

    print('Finally!!!')

n= int(input('Enter an index: '))
l = [ 1 , 3, 5 , 6]
a(l, n)
# print('Hello, executed.')


##Raising Custom Errors using raise keyword


"""
Qs: 1 Write  a program that handles the 
zero division error.
Hint: Take input from user any 2 numbers, 
operate them and handle the error


Qs:2 Handle file not found error

Qs:3 Write a program that takes input from user
and handles following:
1) The number shouldn't be neg
2) The error should be handled. 

Qs 4: Write a program that performs integer division. 
Handle all possible errors that may occur.

Qs: 5 Implement else clause with try and except. 
Hint: else executes if no exceptions are raised

Qs: 6 Write a program that
takes list as an input from user.
and calculates its sum.
Handle exceptions in this case.

"""

