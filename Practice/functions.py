'''# Find the sum of natural numbers using loops '''
List = [1,2,3,4,5]

# def Sum(List):
#     sum = 0 
#     for i in List:
#         sum = i + sum
#     return sum 

# print(Sum(List))

'''# Find the pirme number taking input from users'''

# input_user = int(input("Enter Number here!!"))

# def checkPrime(input_user):
#     if input_user <= 1:
#        print("Not a prime number")
#        return
#     for i in range(2, input_user):
#          if input_user % i == 0 :
#           print("Not a prime number")
#           return
#     print("Prime Number")


# checkPrime(input_user)


'''# Q#:: Write the program to largest and smallest numbers in the list 
# List = [1,2,4,5,7,8,9,10,23,25]'''

# def Max(List):
#     largest_num = List[0]
#     smallest_num = List[-1]
#     for i in List:
#         if i > largest_num :
#             largest_num = i 
#         if i < smallest_num :
#             smallest_num = i
#     print("Smallest number",smallest_num)
#     print("Largest number",largest_num)

# Max(List)

'''# Write a program to reverse and sort the list'''

# def reverse_list(lst):
#     # Base case: If the list is empty or has one element, return it
#     if len(lst) <= 1:
#         return lst
#     else:
#         # Recursively reverse the rest of the list and add the first element at the end
#         return reverse_list(lst[1:]) + [lst[0]]

# def sort_list(lst):
#     # Base case: If the list has one or zero elements, it's already sorted
#     if len(lst) <= 1:
#         return lst
#     else:
#         # Find the minimum element and place it at the front, then sort the rest of the list
#         min_val = min(lst)
#         lst.remove(min_val)
#         return [min_val] + sort_list(lst)

# # Test the functions
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# # Reverse the list
# reversed_list = reverse_list(my_list)
# print(f"Reversed List: {reversed_list}")

# # Sort the list
# sorted_list = sort_list(my_list)
# print(f"Sorted List: {sorted_list}")

'''Write code to remove the duplicate from List '''

# def remove_duplicates(lst, result=None):
#     if result is None:
#         result = []  # Initialize as an empty list on the first call
#     if len(lst) == 0:
#         return result
#     if lst[0] not in result:
#         result.append(lst[0])
#     return remove_duplicates(lst[1:], result)

# List = [1,2,4,5,6,3,4,2,6,3]
# print(remove_duplicates(List))

'''Write a program to recursively give terms of Fibonacci series'''
# f(n) = f(n-1)+ f(n-2)
n=8
# def fib(n):
#     if n == 0 :
#         return 0 
#     elif n == 1:
#        return 1
#     else : 
#         c = fib(n-2) + fib(n-1)
#         return c

# for i in range(n):
#     print(fib(i))
    
    
'''Check if its palindrome or not '''
# def is_palindrome(lst):
#     # Iterate through the first half of the list
#     for i in range(len(lst) // 2):  # We only need to check till half of the list
#         if lst[i] != lst[-(i + 1)]:  # Compare the element at i with the element from the end
#             return False  # If any pair doesn't match, return False
    
#     return True  # If all pairs match, return True

# List = [2,4,3,4,2]
# print(is_palindrome(List))

'''Sum Of Prime Number '''

# def is_prime (n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0 :
#             return False
#     return True

# def Sum_Prime(count=0 , current = 2, sum_prime = 0):
#     if count == 20 :
#         print(f"Sum of 20 numbers {sum_prime}")
#         return sum_prime
#     if is_prime(current):
#         sum_prime = sum_prime + current
#         count = count+1
#     current = current + 1
#     return Sum_Prime(count,current,sum_prime)
    
# print(Sum_Prime())
    
    
'''Count for Vowels '''
# def count_vowels(string):
#     # Base case: If the string is empty, return 0
#     if len(string) == 0:
#         return 0
#     else:
#         # Check if the first character is a vowel
#         if string[0].lower() in 'aeiou':
#             # If it is a vowel, count 1 and proceed with the rest of the string
#             return 1 + count_vowels(string[1:])
#         else:
#             # If it is not a vowel, just proceed with the rest of the string
#             return count_vowels(string[1:])

# # Test the function
# text = "hello world"
# result = count_vowels(text)
# print(f"Number of vowels in '{text}': {result}")


'''Find the power of number ::'''
                                                                                                                                                                                                                                                                                                                                                                                                                             
# def power(x, y):
#     if y == 0 :
#         return 1
#     else : 
#         return x*power(x,y-1)
    
# print(power(2,3))