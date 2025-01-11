a = 10.00
b = 11.00

"""Logical and Conditional Operators"""
"""==, <, >, <=, >=, !=, and, or, not"""
"""= is assignment operator not 'equals to'
   == is logical operator used for 'equality'"""

"""Keywords: if, else, elif, in, pass"""
a= 10
b = 11
if a == b: 
    pass #written this keyword to edit the code later
elif a>=b:
    pass
elif a<=b:
    pass
else:
    pass

"""TASK 1: Discount Calculator:
Write a program to calculate the total bill 
after applying a discount.
* If the total_amount is greater than 5000, 
apply a 20% discount.
* If it is greater than 2000 but less than or
 equal to 5000, apply a 10% discount.
* Otherwise, no discount is applied.
* Print the final bill amount. """


"""TASK 2: Admission Criteria:
Write a program to decide whether
 a student is eligible for admission.
If the test_score is greater than or 
equal to 80:
    *Check if the interview_score is
      greater than or equal to 70.
    *If both conditions are true, 
    print "Admitted".
    *Otherwise, print "Failed Interview"
Otherwise, print "Failed Test"."""

"""TASK 3: Number Categorization:
Write a program that takes a number as input and categorizes it:
If the number is positive:
    *Check if it's even or odd.
    *If even, print "Positive Even".
    *If odd, print "Positive Odd".
If the number is negative:
    *Check if its absolute value is greater than 10.
    *If greater, print "Large Negative".
    *Otherwise, print "Small Negative".
If the number is zero, print "Zero".
"""
#task 3 solution

num = float(input('Enter any Number: '))
if num >0: #checking first if a number is positive
    #Now checking if it is even positive or odd positive
    if num %2 == 0: 
        print('The number is even positive')  
    else:
        print('The number is neither odd nor even')
elif num <0: #checking if the number is negative

    #Now checking if it is small negative or large negative
    if abs(num) > 10:
        print('The number is large negative')
    else:
        print('The number is small negative')
else:  #This condition is for 'zero'
    print('The number is Zero')

"""TASK 4: 
Grade Classification:
Write a program to determine the grade based on marks.
If marks are greater than or equal to 90:
    *Check if marks are 95 or above, print "A+ Grade".
    *Otherwise, print "A Grade".
If marks are between 80 and 89:
    *Check if marks are 85 or above, print "B+ Grade".
    *Otherwise, print "B Grade".
Otherwise, print "C Grade"."""

marks = float(input('Enter marks: '))
if marks >= 90:
    if marks >=95:
        print('A+ Grade')
    else:
        print('A Grade')
elif 80<= marks <= 89:
    if marks >= 85:
        print('B+ Grade')
    else:
        print('B Grade')
else:
    print('C Grade')

"""
TASK 5:
TRIANGLE TYPE DETERMINATION
Write a program to check the type of triangle based 
on the 
lengths of its sides a, b, and c.
If all three sides are equal:
    Print "Equilateral".
Otherwise:
    If any two sides are equal:
        Print "Isosceles".
    If no sides are equal:
        Check if the sum of any two sides is greater than 
        the third side (to ensure it's a valid triangle).
    If true, print "Scalene".
    Otherwise, print "Invalid Triangle".
"""
#this code has logical bug, resolve it.
a = float(input('Enter 1st side: '))
b = float(input('Enter 2nd side: '))
c = float(input('Enter 3rd side: '))
if a == b == c:
    print('Equilateral') 
else:
    if a == b or b == c or a == c:
        print('Isosceles')
    else:
        if a + b > c and b + a > c and c + a > b:
            print('Scalene')
        else:
            print('Invalid Triangle')
"""
TASK 6:
Temperature Suggestion:
Write a program that suggests clothing based on the temperature.
If temperature is greater than 30:
    Check if it's greater than 40:
    If yes, print "Stay indoors with AC".
    Otherwise, print "Wear light clothes".
If the temperature is between 20 and 30:
    Check if it's closer to 20 (e.g., less than 25):
    If yes, print "Wear a light jacket".
    Otherwise, print "Comfortable weather, dress normally".
Otherwise, print "Wear warm clothes".
"""
"""TASK 7:
Password Strength Checker:
Write a program to check the strength of a password based 
on its length and content.
If the password_length is greater than or equal to 8:
    Check if it contains both letters and numbers:
    If yes, print "Strong Password".
    Otherwise, print "Weak Password".
If the password length is less than 8:
    If yes, print "Moderate Password".
Otherwise, print "Very Weak Password"."""

"""TASK 8: Write a program that displays -Babar Azam 
on output, if score >30,
Shoaib Akhtar, 
if 20<score<30, and Shahid Afridi if 10<score >20.

TASK 9: Write a program that takes password from user as input. 

Validate the password on the following criteria:
Password length between 7 to 15 characters which contain at least one 
numeric digit and a special character is acceptable"""

"""Task 10: Wish 'good morning', 
'good noon', 'good after noon', 
'good evening',
 'good night'to the user
when a user enters the time 
in hours:minutes:seconds """
'02:00:01'
