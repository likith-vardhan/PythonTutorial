# What is a Dictionary?
# A dictionary stores data as key-value pairs — like a real dictionary where every word (key) has a definition (value).


# Creating a dictionary
student = {
    "name": "Ravi",
    "age": 22,
    "city": "Bengaluru",
    "marks": 92.5
}

print(student)
print(type(student))    # <class 'dict'>


# accessing values

student = {"name": "Ravi", "age": 22, "city": "Bengaluru"}

# Method 1: Square bracket — KeyError if key missing!
print(student["name"])      # Ravi
print(student["age"])       # 22

# Method 2: .get() — returns None if key missing (safe ✅)
print(student.get("city"))      # Bengaluru
print(student.get("salary"))    # None — no error!
print(student.get("salary", 0)) # 0 — custom default value

# Modifying Dictionaries

student = {"name": "Ravi", "age": 22}

# Add new key-value pair
student["city"] = "Bengaluru"
print(student)    # {'name': 'Ravi', 'age': 22, 'city': 'Bengaluru'}

# Update existing value
student["age"] = 23
print(student)    # {'name': 'Ravi', 'age': 23, 'city': 'Bengaluru'}

# Delete a key
del student["city"]
print(student)    # {'name': 'Ravi', 'age': 23}

# pop() — remove and return value
age = student.pop("age")
print(age)        # 23
print(student)    # {'name': 'Ravi'}

