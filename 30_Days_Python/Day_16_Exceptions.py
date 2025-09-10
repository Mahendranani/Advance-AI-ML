# Day 16: Exception Handling
# --------------------------

# 1. Try Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.

try:
  print(x_undefined) # This variable is not defined
except:
  print("An exception occurred")

# 2. Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error.
try:
  print(x_undefined)
except NameError:
  print("Variable x_undefined is not defined")
except:
  print("Something else went wrong")

# 3. Else
# You can use the else keyword to define a block of code to be executed if no errors were raised.
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# 4. Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x_undefined)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# 5. Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.

x = -1

if x < 0:
  # raise Exception("Sorry, no numbers below zero") # Uncomment to see error
  print("Would raise Exception here if uncommented")

x = "hello"

if not type(x) is int:
  # raise TypeError("Only integers are allowed") # Uncomment to see error
  print("Would raise TypeError here if uncommented")

# Reviewed on 2025-09-10
