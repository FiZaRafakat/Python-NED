from abc import ABC, abstractmethod
import math

# 1. Shape Area Calculation
'''Define an abstract class `Shape` with an abstract method `calculate_area()`. Then create subclasses
`Circle` and `Rectangle` that implement this method, calculating the area for each shape.'''
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Example usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle area: {circle.calculate_area()}")
print(f"Rectangle area: {rectangle.calculate_area()}")


# 2. Payment System
'''Create an abstract class `Payment` with an abstract method `process_payment()`. Then create two
subclasses: `CreditCardPayment` and `PayPalPayment`. Implement the `process_payment()` method in
both subclasses.'''

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Example usage:
credit_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

credit_payment.process_payment(100)
paypal_payment.process_payment(200)

# 3. Transportation System
'''Create an abstract class `Transportation` with an abstract method `move()`. Then create subclasses `Car`
and `Bicycle` that implement the `move()` method in different ways.'''

class Transportation(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transportation):
    def move(self):
        print("The car is driving on the road.")

class Bicycle(Transportation):
    def move(self):
        print("The bicycle is being pedaled on the bike path.")

# Example usage:
car = Car()
bicycle = Bicycle()

car.move()
bicycle.move()


# 4. Appliance Interface
'''Define an abstract class `Appliance` with an abstract method `turn_on()`. Create subclasses
`WashingMachine` and `Refrigerator`, each implementing the `turn_on()` method.'''
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("The washing machine is now on and ready to wash clothes.")

class Refrigerator(Appliance):
    def turn_on(self):
        print("The refrigerator is now on and cooling.")

# Example usage:
washing_machine = WashingMachine()
refrigerator = Refrigerator()

washing_machine.turn_on()
refrigerator.turn_on()

# 5. Shape Drawing Interface
'''Define an abstract class `Shape` with an abstract method `draw()`. Then create subclasses `Circle` and
`Square` that each implement `draw()` to display the shape in a console.'''

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

class Square(Shape):
    def draw(self):
        print("Drawing a square.")

# Example usage:
circle = Circle()
square = Square()

circle.draw()
square.draw()

# 6. Employee Task Management
'''Create an abstract class `Employee` with an abstract method `perform_task()`. Then create two
subclasses, `Manager` and `Developer`, and implement `perform_task()` for each subclass with
appropriate tasks.'''

class Employee(ABC):
    @abstractmethod
    def perform_task(self):
        pass

class Manager(Employee):
    def perform_task(self):
        print("Managing team and overseeing project progress.")

class Developer(Employee):
    def perform_task(self):
        print("Writing and testing code.")

# Example usage:
manager = Manager()
developer = Developer()

manager.perform_task()
developer.perform_task()


'''Create a Parent Abstract class with an abstract, 
method that can be implemented by any subclass,
used in calculating the cost of appliance.
Make 2 sub classes for each appliance of the above 
abstract class each having their own instant 
variables for calculating thier total_cost(Price).

Output: 
First Step Display this:
*****Welcome*****
# What do you want to buy?
# 1. Coffee Maker
# 2. Dish Washer
# 3. Microwave

2nd step display this: 
# Pick a Manufacturer:  (User Inputs the appliance)
# 1. Dawlence
# 2. Kenwood
# 3. Westpoint

Final Processed Output:
your selected appliance {appliance name} 
from {company name} costs {cost}'''

class ApplianceCost(ABC):
    @abstractmethod
    def calculate_cost(self):
        pass

class CoffeeMaker(ApplianceCost):
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
        self.price = {"Dawlence": 50, "Kenwood": 60, "Westpoint": 55}

    def calculate_cost(self):
        return self.price[self.manufacturer]

class DishWasher(ApplianceCost):
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
        self.price = {"Dawlence": 300, "Kenwood": 350, "Westpoint": 320}

    def calculate_cost(self):
        return self.price[self.manufacturer]

class Microwave(ApplianceCost):
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
        self.price = {"Dawlence": 100, "Kenwood": 120, "Westpoint": 110}

    def calculate_cost(self):
        return self.price[self.manufacturer]

def main():
    print("*****Welcome*****")
    print("What do you want to buy?")
    print("1. Coffee Maker")
    print("2. Dish Washer")
    print("3. Microwave")

    choice = int(input("Enter your choice (1/2/3): "))

    print("Pick a Manufacturer:")
    print("1. Dawlence")
    print("2. Kenwood")
    print("3. Westpoint")

    manufacturer_choice = int(input("Enter your choice (1/2/3): "))
    manufacturers = {1: "Dawlence", 2: "Kenwood", 3: "Westpoint"}
    manufacturer = manufacturers[manufacturer_choice]

    if choice == 1:
        appliance = CoffeeMaker(manufacturer)
        appliance_name = "Coffee Maker"
    elif choice == 2:
        appliance = DishWasher(manufacturer)
        appliance_name = "Dish Washer"
    elif choice == 3:
        appliance = Microwave(manufacturer)
        appliance_name = "Microwave"
    else:
        print("Invalid choice")
        return

    cost = appliance.calculate_cost()
    print(f"Your selected appliance {appliance_name} from {manufacturer} costs ${cost}")

if __name__ == "__main__":
    main()