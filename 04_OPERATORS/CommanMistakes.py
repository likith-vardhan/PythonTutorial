# ❌ Mistake 1: Using = instead of == in comparison
x = 5
print(x = 5)    # SyntaxError!

# ✅ Fix:
print(x == 5)   # True


# ❌ Mistake 2: Division always gives float
result = 10 / 2
print(result)        # 5.0, NOT 5
print(type(result))  # <class 'float'>

# ✅ Fix: Use // if you need an integer
result = 10 // 2
print(result)        # 5
print(type(result))  # <class 'int'>


# ❌ Mistake 3: Forgetting operator precedence
discount = 10
price = 200 + 100 * discount   # Multiplies first! = 1200
# ✅ Fix:
price = (200 + 100) * discount  # = 3000