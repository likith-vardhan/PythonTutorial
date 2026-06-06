# Looping Through Lists

fruits = ["apple", "banana", "mango"]

# Basic loop
for fruit in fruits:
    print(fruit)

# With index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. mango

# Loop with range and index
for i in range(len(fruits)):
    print(f"fruits[{i}] = {fruits[i]}")