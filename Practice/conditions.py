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

# password = input("Enter a Password")
# if len(password) >= 8:
#     if password.isalnum() and not password.isdigit() and not password.isalpha():
#         print("Strong Password")
#     else:
#         print("Weak Password")
# elif len(password) <= 4:
#     print("Moderate Password")
# else : 
#     print("Very Weak Password")
    

"""TASK 8: Write a program that displays -Babar Azam 
on output, if score >30,
Shoaib Akhtar, 
if 20<score<30, and Shahid Afridi if 10<score >20.
"""

score = int(input("Enter a Score"))
if score > 30 :
    print("Babar Azam")
elif 20< score <=30:
    print("Shoaib Akhtar")
elif 10<score<=20:
    print("Shahid Afridi")
else :
    print("No Player Matches")

"""
TASK 9: Write a program that takes password from user as input. 

Validate the password on the following criteria:
Password length between 7 to 15 characters which contain at least one 
numeric digit and a special character is acceptable
"""
Password = input("Enter a Password !!")

if 7 > len(Password) < 15:
    if Password.isdigit() :
        print("Strong Password")
    else :
        print("Weak Password")
else :
    print("Very Weak Password")

