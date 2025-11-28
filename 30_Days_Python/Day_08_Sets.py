# Day 8: Sets
# -----------

# 1. Creating a Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# 2. Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

print("banana" in thisset)

# 3. Add Items
thisset.add("orange")
print("After add:", thisset)

# 4. Remove Items
thisset.remove("banana") # Raises error if item does not exist
thisset.discard("banana") # Does NOT raise error if item does not exist
print("After remove:", thisset)

# 5. Loop Sets
print("\nLooping:")
for x in thisset:
    print(x)

# 6. Join Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print("Union:", set3)

# 7. Set Methods
# intersection, difference, symmetric_difference, etc.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print("Intersection:", z)

z = x.difference(y)
print("Difference (x - y):", z)
