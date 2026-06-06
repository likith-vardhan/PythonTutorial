
# Adding items:

fruits = ["apple", "banana"]

# append() — add ONE item to the END
fruits.append("mango")
print(fruits)    # ['apple', 'banana', 'mango']

# insert() — add at a SPECIFIC position
fruits.insert(1, "kiwi")
print(fruits)    # ['apple', 'kiwi', 'banana', 'mango']

# extend() — add MULTIPLE items from another list
fruits.extend(["grape", "melon"])
print(fruits)    # ['apple', 'kiwi', 'banana', 'mango', 'grape', 'melon']


# Removing items

fruits = ["apple", "kiwi", "banana", "mango", "kiwi"]

# remove() — removes FIRST occurrence of a value
fruits.remove("kiwi")
print(fruits)    # ['apple', 'banana', 'mango', 'kiwi']

# pop() — removes by INDEX (default: last item) and RETURNS it
removed = fruits.pop()
print(removed)   # kiwi
print(fruits)    # ['apple', 'banana', 'mango']

removed = fruits.pop(0)
print(removed)   # apple
print(fruits)    # ['banana', 'mango']

# clear() — removes ALL items
fruits.clear()
print(fruits)    # []

# Searching & Sorting:

scores = [85, 92, 78, 92, 65, 88]

# index() — find position of first occurrence
print(scores.index(92))     # 1

# count() — how many times a value appears
print(scores.count(92))     # 2

# in — check if item exists
print(85 in scores)         # True
print(100 in scores)        # False

# sort() — sort in place (modifies original)
scores.sort()
print(scores)               # [65, 78, 85, 88, 92, 92]

scores.sort(reverse=True)
print(scores)               # [92, 92, 88, 85, 78, 65]

# sorted() — returns NEW sorted list (original unchanged)
nums = [3, 1, 4, 1, 5, 9]
new = sorted(nums)
print(new)                  # [1, 1, 3, 4, 5, 9]
print(nums)                 # [3, 1, 4, 1, 5, 9] — unchanged!

# reverse() — reverse in place
nums.reverse()
print(nums)                 # [9, 5, 1, 4, 1, 3]


# other useful methods

nums = [3, 1, 4, 1, 5]

print(len(nums))       # 5   — number of items
print(sum(nums))       # 14  — sum of all items
print(min(nums))       # 1   — smallest item
print(max(nums))       # 5   — largest item

# copy() — create independent copy
original = [1, 2, 3]
copy = original.copy()
copy.append(4)
print(original)        # [1, 2, 3] — unchanged!
print(copy)            # [1, 2, 3, 4]