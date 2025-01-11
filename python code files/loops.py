# a = 2
# b = 5
# print(max(a,b))
# print(min(a, b))
# colors = ['red', 'blue', 'orange']
# #print 'PRESENT' after checking if red is in the list
# if 'red' in colors:
#     print('PRESENT')
# else:
#     print('not present')

"""loops are used to automate tasks.
Loops are 'iterable'
(run mulitple time under specific time limit)
there are 2 types of loops in python:
1)for loop
2)while loop
           """
# #Understanding Range Function in for loop
print('Output of range = 5\n')
for i in range(5):
    print(i)
print('\nOutput of range = (0, 5)\n')
for j in range(0,5):
    print(j)
print('\nOutput of range = (1, 5)\n')
for k in range(1,5):
    print(k)
print('\nOutput of range = (2, 5)\n')
for l in range(2,5):
    print(l)
print('\nOutput of range = (3, 5)\n')
for m in range(3,5):
    print(m)
#UNDERSTADNING STEP SIZE IN RANGE FUNCTION
print('\nOutput when range = (0, 10, 1)\n')
for i in range (0,10,1):
    print(i)
print('\nOutput when range = (0, 10, 2)\n')
for i in range (0,10,2):
    print(i)
print('\nOutput when range = (0, 10, 3)\n')
for i in range(0,10,3):
    print(i)

"""write a program with range(5) but it should give 
1
2
3
4
5 as an ouput. """
for i in range(5):
    print(i+1)

# understanding for with 'pass'
for i in range(5):
    pass

'''write a table of number of your choice 
output: 2 x 1 = 2
'''
num = int(input('Enter a number: '))
for i in range (1,11):
    print(num, 'x', i, '=', num * i)
    #or
    # print(f'{num} x {i} = {num * i}') # f-string

#understanding the break statement
num = int(input('Enter a number: '))
for i in range (1,11):
    if i == 3:
        break #coming out of the loop at i = 3
    print(num, 'x', i, '=', num * i)

print('loop is terminated')

#understanding the continue statement
num = int(input('Enter a number: '))
for i in range (1,11):
    if i == 3:  #skipping i = 3 iteration
        continue
    print(num, 'x', i, '=', num * i)

print('loop is terminated')

#understanding else with for:
for i in range (3):
    print(i)
    if i == 4:
        break
else: #only executes when loop runs completely otherwise \
    #if loop breaks else doesn't execute 
    print('Else is Executed when break condition doesnt run')

#nesting in for loops
colors = ['red', 'blue', 'orange']
for i in colors:
    print(i) #output: red blue orange
    for j in i: # required output: r e d b l u e o r a n g e
        print(j)
