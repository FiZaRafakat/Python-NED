# Simple Function

def fact(n):
    factorial=1
    if n==0 or n==1:
        print(f"Factorial of {n} is : 1")
    else :
        for i in range(1,n+1):
            factorial *= i
        # print(factorial)
        return factorial

# print(fact(5))

# Recursion function

def factorial(n):
    if n==0 or n==1:
        return 1 
    else :
        return n*factorial(n-1)
# print(factorial(8))

'''Febonacci Sequence:

0+1 = 1  0 = a , 1= b , output = c , This sequnece changes the number , after that now a turns in first 1 , b = returns in output 1 and the output comes in which it\s add a and b ; and the output c = 2
1+1 = 2  
1+2 = 3
2+3 = 5
3+5 = 8 
'''

# Normal function 
n=10 
a= 0 
b = 1
# print(a)
# print(b)
# for i in range(n):
#     c = a + b 
#     a = b 
#     b = c
#     print(c)

# Recursion Function 

# def fib(n):
#     if n<=1:
#         return n
#     else :
#         return fib(n-1) + fib(n-2)
    

# n= int(input("Enter number here ---- "))
# for i in range(n):
#     print(fib(i))   



# sum of nautral numbers

def Sum(n):
    if n == 1:
        return 1
    else:
      return n+Sum(n-1)

# print(Sum(5))


# Find the power of number ::
                                                                                                                                                                                                                                                                                                                                                                                                                             
def power(x, y):
    if y == 0 :
        return 1
    else : 
        return x*power(x,y-1)
    
print()
