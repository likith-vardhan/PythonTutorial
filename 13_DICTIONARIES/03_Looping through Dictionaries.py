student = {"name": "Ravi", "age": 22, "city": "Bengaluru"}

# Loop through keys (default)
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through both — most common ✅
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: Ravi
# age: 22
# city: Bengaluru