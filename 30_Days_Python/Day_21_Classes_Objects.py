# Day 21: Classes and Objects
# ---------------------------

# 1. Create a Class
# To create a class, use the keyword class:
class MyClass:
  x = 5

# 2. Create Object
# Now we can use the class named MyClass to create objects:
p1 = MyClass()
print("p1.x:", p1.x)

# 3. The __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print("Name:", p1.name)
print("Age:", p1.age)

# 4. Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:

class PersonWithMethod:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = PersonWithMethod("John", 36)
p1.myfunc()

# 5. The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class PersonSelf:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = PersonSelf("John", 36)
p1.myfunc()

# 6. Modify Object Properties
p1.age = 40
print("Modified Age:", p1.age)

# 7. Delete Object Properties
del p1.age
# print(p1.age) # Error

# 8. Delete Objects
del p1
# print(p1) # Error
