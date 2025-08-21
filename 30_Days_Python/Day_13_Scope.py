# Day 13: Variable Scope
# ----------------------

# 1. Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
  x = 300
  print("Inside function:", x)

myfunc()
# print(x) # This would raise an error because x is not available outside the function

# 2. Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

x = 300

def myfunc2():
  print("Inside function (global x):", x)

myfunc2()
print("Outside function:", x)

# 3. Naming Conflict
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables,
# one available in the global scope (outside the function) and one available in the local scope (inside the function).

x = 300

def myfunc3():
  x = 200
  print("Inside function (local x):", x)

myfunc3()
print("Outside function (global x):", x)

# 4. Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.

def myfunc4():
  global y
  y = 400

myfunc4()
print("Global y created inside function:", y)

# Also, use the global keyword if you want to make a change to a global variable inside a function.
x = 300

def myfunc5():
  global x
  x = 200

myfunc5()
print("Modified global x:", x)

# 5. Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print("Nonlocal x:", myfunc1())

# Reviewed on 2025-08-21
