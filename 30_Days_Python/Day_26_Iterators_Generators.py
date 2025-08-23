# Day 26: Iterators and Generators
# --------------------------------

# 1. Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print("Iterator next:", next(myit))
print("Iterator next:", next(myit))
print("Iterator next:", next(myit))

# 2. Creating an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print("\nCustom Iterator:")
for x in myiter:
  print(x)

# 3. Generators
# Generators are a simple way of creating iterators.
# All the work we mentioned above are automatically handled by generators in Python.
# A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

def my_generator():
    yield 1
    yield 2
    yield 3

print("\nGenerator:")
for value in my_generator():
    print(value)

# 4. Generator Expression
# Similar to list comprehension but returns a generator object.
# It uses parentheses () instead of brackets [].

my_gen = (x*x for x in range(5))
print("\nGenerator Expression:")
for x in my_gen:
    print(x)

# Reviewed on 2025-08-23
