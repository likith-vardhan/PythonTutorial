# Creating tuples
point = (12.9716, 77.5946)
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14, True)
empty = ()

# Single item tuple — MUST have trailing comma!
single = (42,)         # ✅ This is a tuple
not_tuple = (42)       # ❌ This is just an integer in brackets!

print(type(single))    # <class 'tuple'>
print(type(not_tuple)) # <class 'int'>

