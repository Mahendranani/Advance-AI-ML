# Day 22: Inheritance
# -------------------

# 1. Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

# 2. Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
class Student(Person):
  pass

# Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()

# 3. Add the __init__() Function
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class StudentWithInit(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# 4. Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class StudentSuper(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = StudentSuper("Mike", "Olsen", 2019)
x.welcome()

# Reviewed on 2025-09-20
