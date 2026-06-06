
# concatination
name = "Ravi"
age = 22
print("My name is " + name + " and I am " + str(age) + " years old.")

# Way 2 — .format() method
print("My name is {} and I am {} years old.".format(name, age))

# Way 3 — f-strings (modern, preferred ✅)

print(f"My name is {name} and I am {age} years old.")

# f-strings can even do math inside!
a, b = 10, 20
print(f"Sum of {a} and {b} is {a + b}")
# Output: Sum of 10 and 20 is 30

price = 1234.5678

print(f"{price:.2f}")      # 1234.57  — 2 decimal places
print(f"{price:,.2f}")     # 1,234.57 — comma separator
print(f"{42:05d}")         # 00042    — pad with zeros
print(f"{'hello':>10}")    #      hello — right align in 10 chars
print(f"{'hello':<10}|")   # hello     | — left align
print(f"{'hello':^10}")    #   hello   — center align