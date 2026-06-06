students = {
    "Ravi": {"age": 22, "marks": 92},
    "Priya": {"age": 21, "marks": 88},
    "Arjun": {"age": 23, "marks": 95}
}

# Access nested value
print(students["Priya"]["marks"])    # 88

# Loop through nested dict
for name, info in students.items():
    print(f"{name} → Age: {info['age']}, Marks: {info['marks']}")