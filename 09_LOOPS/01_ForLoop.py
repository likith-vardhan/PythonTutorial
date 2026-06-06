# range(stop) — from 0 to stop-1
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# range(start, stop)
for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8

# Counting backwards
for i in range(5, 0, -1):
    print(i)
# Output: 5 4 3 2 1

# Looping through a String
pythonname = "Python"

for letter in name:
    print(letter)
# Output:
# P
# y
# t
# h
# o
# n

# Looping with enumerate() — index + value together
pythonfruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: mango