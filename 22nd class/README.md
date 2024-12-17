# Object Oriented Programming(OOPs):
  
  => Procedural Programming (Datatypes, loops , functions, filesHandling) 

   |

 ## Programming

   |

  => Object Oriented Programming(Advanced Python , Implement Procedural Programming)

### Elements in OOP

1 )  Classes 
- attributes (variable within a class)
- method (function within a class )(method k andr function implement hova hota hai,)
- written with specific name 
- always start class with small alphabet , and their name start with capital alphabet  
- instance (variable/object in which class is called...)
- class is also called a blue-print


      class School:
           school_name = 'ABC School' #school name is attribute
           def method(self):  #self is a parameter for a function and we always use this , either it necessary for a function to pass argument or not 
          #method of a class
               print('The name of School is : ' , self.school_name.lower())
      <!-- How to call a OOP -->
      obj = School()  #obj => instance of a class/Obj
      <!-- How to call a function from class -->
      obj.method()


