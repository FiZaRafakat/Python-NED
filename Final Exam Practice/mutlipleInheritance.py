# 1. Artist and Writer Classes
'''Define a class `Artist` with the attribute `art_style` and a method `create_art()`. Define another class
`Writer` with the attribute `writing_style` and a method `write()`. Then define a class `CreativePerson` that
inherits from both `Artist` and `Writer` and has a method `display_info()` that displays both art and writing
styles.'''

class Artist: 
    def __init__(self,art_style):
        self.art_style = art_style 
    def create_art(self):
        print(f"Creating art in {self.art_style} style .")

class Writer:
    def __init__(self,writing_style):
        self.writing_style = writing_style
    def write(self):
        print(f"Writing in {self.writing_style} Style.")
        
class CreativePerson(Artist,Writer):
    def __init__(self, art_style,writing_style):
        Artist.__init__(self,art_style)
        Writer.__init__(self,writing_style)
    def display_info(self):
        print(f"Art Style: {self.art_style}")
        print(f"Writing Style: {self.writing_style}")

# Or 
        
class Artist:
    def __init__(self, art_style):
        self.art_style = art_style
    def create_art(self):
        return f"Creating art in {self.art_style} style."
    def display_info(self):
        return f"Art Style: {self.art_style}"

class Writer:
    def __init__(self, writing_style):
        self.writing_style = writing_style
    def write(self):
        return f"Writing in {self.writing_style} style."
    def display_info(self):
        return f"Writing Style: {self.writing_style}"

class CreativePerson(Artist, Writer):
    def __init__(self, art_style, writing_style):
        Artist.__init__(self, art_style)
        Writer.__init__(self, writing_style)
    def display_info(self):
        artist_info = Artist.display_info(self)
        writer_info = Writer.display_info(self)
        return f"{artist_info}, {writer_info}"
        
# person = CreativePerson(art_style="Abstract", writing_style="Poetry")
# person.create_art()          
# person.write()               
# person.display_info()   

# 2. Student and Sportsman Classes
'''Define a class `Student` with attributes `name` and `age`, and a method `study()`. Define another class
`Sportsman` with an attribute `sport` and a method `play_sport()`. Then define a class `StudentAthlete`
that inherits from both `Student` and `Sportsman` and implements a method `display_info()` to show all
details.'''

class Student:
    def __init__(self, name , age ):
        self.name = name 
        self.age = age 
    def study(self):
        print(f"Student {self.name} is studying.")

class Sportsman:
    def __init__(self,sport):
        self.sport = sport 
    def play_sport(self):
        print(f"Here you can play {self.sport}")
        
class StudentAthlete(Student , Sportsman):
    def __init__(self,name , age , sport):
        Student.__init__(self,name , age)
        Sportsman.__init__(self, sport)
    def display_info(self):
        print(f"{self.name} in the age of {self.age} win a prize for best playing {self.sport} Sport.")
        
# StdAth = StudentAthlete("Fiza",20,"Cricket")
# StdAth.study()
# StdAth.play_sport()
# StdAth.display_info()



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self):
        return f"Student {self.name} is studying."
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Sportsman:
    def __init__(self, sport):
        self.sport = sport
    def play_sport(self):
        return f"Playing {self.sport}"
    def display_info(self):
        return f"Sport: {self.sport}"

class StudentAthlete(Student, Sportsman):
    def __init__(self, name, age, sport):
        Student.__init__(self, name, age)
        Sportsman.__init__(self, sport)
    def display_info(self):
        student_info = Student.display_info(self)
        sportsman_info = Sportsman.display_info(self)
        return f"{student_info}, {sportsman_info}"

# 3. Person and Vehicle Classes
'''Define a class `Person` with attributes `name` and `age`. Define another class `Vehicle` with an attribute
`model`. Create a class `Driver` that inherits from both `Person` and `Vehicle` and displays a message that
includes the driver&#39;s name, age, and the vehicle model.'''

class Person:
    def __init__(self, name , age ):
        self.name = name
        self.age = age 
    
class Vehicle: 
    def __init__(self, model):
        self.model = model
        
class Driver(Person , Vehicle):
    def __init__(self,name , age , model):
        Person.__init__(self, name, age )
        Vehicle.__init__(self, model)
    def display_info(self):
        print(f"The driver {self.name} who is {self.age} years old drives a {self.model}.")

# driver = Driver("Hassan", 18 , "Toyota")
# driver.display_info()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Vehicle:
    def __init__(self, model):
        self.model = model
    def display_info(self):
        return f"Model: {self.model}"

class Driver(Person, Vehicle):
    def __init__(self, name, age, model):
        Person.__init__(self, name, age)
        Vehicle.__init__(self, model)
    def display_info(self):
        person_info = Person.display_info(self)
        vehicle_info = Vehicle.display_info(self)
        return f"{person_info}, {vehicle_info}"
    
# person = Person("Ali", 30)
# print(person.display_info())


# 4. Teacher and Researcher Classes
'''Define a class `Teacher` with the attribute `subject`. Define another class `Researcher` with the attribute
`research_area`. Create a class `Professor` that inherits from both `Teacher` and `Researcher` and prints
out the details of both the subject and research area.'''
class Teacher:
    def __init__(self, subject):
        self.subject = subject

class Researcher:
    def __init__(self, research_area):
        self.research_area = research_area

class Professor(Teacher, Researcher):
    def __init__(self, subject, research_area):
        Teacher.__init__(self, subject)
        Researcher.__init__(self, research_area)
    def display_info(self):
        print(f"Subject: {self.subject}")
        print(f"Research Area: {self.research_area}")

# professor = Professor("Mathematics", "Algebra")
# professor.display_info()


class Teacher:
    def __init__(self, subject):
        self.subject = subject
    def display_info(self):
        return f"Subject: {self.subject}"

class Researcher:
    def __init__(self, research_area):
        self.research_area = research_area
    def display_info(self):
        return f"Research Area: {self.research_area}"

class Professor(Teacher, Researcher):
    def __init__(self, subject, research_area):
        Teacher.__init__(self, subject)
        Researcher.__init__(self, research_area)
    def display_info(self):
        teacher_info = Teacher.display_info(self)
        researcher_info = Researcher.display_info(self)
        return f"{teacher_info}, {researcher_info}"
    
    
# teacher = Teacher("Ahmed", 35)
# print(teacher.display_info())
    

# 5. Chef and Server Classes
'''Define a class `Chef` with the attribute `specialty`. Define another class `Server` with an attribute
`restaurant_name`. Create a class `RestaurantEmployee` that inherits from both `Chef` and `Server` and
displays the employee&#39;s specialty and restaurant name.'''
class Chef:
    def __init__(self, specialty):
        self.specialty = specialty

class Server:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name

class RestaurantEmployee(Chef, Server):
    def __init__(self, specialty, restaurant_name):
        Chef.__init__(self, specialty)
        Server.__init__(self, restaurant_name)
    def display_info(self):
        print(f"Specialty: {self.specialty}")
        print(f"Restaurant Name: {self.restaurant_name}")

# employee = RestaurantEmployee("Italian Cuisine", "La Piazza")
# employee.display_info()


class Chef:
    def __init__(self, specialty):
        self.specialty = specialty
    def display_info(self):
        return f"Specialty: {self.specialty}"

class Server:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
    def display_info(self):
        return f"Restaurant Name: {self.restaurant_name}"

class RestaurantEmployee(Chef, Server):
    def __init__(self, specialty, restaurant_name):
        Chef.__init__(self, specialty)
        Server.__init__(self, restaurant_name)
    def display_info(self):
        chef_info = Chef.display_info(self)
        server_info = Server.display_info(self)
        return f"{chef_info}, {server_info}"
    
# sport = StudentAthlete("Alice", 40, "Basketball")
# print(sport.display_info())

# 6. Product and Category Classes
'''Define a class `Product` with attributes `product_name` and `price`. Define another class `Category` with
the attribute `category_name`. Then create a class `ProductCategory` that inherits from both `Product` and
`Category`, and displays the product name along with its category.'''

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

class Category:
    def __init__(self, category_name):
        self.category_name = category_name

class ProductCategory(Product, Category):
    def __init__(self, product_name, price, category_name):
        Product.__init__(self, product_name, price)
        Category.__init__(self, category_name)
    def display_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price}")
        print(f"Category: {self.category_name}")

# product_category = ProductCategory("Laptop", 1200, "Electronics")
# product_category.display_info()

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
    def display_info(self):
        return f"Product Name: {self.product_name}, Price: ${self.price}"

class Category:
    def __init__(self, category_name):
        self.category_name = category_name
    def display_info(self):
        return f"Category: {self.category_name}"

class ProductCategory(Product, Category):
    def __init__(self, product_name, price, category_name):
        Product.__init__(self, product_name, price)
        Category.__init__(self, category_name)
    def display_info(self):
        product_info = Product.display_info(self)
        category_info = Category.display_info(self)
        return f"{product_info}, {category_info}"

# p = Professor("Sara", "Science")
# print(p.display_info())



'''
Q:Desgin a school management system with the following requirements:
-create a person class with basic attribute like name and age,inherit it in a Teacher class with additional attributes.
-create a sports class with methods (conduct_sport) for sports activities and combine it with teacher class to form a sportsTeacher class.
-create a principal class that inherits from teacher extends it with administrative methods 
methods:display_info , manage_school
-create a sports class with methods (conduct_sport) for sports activities and combine it with teacher class to form a sportsTeacher class.
-create a principal class that inherits from teacher extends it with administrative methods 
methods:display_info , manage_school
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def display_info(self):
        person_info = super().display_info()
        return f"{person_info}, Subject: {self.subject}"

class Sports:
    def conduct_sport(self):
        return "Conducting sports activities."

class SportsTeacher(Teacher, Sports):
    def __init__(self, name, age, subject):
        Teacher.__init__(self, name, age, subject)
    def display_info(self):
        teacher_info = Teacher.display_info(self)
        return f"{teacher_info}, {self.conduct_sport()}"

class Principal(Teacher):
    def __init__(self, name, age, subject):
        super().__init__(name, age, subject)
    def manage_school(self):
        return "Managing the school."
    def display_info(self):
        teacher_info = super().display_info()
        return f"{teacher_info}, {self.manage_school()}"

# Example usage:
# principal = Principal("John", 50, "Mathematics")
# print(principal.display_info())

# sports_teacher = SportsTeacher("Jane", 35, "Physical Education")
# print(sports_teacher.display_info())


'''Simple Inheritance

6. Fruit and Apple Classes

Define a class `Fruit` with an attribute `name` and a method `taste()`. Then define a subclass `Apple` that
inherits from `Fruit` and overrides the `taste()` method to print a specific message about the apple's taste.'''

class Fruit:
    def __init__(self, name):
        self.name = name
    def taste(self):
        return "This fruit tastes good."

class Apple(Fruit):
    def __init__(self, name):
        super().__init__(name)
    def taste(self):
        return f"The {self.name} tastes sweet and crisp."

# Example usage:
apple = Apple("Apple")
print(apple.taste())