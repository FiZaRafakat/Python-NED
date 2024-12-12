# 2/Dec/2024

## For Loop

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

Even strings are iterable objects, they contain a sequence of characters

### Break Statement

With the break statement we can stop the loop before it has looped through all the items

           fruits = ["apple", "banana", "cherry"]
               for x in fruits:
                 print(x)
                 if x == "banana":
                 break
                 
                 
                
In this example loop execute apple and then check the condition the condition implement on banana that's not means loop stop there ; loop execute when loop execute 2nd time it first print banana and then check the condition and break the loop  if there we print after condition then it will break after apple and not print banana,  like below :


            fruits = ["apple", "banana", "cherry"]
               for x in fruits:
                 if x == "banana":
                   break
                 print(x)
                 



### Continue Statement

With the continue statement we can stop the current iteration of the loop, and continue with the next


     fruits = ["apple", "banana", "cherry"]
         for x in fruits:
           if x == "banana":
            continue
         print(x)



### Range function 
To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

------ Note that range(6) is not the values of 0 to 6, but the values 0 to 5.  ------


- The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

       for x in range(2, 6):
          print(x)

- The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

           for x in range(2, 30, 3):
            print(x)



### Else in for loop 

The else keyword in a for loop specifies a block of code to be executed when the loop is finished

--------- Note: The else block will NOT be executed if the loop is stopped by a break statement. ----------

      ex :
      Break the loop when x is 3, and see what happens with the else block:

         for x in range(6):
            if x == 3: break
            print(x)
         else:
            print("Finally finished!")


### Nested Loop 

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":


       adj = ["red", "big", "tasty"]
       fruits = ["apple", "banana", "cherry"]

       for x in adj:
          for y in fruits:
          print(x, y)


###  The pass Statement 

for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

         for x in [0, 1, 2]:
          pass


### Loop through a dictionaries 

You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

        for keys  ::

        thisdict =	{
           "brand": "Ford",
           "model": "Mustang",
           "year": 1964
        }
        for x in thisdict:
           print(x)


       for Values::

       for x in thisdict:
         print(thisdict[x])



--- You can also use the keys() and values() methods to get this ---

for complete items in loops we have two methods 

             thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
             }
             for x, y in thisdict.items():
               print(x, y)

             <!-- 2nd Method -->
             for x in thisdict.items():
               print(x) 