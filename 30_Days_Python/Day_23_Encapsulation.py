# Day 23: Encapsulation
# ---------------------

# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
# It describes the idea of wrapping data and the methods that work on data within one unit.
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

# 1. Private Members
# In Python, we use double underscore (__) before the variable name to make it private.

class Base:
    def __init__(self):
        self.a = "I am public"
        self.__c = "I am private"

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # print(self.__c) # This would raise an AttributeError

# Driver code
obj1 = Base()
print(obj1.a)
# print(obj1.__c) # AttributeError: 'Base' object has no attribute '__c'

# 2. Accessing Private Members
# We can access private members using name mangling: _ClassName__variableName
print("Accessing private variable via name mangling:", obj1._Base__c)

# 3. Getters and Setters
# To access and modify private variables properly, we use getter and setter methods.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")

stud = Student("Jessa", 14)

# retrieving age using getter
print('Name:', stud.name, 'Age:', stud.get_age())

# changing age using setter
stud.set_age(16)
print('Name:', stud.name, 'Age:', stud.get_age())

stud.set_age(-5) # Validation check
