# Day 29: Comprehensions
# ----------------------

# Comprehensions provide a concise way to create sequences (lists, sets, dictionaries, etc.) based on existing sequences.

# 1. List Comprehension
# Syntax: [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("List Comprehension:", newlist)

# Numbers
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# 2. Dictionary Comprehension
# Syntax: {key: value for (key, value) in iterable}

# Create a dict from two lists
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
myDict = {k:v for (k,v) in zip(keys, values)}
print("\nDict Comprehension:", myDict)

# Square dict
square_dict = {x: x**2 for x in range(5)}
print("Square Dict:", square_dict)

# 3. Set Comprehension
# Syntax: {expression for item in iterable}
# Similar to list comprehension but with curly brackets.

numbers = [1, 1, 2, 2, 3, 4, 5, 5]
unique_squares = {x**2 for x in numbers}
print("\nSet Comprehension:", unique_squares)

# 4. Generator Comprehension (Generator Expression)
# Syntax: (expression for item in iterable)
# We saw this in Day 26, but it's worth noting here as it fits the pattern.
gen = (x**2 for x in range(5))
print("\nGenerator Expression:", list(gen))
