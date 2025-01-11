#NESTED DICTIONARY
# nested_dict = {True: 'abc', 2: 'def', 3: {'a':11, 'b':12}}

my_family = {'child1': {'name':'Zuha', 'year':2009},\
    'child2':{'name':'Ahmed', 'year':2014} , \
        'child3':{'name': 'Hasan', 'year' : 2020 }}

print(len(my_family))
print(my_family.keys())
print(my_family.values())
print(my_family.items())
print(my_family['child2']) #all values in this key
print(my_family['child2']['name']) #specified key 

"""Task 3: Create a nested dictionary 
'students'.
students = {'Student1' :
 {'name':'john', 'age':38, 'grade':"A"},
 'Student2': {'name': 'Emma', 'age': 20, 
 'grade':'B'}}
Qs: 1 Print the grade of student2
Qs: 2 Update Student1's grade to 'A+'
Qs: 3 Add a new student, Student3, with the following 
details:
name: 'Mike',
age : '17'
grade: 'A'
 """
students = {'Student1' :
 {'name':'john', 'age':38, 'grade':"A"},
 'Student2': {'name': 'Emma', 'age': 20, 
 'grade':'B'}}
print(students['Student2']['grade'])
students['Student1']['grade'] = 'A+'
print(students)

students['Student3'] = {'name':'Mike', \
                        'age':17, 'grade':'A'}
print(students)

