# Day 5: Loops
# ------------

# 1. While Loop
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
print("While Loop:")
while i < 6:
    print(i)
    i += 1

# 2. For Loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
print("\nFor Loop (List):")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print("\nFor Loop (String):")
for x in "banana":
    print(x)

# 3. The range() Function
print("\nRange Function:")
for x in range(5): # 0 to 4
    print(x)

print("\nRange(2, 6):")
for x in range(2, 6): # 2 to 5
    print(x)

# 4. Break and Continue
print("\nBreak Statement (stops at 3):")
for x in range(1, 6):
    if x == 3:
        break
    print(x)

print("\nContinue Statement (skips 3):")
for x in range(1, 6):
    if x == 3:
        continue
    print(x)

# 5. Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
print("\nElse in Loop:")
for x in range(3):
    print(x)
else:
    print("Finally finished!")
