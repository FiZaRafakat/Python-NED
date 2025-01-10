# 1. Student Class
'''Define a class `Student` with the attributes `name` (string), `age` (integer), and `grades` (list of floats).
Create a constructor to initialize these attributes and a method `average_grade()` that returns the average
grade of the student.'''

class Student:
    def __init__(self, name: str, age: int, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self) -> float:
        try:
            avg = sum(self.grades) / len(self.grades)
            return print(f"The Average Grade of {self.name} is {avg}")
        except ZeroDivisionError:
            return 0.0
        except TypeError:
            return 0.0

# obj = Student("Fiza", 20, [90, 80])
# obj.average_grade()



# 2. Library Class
'''Define a class `Library` with the following attributes: `book_title` (string), `author` (string),
`published_year` (integer), and `is_available` (boolean). Create methods to check the availability of the
book and borrow it.'''

class Library:
    def __init__(self, book_title: str, author: str, published_year: int, is_available: bool):
        self.book_title = book_title
        self.author = author
        self.published_year = published_year
        self.is_available = is_available

    def availability(self):
        try:
            if self.is_available:
                print("The Book is available, You can borrow it ..")
            else:
                print("The Book is not available....")
        except Exception as e:
            print(f"An error occurred while checking availability: {e}")

    def borrow(self):
        try:
            if self.is_available:
                self.is_available = False
                print(f"You have borrowed: {self.book_title}.")
            else:
                print(f"{self.book_title} is not available for borrowing ....")
        except Exception as e:
            print(f"An error occurred while borrowing the book: {e}")

# obj = Library("Math", "Fiza", 2024, True)
# obj.availability()
# obj.borrow()
# obj.availability()

# obj2 = Library("English", "Maheen", 2025, False)
# obj2.availability()
# obj2.borrow()
# obj2.availability()



# 3. Product Class
'''Define a class `Product` with the attributes `product_name` (string), `price` (float), and `quantity`
(integer). Write methods to display the total value of the product in stock (`price * quantity`).'''

class Product: 
    def __init__(self, product_name: str, price: float, quantity: int):
        self.product_name = product_name
        self.price = price 
        self.quantity = quantity

    def total_value(self):
        try:
            total = self.price * self.quantity
            print(f"The total value of {self.product_name} in stock is: {total}")
        except TypeError as e:
            print(f"An error occurred while calculating the total value: {e}")

# obj3 = Product('Smart Watches', 10000, 5)
# obj3.total_value()

# 4. Car Class
'''Define a class `Car` with attributes `make`, `model`, `year`, and `color`. Create a method
`display_car_info()` that prints out the car details in a readable format.'''

class Car: 
    def __init__(self, make: str, model: str, year: int, color: str):
        self.make = make 
        self.model = model 
        self.year = year 
        self.color = color 

    def display_car_info(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}")

# obj4 = Car('Toyota', 'Corolla', 2020, 'Red')
# obj4.display_car_info()

# 5. Rectangle Class
'''Define a class `Rectangle` with attributes `length` and `width`. Create methods to calculate the perimeter
and area of the rectangle.'''

# Simple
class Rectangle: 
    def __init__(self, length : int , width : int):
        self.length = length 
        self.width = width 
    def parameter(self):
        para = 2 *(self.width + self.length)
        return print(para)
    def area(self):
        area = self.length * self.width 
        return print(area)
    
# obj5 = Rectangle(20,20)
# obj5.area()
# obj5.parameter()

# With try except and getters setters 


# class Rectangle:
#     def __init__(self, length: int, width: int):
#         self.set_length(length)
#         self.set_width(width)

#     def get_length(self) -> int:
#         return self.length

#     def set_length(self, value: int):
#         if value > 0:
#             self.length = value
#         else:
#             raise ValueError("Length must be positive")

#     def get_width(self) -> int:
#         return self.width

#     def set_width(self, value: int):
#         if value > 0:
#             self.width = value
#         else:
#             raise ValueError("Width must be positive")

#     def perimeter(self):
#         try:
#             para = 2 * (self.width + self.length)
#             return print(para)
#         except Exception as e:
#             print(f"An error occurred while calculating the perimeter: {e}")

#     def area(self):
#         try:
#             area = self.length * self.width
#             return print(area)
#         except Exception as e:
#             print(f"An error occurred while calculating the area: {e}")

# obj5 = Rectangle(-2, 20)
# obj5.area()
# obj5.perimeter()



# 6. Student Database Class
'''Define a class `StudentDatabase` that holds a list of students. Each student is represented as a dictionary
with their `name` and `age`. Provide methods to add a student, remove a student, and display all students.'''

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name: str, age: int):
        self.students.append({'name': name, 'age': age})
        print(f"Added student: {name}, Age: {age}")

    def remove_student(self, name: str):
        for student in self.students:
            if student['name'] == name:
                self.students.remove(student)
                print(f"Removed student: {name}")
                break

    def display_students(self):
        if not self.students:
            print("No students in the database.")
        else:
            print("Student Database:")
            for student in self.students:
                print(f"Name: {student['name']}, Age: {student['age']}")


db = StudentDatabase()
db.add_student("Hafsa", 20)
db.add_student("Shiza", 22)
db.display_students()
db.remove_student("Shiza")
db.display_students()
