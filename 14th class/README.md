# 5/Dec/2024

# Function

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

#### How to create a function

         def function():
                "Hello"

#### How to call a function

           function()

## Arguments 

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

       for Ex::
       def greet(name):
          print("Hello ",name)
       greet("Fiza")
       greet("Hafsa")

### Parameter vs Arguments

The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

      # Function definition with parameters
        def add(x, y):  # x and y are parameters
          return x + y

      # Calling the function with arguments
       result = add(5, 3)  # 5 and 3 are arguments

      # Display the result
      print(f"Result of adding 5 and 3 is: {result}")


---

### Multiple Arguments / Arbitrary Arguments

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

         ex : 
         def Greet(*name):
            print("Hello")

        Greet("Fiza","Shiza","Hafsa")