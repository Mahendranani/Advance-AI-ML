# Day 18: Working with CSV Files
# ------------------------------

import csv

# 1. Writing to a CSV File
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

filename = 'people.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Created {filename}")

# 2. Reading from a CSV File
print("\nReading CSV:")
with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 3. Reading as Dictionary
print("\nReading as Dict:")
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row))

# 4. Writing Dictionary to CSV
data_dict = [
    {'Name': 'David', 'Age': 40, 'City': 'Seattle'},
    {'Name': 'Eve', 'Age': 28, 'City': 'Austin'}
]

with open('people_dict.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data_dict)

print("\nCreated people_dict.csv")

# Cleanup
import os
if os.path.exists("people.csv"):
    os.remove("people.csv")
if os.path.exists("people_dict.csv"):
    os.remove("people_dict.csv")
print("Cleaned up CSV files.")

# Reviewed on 2025-09-16
