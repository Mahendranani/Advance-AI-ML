# Day 17: File Handling
# ---------------------

# 1. Open a File
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# Create a dummy file for testing
with open("demofile.txt", "w") as f:
    f.write("Hello! Welcome to demofile.txt\nThis file is for testing purposes.\nGood Luck!")

# 2. Read Files
f = open("demofile.txt", "r")
print("Read entire file:")
print(f.read())
f.close()

# 3. Read Only Parts of the File
f = open("demofile.txt", "r")
print("\nRead first 5 chars:", f.read(5))
f.close()

# 4. Read Lines
f = open("demofile.txt", "r")
print("\nRead line:", f.readline())
f.close()

# 5. Loop through the file line by line
print("\nLoop lines:")
f = open("demofile.txt", "r")
for x in f:
  print(x.strip())
f.close()

# 6. Write to an Existing File
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("demofile.txt", "a")
f.write("\nNow the file has more content!")
f.close()

# Verify append
f = open("demofile.txt", "r")
print("\nAfter append:")
print(f.read())
f.close()

# 7. Delete a File
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
  print("\nFile 'demofile.txt' deleted.")
else:
  print("The file does not exist")
