student = {"name": "Ravi", "age": 22, "city": "Bengaluru"}

# Keys, values, items
print(student.keys())     # dict_keys(['name', 'age', 'city'])
print(student.values())   # dict_values(['Ravi', 22, 'Bengaluru'])
print(student.items())    # dict_items([('name','Ravi'),('age',22),...])

# Check if key exists
print("name" in student)      # True
print("salary" in student)    # False

# Update with another dictionary
student.update({"salary": 50000, "age": 25})
print(student)
# {'name': 'Ravi', 'age': 25, 'city': 'Bengaluru', 'salary': 50000}

# Copy
copy = student.copy()

# Clear
student.clear()
print(student)    # {}