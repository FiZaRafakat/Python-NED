"""
Relationships in OOP:
1) Inheritence ("is-a" relationship)
2) Association ("has-a" relationship)

is-a Relationship:
    -used when one class is specialized version of another class
    -modeled using inheritance
    Eg: *A Dog "is-a" Animal ---> dog class inherits from animal class
        *A Car  "is-a" Vehicle ---> car class inherits from vehicle class

has-a Relationship:
    -represents complete + partial ownership (association) b/w classes
    - modelled using aggregation and composition --> association
    - possession of one object by another
    Eg: *A Car "has-a" Engine --> Engine is possessed by a car completely
        *A library "has-a" Books  --> Books are possessed by Library

Association: connection/possession/dependency b/w two classes is association.
    Eg: Person has an address, name etc. But person is not a address etc.
Categories of Association:
    -Aggregation
    -Composition

"""
# Aggregation (partial dependency)
#Student( roll no,name, marks) 
# --> college(Stud(can stand alone), groups, classes)


class Engine:
    def _init_(self, horsepower):
        self.horsepower = horsepower

    def show_info(self):
        print(f"Engine with {self.horsepower} HP.")

class Car:
    def _init_(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Aggregating the Engine object

    def show_details(self):
        print(f"Car Brand: {self.brand}")
        self.engine.show_info()

# Example
engine = Engine(120)
car = Car("Toyota", engine)
car.show_details()  #output: 

# Deleting Car does not affect Engine
del car
engine.show_info()  # Engine still exists

#Composition (complete dependency)
# Person (NAME , ADDRESS, dob(from date and this feature can't stand alone) )
# --> another class has date (day, month, year)
class Room:
    def _init_(self, room_type):
        self.room_type = room_type

    def show_info(self):
        print(f"Room Type: {self.room_type}")

class House:
    def _init_(self, address):
        self.address = address
        self.rooms = []  # List of owned Room objects

    def add_room(self, room_type):
        room = Room(room_type)  # Creating Room objects inside House
        self.rooms.append(room)

    def show_details(self):
        print(f"House Address: {self.address}")
        for room in self.rooms:
            room.show_info()

# Example
house = House("123 Main Street")
house.add_room("Bedroom")
house.add_room("Kitchen")
house.show_details()

# Deleting House destroys its Rooms
del house
# Accessing room would raise an error here as it depends on the House's lifecycle


#Unidirectional Association (one objects interacts with aother, reverse is not true)

class Person:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, model):
        self.model = model
        self.owner = None  # Unidirectional association to Person

    def assign_owner(self, owner):
        self.owner = owner

# Create objects
person = Person("Abeeraa")
car = Car("Tesla Model 3")

# Assigning the owner to the car
car.assign_owner(person)

print(car.owner.name)  # Abeeraa
# The car knows the owner, but the owner does not know about the car


#Bidirectional Association (both objects know about each other. This is achieved by maintaining references in both objects.)

class Person:
    def __init__(self, name):
        self.name = name
        self.cars = []  # Bidirectional association to Car

    def add_car(self, car):
        self.cars.append(car)
        car.owner = self  # Establish bidirectional link

class Car:
    def __init__(self, model):
        self.model = model
        self.owner = None  # Bidirectional association to Person

# Create objects
person = Person("ABC")
car = Car("Tesla")

# Establish bidirectional association
person.add_car(car)

print(car.owner.name)  # abc
print(person.cars[0].model)  # Tesla

#One-to-One (1:1)	One object relates to one other object.	A person and their passport.
#One-to-Many (1:N)	One object relates to multiple other objects.	A teacher and their students.
#Many-to-Many (M:N)	Many objects relate to many other objects.	Students and courses.



#***Functions Decorators***
#Qus: Write a decorator log_function_call that logs the 
# name of the function and it's arguments each time the
# function is called.
# Example Outpt:
# Function Greet is called with 2 arguments ('Alice','Jackson')
# output -> "Hello, Alice Jackson!" 

def log_function_call(func):
    def wrapper(f_name,l_name):
        func(f_name,l_name)
        print(f'Hello, {f_name} {l_name}!')
    return wrapper

@log_function_call
def Greet(f_name,l_name):
    f_name=f_name
    l_name=l_name

Greet("Alice",'Jackson')