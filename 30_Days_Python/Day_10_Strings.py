# Day 10: Strings
# ---------------

# 1. Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
a = "Hello, World!"
print(a[1]) # e

# 2. Slicing
print("Slice 2:5 ->", a[2:5]) # llo

# 3. Modify Strings
print("Upper:", a.upper())
print("Lower:", a.lower())
print("Replace H with J:", a.replace("H", "J"))
print("Split:", a.split(",")) # Returns a list

# 4. String Concatenation
b = "Welcome"
c = a + " " + b
print(c)

# 5. Format Strings (f-strings)
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# 6. Escape Characters
# To insert characters that are illegal in a string, use an escape character.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# 7. String Methods
# There are many built-in methods.
txt = "  hello world  "
print("Strip:", txt.strip()) # Removes whitespace from beginning and end
print("Count 'l':", txt.count("l"))
print("Find 'world':", txt.find("world"))

# Reviewed on 2025-09-03
