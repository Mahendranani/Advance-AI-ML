# Day 20: Date and Time
# ---------------------

import datetime

# 1. Get Current Date
x = datetime.datetime.now()
print("Current Date/Time:", x)

# 2. Date Output
print("Year:", x.year)
print("Day of week:", x.strftime("%A"))

# 3. Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
x = datetime.datetime(2020, 5, 17)
print("Created Date:", x)

# 4. The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.

x = datetime.datetime(2018, 6, 1)

print("Month name, full version:", x.strftime("%B"))
print("Day of week, short version:", x.strftime("%a"))
print("Day of month:", x.strftime("%d"))
print("Year, short version:", x.strftime("%y"))

# 5. Time Delta
# Calculate differences between dates
today = datetime.date.today()
future = datetime.date(2025, 1, 1)
diff = future - today
print(f"\nDays until 2025-01-01: {diff.days}")

# 6. Parsing Dates
date_str = "2023-12-25"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed Date:", date_obj)

# Reviewed on 2025-08-27
