#UNDERSTANDING CONSTRUCTORS IN OOPs

"""Why to use constructors? Instead of directly defining attributes
 within a class.
Constructors are used within a class definition before desrcibing
any method.
They are written with def __init__ dunder (double underscore) method. 
They are used for:
1) Tracking multiple user defined attributes (inputs/variables).
2) Number of attributes can be given to a class instance,
by not directly changing the class code. This saves us from hardcoding, 
and modifying classes directly. (Encapsulation)"""

class Car:
    def __init__(self, brand, name, \
                 price, color, engine):  #user defined constructor
        self.brand = brand
        self.name = name
        self.price = price
        self.color = color
        self.engine = engine
    def show_details (self):
        print(\
            f'Brand: {self.brand}\nName: {self.name}\nPrice: {self.price}\nColor: {self.color}\nEngine: {self.engine}'\
                )

obj1 = Car('toyota', 'altis', '400000', 'white', '1200cc')
obj1.show_details()

#changing only one attribute
obj1.name = 'Yaris'
obj1.show_details()

#default constructor
class Person:
    def __init__(self): #default constructor: takes no parameter except self
        print('i am a constructor')

object = Person()  #the constructor will be automatically invoked here 


"""Practice Exercise:"""

class Library_System: 
    def __init__(self, title, author, is_borrowed, is_returned):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.is_returned = is_returned
    def borrow_book (self, borrow):
        if borrow == 'yes':
            self.is_borrowed = True
        else:
            self.is_borrowed = False
    def return_book (self, return_):
        if return_ == 'yes':
            self.is_returned = True
        else:
            self.is_returned = False
    def show_details(self):
        print(f'TITLE: {self.title}\nAUTHOR: {self.author}\nBORROW STATUS: {self.is_borrowed}\nRETURN STAUS {self.is_returned}')

lib = Library_System('And The Mountains Echoed', 'Khaled Hosseini', False , False)

lib.borrow_book(input('You want to borrow? ').lower())
lib.return_book(input('You want to return ').lower())
lib.show_details()