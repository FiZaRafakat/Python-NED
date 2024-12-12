def addition(a,b):
    return a+ b
def subtarction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def power(a,b):
    return a ** b

print("Select Operation number : ")
print("1) Addition ")
print("2) Subtraction ")
print("3) Multiplication ")
print("4) Division ")
print("5) Power ")


while True : 
    choice = input("Enter you choice number 1 , 2, etc...")
    if choice in ('1','2','3','4','5','6','7'):
        try : 
             num1 = int(input("Enter first number:"))
             num2 = int(input("Enter second number:"))
        except ValueError : 
            print("Enter Valid number")
            continue


    if choice == "1":
        print(num1, "+" , num2 , "=" , addition(num1,num2) )
    elif choice == "2":
        print(num1,"-",num2 ,"=",subtarction(num1,num2))
    elif choice == "3":
        print(num1,"*",num2 , "=",multiplication(num1,num2))
    elif choice == "4":
        print(num1, "/",num2 ,"=" , division(num1, num2))
    elif choice == "5":
        print(num1, "**", num2 , "=", power(num1|num2))
        
    next_calculation = input("Let's do another calculations : yes/no----  ")
    if next_calculation == "no":
        break