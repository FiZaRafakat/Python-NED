# Combine Two dictionaries
dict1 = {'username': 'Fiza Rafakat'}
dict2 = {'Age':20}

dict1.update(dict2)
print(dict1)

# Create new dictionary and access their values 
book = {'Title':'Python','Author':"John Doe",'Price': 100}


# # Accesing Values using square brackets 
# print(book['Author'])
# # For accessing more than one key 
# print(book['fiza'],book['Author'])    #=> Throw an error 


# Accessing values using get method
print(book.get("price"))
print(book.get("Author"))


# Delete the title key form the above dictionary
del book['Title']
print(book)



