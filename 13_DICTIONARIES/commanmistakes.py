# ❌ Mistake 1: Modifying a tuple
coords = (10, 20)
coords[0] = 99    # TypeError! Tuples are immutable

# ✅ Fix: Convert to list, modify, convert back
coords = list(coords)
coords[0] = 99
coords = tuple(coords)


# ❌ Mistake 2: Empty set with {}
empty = {}
print(type(empty))    # <class 'dict'> — NOT a set!

# ✅ Fix:
empty = set()


# ❌ Mistake 3: KeyError in dictionary
student = {"name": "Ravi"}
print(student["age"])    # KeyError! 'age' doesn't exist

# ✅ Fix: Use .get()
print(student.get("age", "Not found"))    # Not found


# ❌ Mistake 4: Using mutable types as dict keys
d = {[1,2]: "value"}    # TypeError! Lists can't be keys

# ✅ Fix: Use tuples as keys (they're immutable)
d = {(1,2): "value"}    # Works! ✅


# ❌ Mistake 5: Assuming set order
s = {3, 1, 4, 1, 5}
print(s[0])    # TypeError! Sets have no index

# ✅ Fix: Convert to list first if you need indexing
s_list = list(s)
print(s_list[0])