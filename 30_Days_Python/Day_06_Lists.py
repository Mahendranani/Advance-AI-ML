# Day 6: Lists
# ------------

# 1. Creating a List
# Lists are used to store multiple items in a single variable.
# Lists are ordered, changeable, and allow duplicate values.

thislist = ["apple", "banana", "cherry"]
print(thislist)

# 2. Access Items
print("First item:", thislist[0])
print("Last item:", thislist[-1])

# 3. Range of Indexes (Slicing)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("2 to 5:", numbers[2:5]) # [2, 3, 4]

# 4. Change Item Value
thislist[1] = "blackcurrant"
print("Modified list:", thislist)

# 5. List Methods
# Append
thislist.append("orange")
print("After append:", thislist)

# Insert
thislist.insert(1, "blueberry")
print("After insert:", thislist)

# Remove
thislist.remove("banana") # Error if not found, but we replaced banana earlier so let's remove 'apple'
thislist.remove("apple")
print("After remove:", thislist)

# Pop (removes last item by default)
thislist.pop()
print("After pop:", thislist)

# Clear
# thislist.clear()

# 6. Loop Through a List
print("\nLooping:")
for x in thislist:
    print(x)

# 7. List Comprehension (Preview - more in Day 29)
# [expression for item in iterable if condition == True]
newlist = [x for x in numbers if x % 2 == 0]
print("Even numbers:", newlist)

# Reviewed on 2025-08-21
