# #public modifiers
# class Person :
#     def __init__(self, id):
#         self.id = id

# obj = Person(12)
# print(obj.id)  #attribute is publicly accessible
# print(obj.__dir__())

#protected modifiers
# class Person :
#     def __init__(self , id):
#         self._id = id   #attribute is protected
# obj = Person(12)
# print(obj.__dir__())
# print(obj._id)  #to modify and access it is ethically wrong

"""Private Modifiers (when we use __varName then python does name mangling)
i.e it considers it a Private Attribute and secures is"""
class Person :
    def __init__(self , id):
        self.__id = id   #attribute is protected

obj = Person(12)
print(obj.__dir__())
# print(obj.__id)  #it is giving an error
print(obj._Person__id)  #it will work : access private variable via this