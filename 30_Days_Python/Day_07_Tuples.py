# Day 7: Tuples
# -------------

# 1. Creating a Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and UNCHANGEABLE.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# 2. Access Tuple Items
print("Second item:", thistuple[1])

# 3. Update Tuples
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable.
# But there is a workaround: convert the tuple into a list, change the list, and convert the list back into a tuple.

y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print("Modified tuple:", thistuple)

# 4. Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# 5. Loop Through a Tuple
print("\nLooping:")
for x in thistuple:
    print(x)

# 6. Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print("Joined tuple:", tuple3)

# 7. Count and Index methods
t = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = t.count(5)
print("Count of 5:", x)

y = t.index(8)
print("Index of first 8:", y)

# Reviewed on 2025-08-25
