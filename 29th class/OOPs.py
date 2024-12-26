'''
## EXPLANANTION OF PYTHON INHERITANCE

Parent Class:
This is the base class from which other class inherits.
It contains attributes and methods that the child class can reuse.

Child Class:
This is the derived class that inherits from the  parent class.
The syntax for inheritance is class ChildClass(ParentClass).
Thge child class automatically gets all attributes and methods of the parent class unless overridden.

1) parent class ko child class mei laxmi inherit krna hai ....
2) jo bhi required attribute or methods hai evnthough it's relate from parent or child , hm usy child mei hi likhy gy , or child sy hi acces kr skty hain ....

## OVERRIDING CONCEPT

Mthod overriding is a concept in object-oriented programming
where a child class provides it's own version of a method that already exist in the parent class...
When you override a method , the child class's method replaces the parent class's method for object of the child class...

Super Keyword in action for calling parent methods explicitly in child class
'''

# class Parent:
#     def sound_of_animal(self):
#         print("Generic")
# class Child(Parent):
#     def sound_of_animal(self):
#         super().sound_of_animal()
#         print("Bark")

# child = Child()
# child.sound_of_animal()



# Without Inheritance

# class Shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.142 * self.radius ** 2

# s = Shape(3,4)
# print(s.area())

# c = Circle(3)
# print(c.area())


# With Inheritance 

# class Shape:
#     def __init__(self , x,y):
#         self.x = x 
#         self.y = y
#     def area(self):
#         return self.x * self.y
# class Circle(Shape):
#     def __init__(self,x,y,radius):
#         super().__init__(x,y)
#         self.radius = radius
#     def area(self):
#         return (self.radius**2) * 3.142

# circle = Circle(5,3,3)
# print(circle.area())

# shape = Shape(3,4)
# shape.area()


'''
HOSPITAL MANAGEMENT SYSTEM

Create a patient class with attributes :
- name 
- age 
- disease
- is_admitted(default to false) do not pass this as an argument 

The class should include methods :
admit() - admit the patient by setting is_admitted to True
discharge() - discharge the patient by setting is_admitted to False 
display_info() -display patient details

Create a Hospital class with attributes :
patient (list of pateint objects).Hint self.patient = []

The class should include methods:
add_patient() -> Add a new patient to the hospital 
list_patients() -> Display information for all patients
search_patients() -> Search for a patient by name 

**** Advance : ****
Add a doctor class, and assign patients to specific directors. 
Track patient histories and appointment schedules.....
'''

class Patient:
    def __init__(self, name , age , disease):
        self.name = name 
        self.age = age 
        self.disease = disease
        self.is_admitted = False
    def admit(self):
        self.is_admitted = True 
    def discharge(self):
        self.is_admitted = False
    def display_info(self):
        print(f"Name Of Patient : {self.name}  \nAge Of Patient : {self.age}  \nDisease Of Patient : {self.disease}  \nAdmitted : {self.is_admitted}")
class Hospital(Patient):
    pateint1 = patient.slpit[0]
    patient = [pateint1 ,]
    def __init__(self, name , age , disease):
        super().__init__(name , age , disease)
    def add_patient(self):
        pateint_input = input("Enter Patient name , age and disease (separeted by comma)")
        patient.append(pateint_input.split[0])
        print("Pateint is added Succesfully....")
    def list_patients(self):
        print(patient)
    def search_patients(self):
        search_patient = input("Search for a patient:")
        if search_patient is found in  patient :
            print(patient)
        else : 
            print("Not Found")

obj = Hospital("Shiza", 30, "Fever")

while True : 
    print("Enter into Our Hospital::")
    print("Enter what you want to do ?  \n1 ) Add Patient \n2) View Patient \n3) Search Patient 4)Exit")   
    Choice = input("Enter your choice here : \n")
    if Choice == 1 :
        obj.add_patient()
    elif Choice == 2 :
        obj.list_patients()
    elif Choice == 3:
        obj.search_patients()
    elif Choice == 4 : 
        break 
    else : 
        print("Try Again")
        





# patient = Patient("Shiza" , 20 , "Fever")
# patient.display_info()
# print("*" * 15)
# patient.admit()
# patient.display_info()
# print("*" * 15)



# Practice Questions

'''
Question 1: Shape Inheritance
Classes: Shape, Rectangle, and Circle.

Shape class:

The Shape class should be an abstract base class (ABC).
It should define an abstract method area() to calculate the area of a shape.
Rectangle class:

Inherit from Shape class.
The Rectangle class should have attributes width and height.
Implement the area() method to return the area of the rectangle (i.e., width * height).
Circle class:

Inherit from Shape class.
The Circle class should have an attribute radius.
Implement the area() method to return the area of the circle (i.e., π * radius²).
Task:

Create one Rectangle and one Circle object.
Call the area() method on both objects and print the results.
'''

# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, height , width):
#         self.height = height
#         self.width = width 
#     def area(self):
#         return self.height * self.width

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius 
#     def area(self):
#         return (self.radius **2 ) * 3.142

# circle = Circle(4)
# rectangle = Rectangle(5,10) 

# print(circle.area())
# print(rectangle.area())

'''
Question 2: Bank Account Inheritance
Classes: BankAccount, CheckingAccount, and SavingsAccount

BankAccount class:

The BankAccount class should have attributes for the account holder’s name and balance.
It should have methods to deposit and withdraw money.
CheckingAccount class:

Inherit from the BankAccount class.
Add an attribute for overdraft_limit.
Override the withdraw() method to consider the overdraft limit.
SavingsAccount class:

Inherit from the BankAccount class.
Add an attribute for interest_rate.
Implement a method apply_interest() to add interest to the balance.
Task:

Create instances of CheckingAccount and SavingsAccount.
Perform deposits and withdrawals on both accounts.
Print the final balance for both accounts after applying interest (if applicable).

'''














