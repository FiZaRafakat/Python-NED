import math
'''create another class library with following attributes:
book(list of book object)
the class should have :
add_Book() => Add book to the library
list_Book() => Print all details of the book  
search_book() => Search for a book by title '''

# class Library:
#     def __init__(self,books):
#       self.books = books
#     def add_book(self,new_book):
#         self.books.append(new_book)
#     def search_book(self, book_to_search):
#         if book_to_search in self.books:
#             print("Found")
#         else : 
#             print("Not Found")
#     def display_info(self):
#         print(self.books)
    
# books = ["The Kite Runner","And The Mountains Echoed","A Thousand Splendid Suns","Welcome Home","Nectar Of Pain","Mind Platter","Him"]

# lib1 = Library(books)
# print("Welcome To Library !!")
# user_input = input("Do you want to add ?\n Yes/No \n").lower()
# if user_input == "yes":
#     lib1.add_book(input("Enter a Book to add ?\n"))
# userInput = input("Do you want to search ?\n Yes/No \n").lower()
# if userInput == "yes":
#     lib1.search_book(input("Enter a book Name : \n").title())

# lib1.display_info()

'''
Create a calculator with classes and objects
Code should have following functions():
add()
sub()
divide()
mutliply()
power()
squareRoot()
'''

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Add(self):
        add = self.a + self.b
        return add
    def Sub(self):
        sub = self.a - self.b
        return sub
    def Mutliply(self):
        mutliply = self.a * self.b
        return mutliply
    def Divide(self):
        divide = self.a / self.b
        return divide
    def Power(self):
        power = self.a ** self.b
        return power
    def SquareRoot(self):
        sRoot = self.a**0.5 ,self.b**0.5
        return sRoot
    def Sin(self):
        angle_of_a = math.radians(self.a)
        angle_of_b = math.radians(self.b)
        print(f"The Sin Of {self.a} : {math.sin(angle_of_a)}")
        print(f"The Sin Of {self.b} : {math.sin(angle_of_b)}")
    def Cos(self):
        angle_of_a = math.radians(self.a)
        angle_of_b = math.radians(self.b)
        print(f"The Cos Of {self.a} : {math.cos(angle_of_a)}")
        print(f"The Cos Of {self.b} : {math.cos(angle_of_b)}")
    def Log(self):
        a_log = math.log10(self.a)
        print(f"The Log of {self.a} is {a_log}")
        b_log = math.log10(self.b)
        print(f"The Log of {self.b} is {b_log} ")

print("Welcome to my Calculator !! ")
user_input = input("Type the number from following you want in this calculator:\n 1) Addition ,2) Subtraction , 3) Multliply , 4) Divide ,5) Power , 6) Square Root 7) Cos 8) Sin 9) Log \n").lower()
a = int(input("Enter first number :\n"))
b = int(input("Enter second number :\n"))
my_calculator = Calculator(a, b)
if user_input == "addition":
    print(my_calculator.Add())
elif user_input == "subtraction":
    print(my_calculator.Sub())
elif user_input == "multiply":
    print(my_calculator.Mutliply())
elif user_input == "divide":
    print(my_calculator.Divide())
elif user_input == "power":
    print(my_calculator.Power())
elif user_input == "square root":
    print(my_calculator.SquareRoot())
elif user_input == "sin":
    my_calculator.Sin()
elif user_input == "cos":
    my_calculator.Cos()
elif user_input == "log":
    my_calculator.Log()
else : 
    print("You should be Type Operation from the above......... 😐 ")