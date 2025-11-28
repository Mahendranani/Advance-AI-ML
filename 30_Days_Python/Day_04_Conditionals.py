# Day 4: Conditional Statements
# -----------------------------

# 1. If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2. Elif and Else
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 3. Nested If
num = 15
if num > 10:
    print("Above 10,")
    if num > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# 4. Short Hand If ... Else (Ternary Operator)
a = 200
b = 33
print("A") if a > b else print("B")

# 5. Pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if a > b:
    pass
