name = "Alice"      # Box labeled 'name', contains "Alice"
age = 25            # Box labeled 'age', contains 25
city = "Bengaluru"  # Box labeled 'city', contains "Bengaluru"

print(name)   # Output: Alice
print(age)    # Output: 25
print(city)   # Output: Bengaluru

age = 25
temperature = -10
score = 0

print(type(age))    # Output: <class 'int'>


# ✅ Valid names
my_name = "Alice"
age2 = 25
_score = 100
firstName = "Bob"      # camelCase
first_name = "Bob"     # snake_case (Python preferred ✅)

# ❌ Invalid names
# 2age = 25          # Cannot START with a number
# my-name = "Alice"  # No hyphens allowed
# class = "Python"   # 'class' is a reserved keyword