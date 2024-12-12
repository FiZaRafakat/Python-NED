# Find the sum of natural numbers using loops 
List = [1,2,3,4,5]

def Sum(List):
    sum = 0 
    for i in List:
        sum += i 
        i = 1
    return sum 

print(Sum(List))

# Find the pirme number taking input from users

input_user = int(input("Enter Number here!!"))

def checkPrime(input_user):
    if input_user <= 1:
       print("Not a prime number")
       return
    for i in range(2, input_user):
         if input_user % i == 0 :
          print("Not a prime number")
          return
    print("Prime Number")


checkPrime(input_user)


# Q#:: Write the program to largest and smallest numbers in the list 
List = [1,2,4,5,7,8,9,10,23,25]

def Max(List):
    largest_num = List[0]
    smallest_num = List[-1]
    for i in List:
        if i > largest_num :
            largest_num = i 
        if i < smallest_num :
            smallest_num = i
    print("Smallest number",smallest_num)
    print("Largest number",largest_num)

Max(List)

# Write a program to reverse and sort the list

L = [1,4,5,8,2,3,7]

