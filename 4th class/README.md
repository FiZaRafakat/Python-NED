# 21/Nov/2024

## String Slicing

### Negative Indexing: => also called extended slicing

Use negative indexes to start the slice from the end of the string:

       For Example
       Get the characters:

       From: "o" in "World!" (position -5)

       To, but not included: "d" in "World!" (position -2):

       b = "Hello, World!"
       print(b[-5:-2])



## String Methods /Functions

### <u>Length </u>

To get the length of a string, use the len() function.

        a = "Hello, World!"
        print(len(a)) => 13

    
### <u>Check String</u>

To check if a certain phrase or character is present in a string, we can use the keyword in. 

          i.e text = "Are you free now ?? "
          print("free" in text)  => true



### <u>Check if not</u>

To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.


         i.e text = "Are you free now"
         print("free" not in text) => false



### <u>uppercase</u>

The upper() method returns the string in upper case

         i.e name = "Fiza"
         print(name.upper()) => FIZA


### <u>lowercase</u>

The lower() method returns the string in lower case


        i.e name = "Fiza"
        print(name.lower()) => fiza



### <u>Remove Whitespace</u>

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

The strip() method removes any whitespace from the beginning or the end

        i.e name = "     Fiza   Rafakat        "
        print(name.strip())  => "Fiza   Rafakat"



### <u>Replace the string</u>

The replace() method replaces a string with another string:

        i.e name = "Fiza Rafakat"
        print(name.replace("Fiza","Nazia"))   => Nazia Rafakat



### <u>Split String</u>

The split() method returns a list where the text between the specified separator becomes the list items.

The split() method splits the string into substrings if it finds instances of the separator

        i.e name = "Fiza Rafakat"
        print(name.split(","))



