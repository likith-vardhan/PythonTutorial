fruits = {"apple", "banana", "mango"}

# Adding
fruits.add("kiwi")
print(fruits)          # {'apple', 'banana', 'mango', 'kiwi'}

# Removing
fruits.remove("banana")    # Error if item doesn't exist!
fruits.discard("banana")   # Safe — no error if missing ✅
print(fruits)

# Membership check — sets are VERY fast at this
print("apple" in fruits)   # True
print("grape" in fruits)   # False