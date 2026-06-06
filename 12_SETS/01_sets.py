# What is a Set?
# A set is an unordered collection with no duplicates.

# Creating sets
fruits = {"apple", "banana", "mango", "apple", "banana"}
print(fruits)    # {'mango', 'apple', 'banana'} — duplicates removed!
                 # order may vary each time you run!

# Empty set — MUST use set(), not {}
empty = set()    # ✅
empty = {}       # ❌ This creates an empty DICTIONARY!

# Convert list to set — instant duplicate removal!
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)    # {1, 2, 3, 4}