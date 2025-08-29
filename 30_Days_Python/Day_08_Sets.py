
thisset = {"apple", "banana", "cherry"}
print(thisset)


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

# Reviewed on 2025-08-29
