# Assign tuple values directly to variables
point = (10, 20)
x, y = point
print(x)    # 10
print(y)    # 20

# Works with any sequence
name, age, city = ("Ravi", 25, "Bengaluru")
print(name)    # Ravi
print(age)     # 25

# Swap variables using tuple unpacking!
a, b = 5, 10
a, b = b, a         # Most Pythonic swap
print(a, b)         # 10 5

# Star unpacking — grab the rest
first, *rest = (1, 2, 3, 4, 5)
print(first)        # 1
print(rest)         # [2, 3, 4, 5]

*start, last = (1, 2, 3, 4, 5)
print(start)        # [1, 2, 3, 4]
print(last)         # 5



# When to use Tuple vs List?
# python ✅ Use TUPLE for fixed data that shouldn't change
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

db_config = ("localhost", 5432, "mydb")   # host, port, dbname

# ✅ Use LIST for data that will grow/change
shopping_cart = ["apple", "bread"]
shopping_cart.append("milk")