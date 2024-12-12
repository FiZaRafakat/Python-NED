# 20/nov/2024

## Slicing String

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

### Slicing from start:

By leaving out the start index, the range will start at the first character

         i.e : print(name[:3])  /
         print(name[0:3])


### Slicing to End 

By leaving out the end index, the range will go to the end


        i.e : print(name[0:len(name)]) /
        print(:5)


## Escape Sequence Characters

Sequence of characters after backslash "/" 

Escape Sequence Characters comprise of more than one character but represent one character when used within the string 

          \n => newline
          \t => For tab space
          \; single quotes
          \\ backslash

