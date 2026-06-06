
# Unlike strings, lists are mutable — you CAN change them in place!

fruits = ["apple", "banana", "mango"]

# Change an item
fruits[1] = "blueberry"
print(fruits)    # ['apple', 'blueberry', 'mango']

# Change a slice
fruits[0:2] = ["kiwi", "grape"]
print(fruits)    # ['kiwi', 'grape', 'mango']