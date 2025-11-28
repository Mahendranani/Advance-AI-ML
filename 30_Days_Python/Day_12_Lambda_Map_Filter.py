# Day 12: Lambda, Map, Filter, Reduce
# -----------------------------------

# 1. Lambda Functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print("Lambda x(5):", x(5))

multiply = lambda a, b : a * b
print("Lambda multiply(5, 6):", multiply(5, 6))

# 2. Map Function
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print("Map result:", list(x))

# Using lambda with map
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print("Squared with map:", list(squared))

# 3. Filter Function
# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
print("Adults (filter):", list(adults))

# Using lambda with filter
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print("Evens with filter:", list(evens))

# 4. Reduce Function
# The reduce() function accepts a function and a sequence and returns a single value calculated as follows:
# 1. Initially, the function is called with the first two items from the sequence and the result is returned.
# 2. The function is then called again with the result obtained in step 1 and the next value in the sequence.
# 3. This process keeps repeating until there are no items left in the sequence.

from functools import reduce

def add(x, y):
    return x + y

list1 = [2, 4, 7, 3]
print("Reduce (sum):", reduce(add, list1))
