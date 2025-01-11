# # #6TH DataType is List
# # my_list = [1, 'python', False, 10.09, '99']

# # #accessing elements in a list
# # print(len(my_list))

# # print(my_list[0]) 
# # print(my_list[1])
# # print(my_list[2])
# # print(my_list[3])
# # print(my_list[4])
# # print(my_list[-1])

# #insertion/ deletion using slicing in lists
# # marks = [98, 70, 50,10, 11, 12, 13]
# # print(len(marks))
# # marks[1:2] = marks[100, 100]

# #lists and strings are 'mutable'
# #Lists Insertion and Replacement
# marks = [98, 70, 50,10, 11, 12, 13]
# print('Original List:', marks)
# print(len(marks)) #7
# marks[0:1] = [100, 100] #insertion at index 0 +replacement
# marks[0:2] = [200, 200]
# # print(marks)
# marks[0] = 10
# print('Final Mutated List:', marks)

#insertion without replacemnt
# marks[1:1] = ['a', 'b']
# print('Insertion without replacement List:', marks)

# #deletion
# marks[2:3] = []
# print('Deletion on List:', marks)

#List Methods
my_list = ['apple', 'banana', 'grapes', 'orange']
# # print(len(my_list)) #4 : length

# #appending the list
# fruit = 'strawberry'
# my_list.append(fruit)
# print("Appended List:", my_list)

# #reversing a list
# my_list.reverse()
# print("Reversed_List:" , my_list)

# #sorting a list w.r.t ascending
# a = [1 , 10, 5, 2, 0]
# a.sort() #ascending order sorting
# a.sort(reverse = True) #sorting in descending order
# print("Sorted List:", a)

# #extending a list
# my_list2 = [1,2,3]
# my_list.extend(my_list2)
# print("Extended List:", my_list)

# #Pop (Delete) last item from a list
# my_list.pop()
# print('Last Item is removed:', my_list)
print('Final List:', my_list)

#making a copy of  a list

# L = my_list
# print(L) 
L = my_list.copy()
print('Copied List:', L)

element = False
L.append(element)
print('Appended List my_list:', L)

"""Task: 01 Consider a list of your choice and 
    *print last three elements,
    *print starting three elements"""

"""Task: 02 Replace the 2nd element of your
considered list with '25' integer"""
