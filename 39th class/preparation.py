'''Practice Questions::'''

'''1) Write a python program that counts how many times a particular number appears in a list of integers.'''

# List = [1,3,4,5,3,6,7,3,2,3,4,2]

# def counts(n):
#     count = 0
#     for i in List: 
#         if i == n :
#            count += 1 
#     return print(count)
       
        
# n = int(input("Enter a number to find!!"))
# counts(n)

'''2) Given a list containing both integers and strings , Write a python program that removes duplicate elements from the list and prints the result.'''

# List2 = ['Fiza',1,5,6,'Shiza',5,6,'Shiza']

# def duplicate():
#     list3 = []
#     for i in List2: 
#         if i not in list3 : 
#            list3.append(i)
#     return print(list3)

# duplicate()


'''3) Write a python program that creates a list of numbers , both integers and floats. Use list comprehensive to create a new list that contains only the numbers greater than 10 , Calculate the sum of the numbers in the new list ....'''

'''check it's number and integer'''

# def List(userInput):
#     list5 = []
#     for i in userInput:
#         if type(i) == int or type(i) == float:
#             list5.append(i)
#     return print("The List of Integer and float " ,list5)

    
# List1 = [1,2,3,4,6,7,1.0, 2.8,'Fiza']
# List(List1)

'''For Sum of 10 , and integer and float checking '''

# def List(userInput):
#     list5 = []
#     for i in userInput:
#         if type(i) == int or type(i) == float:
#             if i >= 10 :
#                 list5.append(i)
#     return print("The List of numbers greater than 10 " ,list5)

    
# List1 = [1,2,3,4,6,7,1.0,20, 20 , 50 , 70 , 20, 2.8]
# List(List1)

'''For Sum of numbers in a list'''

# def List(userInput):
#     list5 = []
#     sum = 0
#     for i in userInput:
#         if type(i) == int or type(i) == float:
#             if i >= 10 :
#                 list5.append(i)
#                 sum += i 
#     print("The List of numbers greater than 10 " ,list5)                
#     print("The sum of numbers greater than 10 " ,sum)            
#     return 
    
# List1 = [1,2,3,4,6,7,1.0,20,'Fiza', 20,"Shiza" , 20 , 20 , 20,10, 2.8]
# List(List1)

'''4) Write a python program 'rotate_string(text,n) that rotates the string by 'n' positions.
For Example : If the input is : 'abcdef' and n = 2 , the output should be 'cdefab'. '''

# def rotateString(text,n):
#     txt1 = text[:n]
#     txt2 = text[n:]
#     return print(txt2 + txt1)
     
# text = input("Enter a text ").strip()
# n = int(input("Enter a number"))

# rotateString(text,n)

'''5) Write a python function 'merge_dicts' that merge two dictionaries . If There are common keys , add the values together.
Example : 
Input : {'a': 1 , "b" : 2},{"b":3, "c" : 4}
Output : {"a" : 1 , "b" : 5, "c":4}
'''


# def merge_dicts(dict1, dict2):
#     merge_dic = dict1.copy()
#     for key,value in dict2.items:
#         if key in merge_dic:
#            merge_dic[key] += value 
#         else : 
#             merge_dic[key] = value
#     return merge_dic

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# result = merge_dicts(dict1, dict2)

# print(result)

'''
sheet Question 

Palindrome Check
'''


# OOP's
'''
MRO , relationship , (theory)(3 Coding)
is a => inheritence (Dog is a animal)
has a => association (company has an employee)

Getter setters is compulsory
multiple inheritance,
abstraction and interface(Employee task management)(miss waly )
public private property () 
Encapsulation (pdf)
important ____ ) library management System
'''
#Basic 
'''
Exceptional handling
Palindrome Check
Qno: 4
str* args (keyword Arguments)
Working with files
'''

