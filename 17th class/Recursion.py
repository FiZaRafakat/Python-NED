L = [2,4,6,8]

# Write a program to solve it using recursion and simple function by finding dum of series 

# # Using Loops
# sum = 0 
# for i in L :
#     sum = i + sum 
# print(sum)

# # Using Function

# def sumOfList(L):
#     sum = 0 
#     for i in L :
#         sum = i + sum
#     return sum

# print(sumOfList(L))

# Using Recursion 

'''List ==> If Empty ?
        |
         ===> else not Empty ? '''

# def Sum_of_list(L):
#     if len(L) == 0 :  #empty
#         return 0
#     else : 
#         return L[0] + Sum_of_list(L[1:])
# print(Sum_of_list(L))


# W3 Example

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     # print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# print(tri_recursion(6))


# def factorial(n):
#     return n * factorial(n - 1)

# # Ye code crash ho sakta hai, kyunki base case nahi hai!
# print(factorial(5))


'''Write a program to recursively give terms of Fibonacci series'''
# f(n) = f(n-1)+ f(n-2)
n=8
def fib(n):
    if n == 0 :
        return 0 
    elif n == 1:
       return 1
    else : 
        c = fib(n-2) + fib(n-1)
        return c

for i in range(n):
    print(fib(i))



'''Reverse a string
Reverse string from hello to "elloh"'''
# def reverse(String):
#     if len(String) == 0:
#       return String
#     else : 
#       result =  String[0] + reverse(String[1:])
      
       
# String = "Hello"

# print(reverse(String))