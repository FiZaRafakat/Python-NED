def avg():
    a = int(input("Enter any number for a :---"))
    b = int(input("Enter any number for b :---"))
    c = int(input("Enter any number for c :---"))

    average = (a+b+c)/3
    print(f"The Average number for {a} , {b} and {c} is ",average)

# avg()

def check(num):
    # num = int(input("Enter any number:   "))
    if num%2 == 0:
        print(f"This {num} number is Even Number")
    else : 
        print(f"This {num} number is Odd Number")

# check()

def sum():
    e = int(input("Enter a number to add     "))
    f = int(input("Enter a number to add     "))
    sum = e + f
    print(f"Sum of the number {e} and  {f} is {sum}")

# print("Enter numbers for sum :: ")
# # sum()
# print("Enter a number for Avg :: ")
# # avg()
# print("Enter a number for check it's Even or Odd")
# check()


def Avg(a,b,c):
    # a = int(input("Enter any number for a :---"))
    # b = int(input("Enter any number for b :---"))
    # c = int(input("Enter any number for c :---"))

    average = (a+b+c)/3
    print(f"The Average number for {a} , {b} and {c} is ",average)

# Avg(5,6,7)


def Greet(name):
    print(f'Hello {name} , How is your Python Going ?')
    

# Greet('Fiza')
# sum()
# Greet("Shiza")
# check(9)
# Greet("Nimra")
# avg()


def Sum(a,b):
    return a+ b 


res = Sum(1, 4)
print(res)



def multiple(a, b):
    return a * b

multiply = multiple(9, 5)
print(multiply)


# def multiple_args(*stds):
#     print("The name of stds : ", stds[0])

# multiple_args("Fiza","Shiza","Nimra","Sana")
# multiple_args("Shiza", "Hafsa","Fiza")

