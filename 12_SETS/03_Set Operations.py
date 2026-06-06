a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — all items from both sets
print(a | b)           # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))      # same thing

# Intersection — only items in BOTH sets
print(a & b)               # {4, 5}
print(a.intersection(b))   # same thing

# Difference — items in a but NOT in b
print(a - b)               # {1, 2, 3}
print(a.difference(b))     # same thing

# Symmetric difference — items in either but NOT both
print(a ^ b)                        # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))    # same thing