# Day 14: Modules
# ---------------

# 1. What is a Module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# We can import built-in modules.
import platform

x = platform.system()
print("System:", x)

# 2. Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module.
x = dir(platform)
print("Dir of platform (first 5):", x[:5])

# 3. Import From Module
# You can choose to import only parts from a module, by using the from keyword.
from math import sqrt, pi

print("Square root of 16:", sqrt(16))
print("Pi:", pi)

# 4. Renaming a Module
# You can create an alias when you import a module, by using the as keyword.
import datetime as dt

x = dt.datetime.now()
print("Current date/time:", x)

# 5. Math Module
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print("Ceil:", x)
print("Floor:", y)

# 6. Random Module
import random

print("Random number (0-9):", random.randrange(1, 10))
print("Random choice:", random.choice(["apple", "banana", "cherry"]))

# Reviewed on 2025-09-14
