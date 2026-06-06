# ❌ Mistake 1: Index out of range
fruits = ["apple", "banana", "mango"]
print(fruits[3])      # Error! Valid indices: 0, 1, 2

# ✅ Fix: Use len() to check
print(fruits[len(fruits) - 1])   # Last item safely


# ❌ Mistake 2: Copying a list with =
a = [1, 2, 3]
b = a             # b is NOT a copy — both point to same list!
b.append(4)
print(a)          # [1, 2, 3, 4] — a changed too! 😱

# ✅ Fix: Use .copy()
b = a.copy()
b.append(4)
print(a)          # [1, 2, 3] — unchanged ✅


# ❌ Mistake 3: Modifying list while looping
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)    # Skips items! Unpredictable behavior
print(nums)                 # [1, 3, 5] — seems fine but unreliable

# ✅ Fix: Loop over a copy
for num in nums.copy():
    if num % 2 == 0:
        nums.remove(num)


# ❌ Mistake 4: append() vs extend()
fruits = ["apple"]
fruits.append(["banana", "mango"])    # Adds a LIST inside the list!
print(fruits)    # ['apple', ['banana', 'mango']] 😱

# ✅ Fix: Use extend() to add multiple items
fruits = ["apple"]
fruits.extend(["banana", "mango"])
print(fruits)    # ['apple', 'banana', 'mango'] ✅