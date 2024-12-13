'''Question from Chatgpt for practice'''

a = 10
b = 3
c = 2
result = a // b * c
print(result)

'''Step-by-Step Breakdown:

    First, the floor division (//) is performed:

a // b

    a is 10 and b is 3.
    Floor division (//) returns the integer part of the division. When 10 is divided by 3, the result is approximately 3.33, but since we're doing floor division, it rounds down to the nearest integer.
    So, 10 // 3 results in 3.

Next, the result of the floor division is multiplied by c:

    result = 3 * c

        Now, 3 (from the floor division) is multiplied by c, which is 2.
        3 * 2 = 6

Final Result:

The final output is 6.'''

x = 5
y = 2
z = 4
result = x ** y - z
print(result)

'''Step-by-Step Breakdown:

    First, evaluate x ** y:

x ** y

    x is 5, and y is 2.
    Exponentiation (**) means raising x to the power of y. So:
    5 ** 2 = 5 * 5 = 25

Now subtract z from the result of x ** y:

    result = 25 - z

        z is 4.
        So, 25 - 4 = 21.

Final Result:

The final output will be 21.'''

a = 8
b = 5
c = 2
result = a % b + c * 2
print(result)

'''Step-by-Step Breakdown:

    First, evaluate a % b:

a % b

    a is 8, and b is 5.
    The modulus operation (%) returns the remainder when a is divided by b.
    When 8 is divided by 5, the quotient is 1 (because 5 goes into 8 once), and the remainder is 3.
    So, 8 % 5 results in 3.

Next, evaluate c * 2:

c * 2

    c is 2.
    So, 2 * 2 = 4.

Now add the results of a % b and c * 2:

    result = 3 + 4

        The result of 3 + 4 is 7.

Final Result:

The final output is 7.'''


x = 7
y = 3
z = 2
result = (x + y) ** z // x
print(result)

'''Step-by-Step Breakdown:

    First, evaluate the parentheses (x + y):

x + y = 7 + 3 = 10

Next, apply the exponentiation ** to the result of (x + y):

10 ** z = 10 ** 2 = 100

Now, perform floor division // with the result of the exponentiation (100) and x (which is 7):

100 // 7 = 14'''

a = 6
b = 4
c = 2
result = (a + b) // c - a
print(result)

'''Step-by-Step Breakdown:

    First, evaluate the parentheses (a + b):

a + b = 6 + 4 = 10

Next, apply the floor division // with the result of (a + b) (which is 10) and c (which is 2):

10 // c = 10 // 2 = 5

Now, subtract a (which is 6) from the result of the floor division:

    5 - a = 5 - 6 = -1

Final Result:

The final output will be -1.'''

x = 10
y = 3
z = 2
result = x + y * z - x // y
print(result)

'''Step-by-Step Breakdown:

    Multiplication (y * z):

y * z = 3 * 2 = 6

Floor division (x // y):

x // y = 10 // 3 = 3

(Floor division gives the quotient without the remainder.)

Now, apply the addition and subtraction:

    result = x + (y * z) - (x // y)
    result = 10 + 6 - 3
    result = 16 - 3
    result = 13

Final Result:

The final output will be 13.'''


a = 8
b = 4
c = 2
result = (a + b) * c // a - b
print(result)


'''Step-by-Step Breakdown:

    Evaluate the parentheses (a + b):

a + b = 8 + 4 = 12

Next, multiply by c:

12 * c = 12 * 2 = 24

Now, apply floor division // with a:

24 // a = 24 // 8 = 3

(Floor division gives the quotient without the remainder.)

Finally, subtract b:

    3 - b = 3 - 4 = -1

Final Result:

The final output will be -1.'''

p = 9
q = 5
r = 4
result = p % q + r * p // q
print(result)

'''Step-by-Step Breakdown:

    Evaluate the modulus operation (p % q):

p % q = 9 % 5 = 4

(The remainder when 9 is divided by 5 is 4.)

Evaluate the multiplication (r * p):

r * p = 4 * 9 = 36

Now, apply floor division (//) with p // q:

36 // q = 36 // 5 = 7

(Floor division gives the quotient without the remainder, so 36 divided by 5 is 7.)

Finally, apply addition (p % q + (r * p // q)):

    result = 4 + 7 = 11

Final Result:

The final output will be 11.'''

m = 6
n = 2
o = 3
result = m * (n + o) // n - m % o
print(result)


'''Step-by-Step Breakdown:

    Evaluate the parentheses (n + o):

n + o = 2 + 3 = 5

Now, multiply m by the result of (n + o):

m * (n + o) = 6 * 5 = 30

Next, apply floor division (//) with n:

30 // n = 30 // 2 = 15

Now, evaluate the modulus (m % o):

m % o = 6 % 3 = 0

Finally, apply the subtraction:

    result = 15 - 0 = 15

Final Result:

The final output will be 15.'''

a = 15
b = 4
c = 5
result = a // b * c - a % b
print(result)

'''Step-by-Step Breakdown:

    Evaluate the floor division (a // b):

a // b = 15 // 4 = 3

(The floor division of 15 by 4 gives 3.)

Now, multiply the result of floor division by c:

3 * c = 3 * 5 = 15

Evaluate the modulus operation (a % b):

a % b = 15 % 4 = 3

(The remainder when 15 is divided by 4 is 3.)

Finally, apply the subtraction:

    result = 15 - 3 = 12

Final Result:

The final output will be 12.'''