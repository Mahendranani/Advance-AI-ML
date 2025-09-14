# Day 19: Working with JSON Files
# -------------------------------

import json

# 1. Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("JSON to Dict:", y["age"])

# 2. Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print("Dict to JSON:", y)

# 3. Formatting JSON
# The json.dumps() method has parameters to make it easier to read the result:
print("\nPretty Print:")
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# 4. Writing JSON to a File
data = {
    "employees": [
        {"name": "John Doe", "department": "Sales"},
        {"name": "Jane Smith", "department": "Marketing"}
    ]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nCreated data.json")

# 5. Reading JSON from a File
with open("data.json", "r") as f:
    data_loaded = json.load(f)

print("Loaded from file:", data_loaded["employees"][0]["name"])

# Cleanup
import os
if os.path.exists("data.json"):
    os.remove("data.json")
print("Cleaned up data.json")

# Reviewed on 2025-09-15
