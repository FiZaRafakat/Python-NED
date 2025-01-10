# 1. Bank Account Class
'''Define a class `BankAccount` with private attributes `account_number` and `balance`. Provide public
methods `deposit()` and `withdraw()` to handle deposits and withdrawals. Ensure that the `withdraw()`
method checks that the withdrawal amount is not greater than the balance.'''

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.__balance}")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            print("Withdrawal amount must be positive")

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance must be non-negative")

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

# bank = BankAccount("2187934", 10000)
# bank.withdraw(15000)
# bank.withdraw(3000)
# bank.deposit(2000)
# print(f"Account Number: {bank.get_account_number()}")
# bank.set_account_number("4793483")
# print(f"Account Number: {bank.get_account_number()}")
# print(f"Balance: {bank.get_balance()}")
# bank.set_balance(20000)
# print(f"Balance: {bank.get_balance()}")


# 2. Employee Class with Salary
'''Define a class `Employee` with a private attribute `salary`. Write a method `get_salary()` that allows
access to the salary, but only if the employee's salary is greater than 0.'''

class Employee:
    def __init__(self, salary):
        self.__salary = salary
        
    def get_salary(self):
        if self.__salary > 0:
            return self.__salary
        else:
            return "Salary must be greater than 0"


# employee = Employee(5000)
# print(employee.get_salary()) 

# employee = Employee(-1000)
# print(employee.get_salary())


# 3. Account Holder Class
'''Create a class `AccountHolder` with private attributes `name` and `account_balance`. Provide public
methods `deposit(amount)` and `withdraw(amount)` to handle money transactions, while ensuring that
negative values are not accepted.'''


class AccountHolder:
    def __init__(self, name , accountBalance):
        self.__name = name 
        self.__accountBalance = accountBalance
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__accountBalance:
            self.__accountBalance -= amount
            print(f"Withdraw {amount} , Net Balance {self.__accountBalance}")
        elif amount < 0 : 
            print(f"Amount must be greater than 0 ")
        else : 
            print("Invalid Amount")
    def deposit(self, amount):
        if amount > 0 : 
            self.__accountBalance += amount
            print(f"Deposited Amount {amount} , Net Balance {self.__accountBalance}")
        else : 
            print("The amount must be greater than 0")
    #Getter and Setter   
    def getName(self):
        print(self.__name)
    def getAccountBalance(self):
        print(self.__accountBalance)
    
    def setName(self, name ):
        self.__name = name
        return
    def setAccountBalance(self, accountBalance):
        if accountBalance >=0: 
            self.__accountBalance = accountBalance
            return
        else : 
            print("Number must be greater than 0")

 
# person = AccountHolder("Shiza",2000)
# person.deposit(2000)
# person.withdraw(8000)
# person.withdraw(1000)
# person.getAccountBalance()
# person.setAccountBalance(-20)
# person.setAccountBalance(20000)
# person.getAccountBalance()
# person.getName()
# person.setName("Hafsa") 
# person.getName()   

# 4. Product Stock Class
'''Define a class `ProductStock` with private attributes `product_name` and `quantity_in_stock`. Write a
public method `check_availability()` to check if a product is in stock and return a message accordingly.'''


class ProductStock:
    def __init__(self, product_name, quantity_in_stock):
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def check_availability(self):
        if self.__quantity_in_stock > 0:
            return f"{self.__product_name} is in stock"
        else:
            return f"{self.__product_name} is out of stock"

    def get_product_name(self):
        return self.__product_name

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_quantity_in_stock(self, quantity_in_stock):
        if quantity_in_stock >= 0:
            self.__quantity_in_stock = quantity_in_stock
        else:
            print("Quantity must be non-negative")

# product = ProductStock("Laptop", 10)
# print(product.check_availability())
# product.set_quantity_in_stock(0)
# print(product.check_availability())


# 5. Gradebook Class
'''Create a `Gradebook` class with private attributes `student_name` and `grades` (a list). Provide a method
`add_grade()` to add grades, and a method `average_grade()` that returns the average of all grades.'''

class Gradebook:
    def __init__(self, student_name):
        self.__student_name = student_name
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Added grade: {grade}")
        else:
            print("Grade must be between 0 and 100")

    def average_grade(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        else:
            return "No grades available"

    def get_student_name(self):
        return self.__student_name

    def get_grades(self):
        return self.__grades

# gradebook = Gradebook("John Doe")
# gradebook.add_grade(85)
# gradebook.add_grade(90)
# gradebook.add_grade(78)
# print(f"Average Grade: {gradebook.average_grade()}")
# print(f"Grades: {gradebook.get_grades()}")


# 6. Movie Class
'''Create a class `Movie` with a private attribute `rating` and a public method `get_rating()` that allows
access to the rating only if it is above a certain threshold (e.g., 3).'''

class Movie:
    def __init__(self, rating):
        self.__rating = rating

    def get_rating(self):
        if self.__rating > 3:
            return self.__rating
        else:
            return "Rating is below the threshold"

# movie = Movie(4)
# print(movie.get_rating())

# movie = Movie(2)
# print(movie.get_rating())