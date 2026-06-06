# ❌ Mistake 1: Using a variable before creating it
print(salary)    # Error! 'salary' doesn't exist yet

# ✅ Fix: Always define before using
salary = 50000
print(salary)


# ❌ Mistake 2: Mixing up types accidentally
age = "25"       # This is a STRING, not a number!
print(age + 5)   # Error! Can't add text and number

# ✅ Fix:
age = 25         # Integer
print(age + 5)   # Output: 30


# ❌ Mistake 3: Case sensitivity
Name = "Alice"
print(name)      # Error! 'name' and 'Name' are DIFFERENT variables

# ✅ Fix: Be consistent
name = "Alice"
print(name)