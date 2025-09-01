# Day 28: Regular Expressions (RegEx)
# -----------------------------------

import re

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

txt = "The rain in Spain"

# 1. Search
# The search() function searches the string for a match, and returns a Match object if there is a match.
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

# 2. Findall
# The findall() function returns a list containing all matches.
x = re.findall("ai", txt)
print("Findall 'ai':", x)

# 3. Split
# The split() function returns a list where the string has been split at each match.
x = re.split("\s", txt)
print("Split at whitespace:", x)

# 4. Sub
# The sub() function replaces the matches with the text of your choice.
x = re.sub("\s", "9", txt)
print("Sub whitespace with 9:", x)

# 5. Match Object
# A Match Object is an object containing information about the search and the result.
x = re.search("ai", txt)
print("\nMatch Object:")
print("Span:", x.span()) # tuple containing the start-, and end positions of the match
print("String:", x.string) # the string passed into the function
print("Group:", x.group()) # part of the string where there was a match

# 6. Metacharacters
# []	A set of characters	"[a-m]"
# \d	Returns a match where the string contains digits (numbers from 0-9)
# .	Any character (except newline character)
# ^	Starts with
# $	Ends with
# *	Zero or more occurrences
# +	One or more occurrences

txt = "The rain in Spain 123"
x = re.findall("\d", txt)
print("\nDigits found:", x)

# Reviewed on 2025-09-01
