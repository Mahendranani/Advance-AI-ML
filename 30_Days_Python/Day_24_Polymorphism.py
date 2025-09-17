# Day 24: Polymorphism
# --------------------

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# 1. Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.

# String
x = "Hello World"
print("Len of string:", len(x))

# Tuple
mytuple = ("apple", "banana", "cherry")
print("Len of tuple:", len(mytuple))

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Len of dict:", len(thisdict))

# 2. Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       # Create a Car class
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat class
plane1 = Plane("Boeing", "747")     # Create a Plane class

print("\nPolymorphism with Classes:")
for x in (car1, boat1, plane1):
  print(f"{x.brand} {x.model}: ", end="")
  x.move()

# 3. Inheritance Class Polymorphism
# What about child classes with the same name?

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

print("\nPolymorphism with Inheritance:")
for x in (car1, boat1, plane1):
  print(x.brand, ": ", end="")
  x.move()

# Reviewed on 2025-09-18
