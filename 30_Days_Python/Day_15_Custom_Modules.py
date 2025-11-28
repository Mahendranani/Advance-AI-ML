# Day 15: Custom Modules
# ----------------------

# 1. Creating a Module
# To create a module just save the code you want in a file with the file extension .py
# We will create a simple module file named `mymodule.py` dynamically here for demonstration.

module_content = """
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
"""

with open("mymodule.py", "w") as f:
    f.write(module_content)

print("Created mymodule.py")

# 2. Use a Module
# Now we can use the module we just created, by using the import statement.
import mymodule

mymodule.greeting("Jonathan")

# 3. Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc).
a = mymodule.person1["age"]
print("Age from module:", a)

# 4. Re-naming a Module
import mymodule as mx
a = mx.person1["country"]
print("Country from module alias:", a)

# Clean up (optional, but good for keeping directory clean if this was just a test)
# import os
# os.remove("mymodule.py")
