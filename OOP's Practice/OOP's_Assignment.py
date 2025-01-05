'''1)
Write code to develop a class called Circle which contains the following public attributes and methods. Decide
appropriate attributes/parameters and return types.
• Attributes: radius and color
• Methods:
o setRadius(r): sets radius value to r
o getRadius(): returns radius value
o setColor(c): sets color name to c
o getColor(): returns color name
o getCircumference(): returns circumference of the circle
o getArea(): returns area of the circle
Instantiate necessary objects to test the functionality of this class.
'''
# class Circle:
#     def __init__(self,radius,color):
#         self.radius = radius
#         self.color = color
#     def setRadius(self,r):
#         self.radius = r
#     def getRadius(self):
#         return self.radius
#     def setColor(self,c):
#         self.color = c
#     def getColor(self):
#         return self.color
#     def getCircumference(self):
#         return 2*3.14*self.radius
#     def getArea(self):
#         return 3.14*self.radius**2
    
# c1 = Circle(5,'Red')
# print(c1.getRadius())
# print(c1.getColor())
# print(c1.getCircumference())
# print(c1.getArea())
# c1.setRadius(10)
# c1.setColor('Blue')
# print(c1.getRadius())
# print(c1.getColor())
# print(c1.getCircumference())
# print(c1.getArea())

'''2)
Write code to develop a class BankAccount that supports the following methods:
• withdraw(): takes an amount as input from user and withdraws it from the balance
• deposit(): takes an amount as input from user and adds it to the balance
• balance(): returns the balance on the account
Make all the methods public and decide appropriate parameter(s) and return types wherever needed. Also create
appropriate public attributes. Instantiate necessary objects to test the functionality of this class.
'''
# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def withdraw(self,amount):
#         self.balance -= amount
#     def deposit(self,amount):
#         self.balance += amount
#     def get_balance(self):
#         return self.balance

# B = BankAccount(10000)
# print("You have a 10,000 balance in your account. What do you want to do? \n1. Withdraw \n2. Deposit")
# choice = int(input("Enter choice: "))

# if choice == 1:
#     amount = float(input("Enter amount to withdraw: "))
#     if B.get_balance() == 0:
#         print("You have insufficient balance to withdraw")
#     if amount <= B.get_balance() : 
#         B.withdraw(amount)
#         print(f"New balance: {B.get_balance()}")
#     elif amount > B.get_balance():
#         print("You have insufficient balance to withdraw") 
# elif choice == 2:
#     amount = float(input("Enter amount to deposit: "))
#     if amount < 0:
#         print("Invalid amount")
#     elif amount >= 0:
#         B.deposit(amount)
#         print(f"New balance: {B.get_balance()}") 
# else: 
#     print("Invalid choice")

'''3)
Repeat problem 2, making all attributes private. Make appropriate changes in the code wherever needed.
'''

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def withdraw(self,amount):
#         self.__balance -= amount
#     def deposit(self,amount):
#         self.__balance += amount
#     def get_balance(self):
#         return self.__balance

# B = BankAccount(10000) 
# print("You have a 10,000 balance in your account. What do you want to do? \n1. Withdraw \n2. Deposit")
# choice = int(input("Enter choice: "))

# if choice == 1:
#     amount = float(input("Enter amount to withdraw: "))
#     if B.get_balance() == 0:
#         print("You have insufficient balance to withdraw")
#     if amount <= B.get_balance() : 
#         B.withdraw(amount)
#         print(f"New balance: {B.get_balance()}")
#     elif amount > B.get_balance():
#         print("You have insufficient balance to withdraw")
# elif choice == 2:
#     amount = float(input("Enter amount to deposit: "))
#     if amount < 0:
#         print("Invalid amount")
#     elif amount >= 0:
#         B.deposit(amount)
#         print(f"New balance: {B.get_balance()}")
# else:
#     print("Invalid choice")

'''4)
Write code to implement class Worker that supports two private attributes hoursWorked and wageRate, and
the following public methods:
• setHoursWorked(h): sets hoursWorked to h
• changeRate(r): changes the worker’s pay rate to the new hourly rate r
• pay(): returns the pay as product of hoursWorked and wageRate
Instantiate necessary objects to test the functionality of this class.
'''

# class Worker:
#     def __init__(self, hoursWorked , wageRate):
#         self.__hoursWorked = hoursWorked
#         self.__wageRate = wageRate
#     def setHoursWorked(self,h):
#         self.__hoursWorked = h
#     def changeRate(self,r):
#         self.__wageRate = r
#     def pay(self):
#         return self.__hoursWorked * self.__wageRate
    
# F = Worker(40,10000)
# print(F.pay())
# F.setHoursWorked(50)
# print(F.pay())
# F.changeRate(15000)
# print(F.pay())

'''5)
Repeat problem 4, adding constructor to initialize the attributes. Also set attributes’ default values.
'''

# class Worker:
#     def __init__(self, hoursWorked = 40 , wageRate = 10000):
#        self.__hoursWorked = hoursWorked
#        self.__wageRate = wageRate
#     def setHoursWorked(self,h): 
#         self.__hoursWorked = h
#     def changeRate(self,r):
#         self.__wageRate = r
#     def pay(self):
#         return self.__hoursWorked * self.__wageRate
    
# F = Worker()
# print(F.pay())
# F.setHoursWorked(50)
# print(F.pay())
# F.changeRate(15000)
# print(F.pay())


'''6)
Write code to develop a class named Vehicles having three private attributes noOfWheels, color and modelNo;
define related constructor and public getter/setter methods. Use appropriate types for all attributes, method
parameters and return values wherever needed. Instantiate necessary objects to test the functionality of this class.
'''  
# class Vehicles:
#     def __init__(self,noOfWheels : int,color : str,modelNo : str):
#         self.__noOfWheels = noOfWheels 
#         self.__color = color
#         self.__modelNo = modelNo
        
#     @property
#     def noOfWheels(self) -> int:
#         return self.__noOfWheels
    
#     @noOfWheels.setter
#     def noOfWheels(self,noOfWheels : int):
#         self.__noOfWheels = noOfWheels
        
#     @property
#     def color(self) -> str:
#         return self.__color
    
#     @color.setter
#     def color(self,color : str):
#         self.__color = color
      
#     @property  
#     def modelNo(self):
#         return self.__modelNo
    
#     @modelNo.setter
#     def modelNo(self,modelNo):
#         self.__modelNo = modelNo
        
# V = Vehicles(4,'Black','12345')
# print(V.noOfWheels)
# print(V.color)
# print(V.modelNo)
# V.noOfWheels = 2
# V.color = 'Red'
# V.modelNo = '54321'
# print(V.noOfWheels)
# print(V.color)
# print(V.modelNo)


'''7)
Write code to develop a class Engine having private attributes engineNo and dateOfManufacture, along
with appropriate constructor and public getter/setter methods. Decide appropriate types for all attributes, method
parameters and return values for this new class.
'''
# class Engine:
#     def __init__(self,engineNo : str , dateOfManufacture : str):
#         self.__engineNo = engineNo
#         self.__dateOfManufacture = dateOfManufacture
    
#     @property
#     def engineNo(self) -> str:
#         return self.__engineNo
    
#     @engineNo.setter
#     def engineNo(self,engineNo : str):
#         self.__engineNo = engineNo
    
#     @property
#     def dateOfManufacture(self) -> str:
#         return self.__dateOfManufacture
    
#     @dateOfManufacture.setter
#     def dateOfManufacture(self,dateOfManufacture : str):
#         self.__dateOfManufacture = dateOfManufacture

    
# E = Engine("ENG12345", "2023-01-01")
# print(E.engineNo)
# print(E.dateOfManufacture)
# E.engineNo = "ENG54321"
# E.dateOfManufacture = "2023-12-31"
# print(E.engineNo)
# print(E.dateOfManufacture)

'''8)
Write code to create a class that imitates part of the functionality of the basic data type int. Call the class Int (note
different capitalization). The only data in this class is an int variable. Include methods to initialize an Int to any
value (0 being default), to change it anytime and to display it, and to add two Int values. Write a program that
exercises this class by creating one uninitialized and two initialized Int values, adding the two initialized values and
placing the response in the uninitialized value, and then displaying this result.
'''

# class Integer:
#     def __init__(self,value = 0):
#         self.value = value
#     def display(self):
#         return self.value
#     def set_value(self, value):
#         self.value = value
#     def add(self, a, b):
#         self.value = a.value + b.value
    
# I1 = Integer()
# I2 = Integer(5)
# I3 = Integer(10)
# print(I1.display())
# print(I2.display())
# result = I1.add(I2,I3)
# print(result)

'''9)
Imagine a tollbooth at a bridge. Cars passing by the booth are expected to pay a Rs. 50 toll. Mostly they do, but
sometimes a car goes by without paying. The tollbooth keeps track of the number of cars that have gone by, and of
the total amount of money collected. Write code to model this tollbooth with a class called TollBooth having two
attributes: to hold the total number of cars, and to hold the total amount of money collected. A constructor initializes
both of these to 0. A method called payingCar() increments the car total and adds Rs. 50 to the cash total.
Another method, called nopayCar(), increments the car total but adds nothing to the cash total. Finally, a method
function called display() displays the two totals. Include a program to test this class. This program should allow
the user to select one key to count a paying car, and another to count a nonpaying car; and any other key to print out
the total cars and total cash and then exit.
'''

# class TollBooth:
#     def __init__(self):
#         self.total_cars = 0
#         self.total_cash = 0
#     def payingCar(self):
#         self.total_cars += 1
#         self.total_cash += 50
#     def nopayCar(self):
#         self.total_cars += 1
#     def display(self):
#         print(f"Total cars: {self.total_cars}")
#         print(f"Total cash: {self.total_cash}")
        
# T = TollBooth()
# while True:
#     print("Press 1 for paying car")
#     print("Press 2 for non paying car")
#     print("Type display to display total cars and total cash")
#     print("*"*20)
#     choice = input("Enter choice: ").strip()
#     if choice == '1':
#         T.payingCar()
#     elif choice == '2':
#         T.nopayCar()
#     else:
#         T.display()
#         break

'''10)
Write code to create a class called Time that has separate member data for hours, minutes, and seconds. Make
constructor to initialize these attributes, with 0 being the default value. Add a method to display time in 11:59:59
format. Add another method addTime which takes one argument of Time type and add this time to the current time
of the self object. Instantiate two objects t1 and t2 to any arbitrary values, display both the objects, add t2 to t1
and display the result.
'''

# class Time:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#     def display_time(self):
#         print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")
#     def addTime(self, t):
#         self.hours += t.hours
#         self.minutes += t.minutes
#         self.seconds += t.seconds    
#         if self.seconds >= 60:
#             self.minutes += self.seconds // 60
#             self.seconds = self.seconds % 60
#         if self.minutes >= 60:
#             self.hours += self.minutes // 60
#             self.minutes = self.minutes % 60
#         if self.hours >= 24:
#             self.hours = self.hours % 24            
#         return self.hours,self.minutes,self.seconds
   
# t1 = Time(10,20,30)
# t2 = Time(5,10,20)
# t3 = Time()
# t1.display_time()
# t2.display_time()
# t1.addTime(t2)
# t1.display_time()
# t3.display_time()

'''11)
In ocean navigation, locations are measured in degrees and minutes of latitude and longitude. Thus if you’re lying off
the mouth of Papeete Harbor in Tahiti, your location is 149 degrees 34.8 minutes west longitude, and 17 degrees 31.5
minutes south latitude. This is written as 149°34.8’ W, 17°31.5’ S. There are 60 minutes in a degree (an older system
also divided a minute into 60 seconds, but the modern approach is to use decimal minutes instead). Longitude is
measured from 0 to 180 degrees, east or west from Greenwich, England, to the international dateline in the Pacific.
Latitude is measured from 0 to 90 degrees, north or south from the equator to the poles. Write code to create a class
Angle that includes three member variables: int for degrees, a float for minutes, and a char for the direction letter
(N, S, E, or W). This class can hold either a latitude variable or a longitude variable. Write one method to obtain an
angle value (in degrees and minutes) and a direction from the user, and a second to display the angle value in
179°59.9’ E format. Also write a three-argument constructor. Write a main program that displays an angle initialized
with the constructor, and then, within a loop, allows the user to input any angle value, and then displays the value.
You can use the hex character constant ‘\xF8’, which usually prints a degree (°) symbol.
'''

# class Angle:
#     def __init__(self, degrees, minutes, direction):
#         self.degrees = degrees
#         self.minutes = minutes
#         self.direction = direction

#     def get_angle(self):
#         self.degrees = int(input("Enter degrees: "))
#         self.minutes = float(input("Enter minutes: "))
#         self.direction = input("Enter direction (N, S, E, W): ").upper()

#     def display_angle(self):
#         print(f"{self.degrees}\u00B0{self.minutes}’ {self.direction}")

# if __name__ == "__main__":
#     A = Angle(149, 34.8, 'W')
#     A.display_angle()
    
#     while True:
#         A.get_angle()
#         A.display_angle()
#         cont = input("Do you want to enter another angle? (y/n): ").lower()
#         if cont != 'y':
#             break
        
'''12)
Write code to create a class Tracker that includes a data member that holds a serial number for each object created
from the class. That is, the first object created will be numbered 1, the second 2, and so on. For this, create a class
attribute named count; then, as each object is created, its constructor can examine this count member variable to
determine the appropriate serial number for the new object. Add a method that permits an object to report its own
serial number. Then write a main program that creates three objects and queries each one about its serial number.
They should respond I am object number 2, and so on.
'''

# class Tracker:
#     count = 0
#     def __init__(self):
#         Tracker.count += 1
#         self.serial_number = Tracker.count
#     def get_serial_number(self):
#         return f"I am object number {self.serial_number}"
    
# T1 = Tracker()
# T2 = Tracker()
# T3 = Tracker()
# print(T1.get_serial_number())
# print(T2.get_serial_number())
# print(T3.get_serial_number())

'''13)
Create a class called Ship that incorporates a ship’s number and location. Use the approach of problem 12 to
number each ship object as it is created. Use two variables of the Angle class from problem 11 to represent the
ship’s latitude and longitude. A method of the Ship class should get a position from the user and store it in the
object; another should report the serial number and position. Write a main program that creates three ships, asks the
user to input the position of each, and then displays each ship’s number and position.
'''

# class Ship:
#     count = 0
#     def __init__(self):
#         Ship.count += 1
#         self.serial_number = Ship.count
#         self.latitude = Angle(0,0.0,'N')
#         self.longitude = Angle(0,0.0,'E')
#     def get_position(self):
#         print(f"Enter position for ship {self.serial_number}")
#         print("-"*40)
#         print(f"Enter latitude:")
#         self.latitude.get_angle()
#         print("*"*40)
#         print(f"Enter longitude:")
#         self.longitude.get_angle()
#         print("*"*40)
#     def report_position(self):
#         print("_"*40)
#         print(f"Ship {self.serial_number} is at:")
#         print(f"Latitude:")
#         self.latitude.display_angle()
#         print(f"Longitude:")
#         self.longitude.display_angle()
        
# S1 = Ship()
# S2 = Ship()
# S1.get_position()
# S2.get_position()  
# S1.report_position()
# S2.report_position()
