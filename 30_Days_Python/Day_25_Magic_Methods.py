# Day 25: Magic (Dunder) Methods
# ------------------------------

# Magic methods in Python are the special methods that start and end with the double underscores.
# They are also called dunder methods.
# Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.

# 1. __init__
# We have already seen this. It is the constructor.

# 2. __str__
# The __str__() method controls what should be returned when the class object is represented as a string.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print("String Representation:", p1)

# 3. __len__
# Controls the behavior of len() function.

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

l = MyList([1, 2, 3, 4])
print("Length of MyList:", len(l))

# 4. __add__ (Operator Overloading)
# Controls the behavior of + operator.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(2, 3)

print("Point Addition:", p1 + p2)

# 5. __eq__
# Controls equality ==

class PointEq:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = PointEq(1, 1)
p2 = PointEq(1, 1)
p3 = PointEq(1, 2)

print("p1 == p2:", p1 == p2)
print("p1 == p3:", p1 == p3)

# Reviewed on 2025-09-02
