# Normal way — 4 lines
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)    # [1, 4, 9, 16, 25]

# List comprehension — 1 line ✅
squares = [i ** 2 for i in range(1, 6)]
print(squares)    # [1, 4, 9, 16, 25]

# With condition — even numbers only
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)      # [2, 4, 6, 8, 10]

# Transforming strings
fruits = ["apple", "banana", "mango"]
upper = [fruit.upper() for fruit in fruits]
print(upper)      # ['APPLE', 'BANANA', 'MANGO']