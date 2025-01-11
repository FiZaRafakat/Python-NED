class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        return f"name:{self.name} age:{self.age}"
class Teacher(Person):
    def __init__(self, name, age , subject):
        super().__init__(name, age)
        self.subject=subject
    def display_info(self):
        Person_info=super().display_info()
        return f"{Person_info} , subject:{self.subject}"
class Sports:
    def __init__(self,sport_name):
        self.sportname=sport_name
    def conct_sport(self):
        return f"{self.sportname}" 
class Sportsteacher(Teacher,Sports):
    def __init__(self, name, age, subject,sport_name):
        Teacher.__init__(self,name, age, subject)                    
        Sports.__init__(self,sport_name)  
    def display_info(self):
        Teache_info=Teacher.display_info(self)                      
        sport_info=f"spots:{self.sportname}"
        return f"{Teache_info},{sport_info}"  
class Principal(Teacher):
    def __init__(self, name, age, subject ,school_name):
        super().__init__(name, age, subject)  
        self.school_name=school_name
    def display_info(self):
        return super().display_info()
person=Person("Ali",30)
teacher=Teacher("ahmed", 35,"maths")
sport=Sportsteacher("alice",40,"science","basketball")
p=Principal("sara",50,"science","abc")
print(person.display_info())
print(teacher.display_info())
print(sport.display_info())
print(p.display_info())

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

