# ❌ Mistake 1: Index out of range
name = "Hi"
print(name[5])    # Error! Only index 0 and 1 exist

# ✅ Fix: Always check length first
print(len(name))  # 2


# ❌ Mistake 2: Strings are IMMUTABLE — can't change one character
name = "Jawa"
name[0] = "R"     # Error! Strings cannot be modified in place

# ✅ Fix: Create a new string
name = "R" + name[1:]
print(name)       # Rawa


# ❌ Mistake 3: Concatenating string + number directly
age = 22
print("Age: " + age)      # Error! Can't join str and int

# ✅ Fix: Convert to string first
print("Age: " + str(age)) # Age: 22
# Or just use f-string:
print(f"Age: {age}")      # Age: 22