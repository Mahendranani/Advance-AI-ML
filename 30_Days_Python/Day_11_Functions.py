# Day 11: Functions
# -----------------

# 1. Creating a Function
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
  print("Hello from a function")

# Calling a function
my_function()

# 2. Arguments
# Information can be passed into functions as arguments.
def my_function_with_args(fname):
  print(fname + " Refsnes")

my_function_with_args("Emil")
my_function_with_args("Tobias")

# 3. Number of Arguments
# By default, a function must be called with the correct number of arguments.
def my_function_full_name(fname, lname):
  print(fname + " " + lname)

my_function_full_name("Emil", "Refsnes")

# 4. Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name.
def my_function_kids(*kids):
  print("The youngest child is " + kids[2])

my_function_kids("Emil", "Tobias", "Linus")

# 5. Keyword Arguments
# You can also send arguments with the key = value syntax.
def my_function_child(child3, child2, child1):
  print("The youngest child is " + child3)

my_function_child(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# 6. Return Values
def my_function_math(x):
  return 5 * x

print(my_function_math(3))
print(my_function_math(5))

# 7. Default Parameter Value
def my_function_country(country = "Norway"):
  print("I am from " + country)

my_function_country("Sweden")
my_function_country()

# Reviewed on 2025-08-28
