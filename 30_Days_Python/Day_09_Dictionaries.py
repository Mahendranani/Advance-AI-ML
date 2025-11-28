# Day 9: Dictionaries
# -------------------

# 1. Creating a Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# 2. Accessing Items
x = thisdict["model"]
print("Model:", x)

y = thisdict.get("year")
print("Year:", y)

# 3. Change Values
thisdict["year"] = 2018
print("Updated year:", thisdict["year"])

# 4. Add Items
thisdict["color"] = "red"
print("After adding color:", thisdict)

# 5. Remove Items
thisdict.pop("model")
print("After popping model:", thisdict)

# 6. Loop Through a Dictionary
print("\nLooping Keys:")
for x in thisdict:
    print(x)

print("\nLooping Values:")
for x in thisdict:
    print(thisdict[x])

print("\nLooping Items:")
for x, y in thisdict.items():
    print(x, ":", y)

# 7. Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print("\nChild1 Name:", myfamily["child1"]["name"])
