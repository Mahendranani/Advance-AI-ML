# Day 2: Variables and Data Types
# -------------------------------

# 1. Variables
# A variable is a container for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

# Variable names are case-sensitive (age, Age and AGE are three different variables)
age = 25
Age = 30
print("age:", age)
print("Age:", Age)

# 2. Data Types
# Python has the following data types built-in by default:

# Text Type:	str
name = "Alice"
print("Type of name:", type(name))

# Numeric Types:	int, float, complex
count = 10          # int
price = 19.99       # float
comp = 1j           # complex
print("Type of count:", type(count))
print("Type of price:", type(price))

# Sequence Types:	list, tuple, range
my_list = ["apple", "banana", "cherry"]
print("Type of my_list:", type(my_list))

# Mapping Type:	dict
my_dict = {"name": "John", "age": 36}
print("Type of my_dict:", type(my_dict))

# Boolean Type:	bool
is_active = True
print("Type of is_active:", type(is_active))

# 3. Type Conversion (Casting)
# You can convert from one type to another with the int(), float(), and str() methods.

num_str = "100"
num_int = int(num_str)  # Convert string to int
print("Converted int:", num_int, type(num_int))

val_float = 3.14
val_int = int(val_float) # Convert float to int (truncates decimal)
print("Converted float to int:", val_int)

val_num = 50
val_str = str(val_num) # Convert int to string
print("Converted int to str:", val_str, type(val_str))
