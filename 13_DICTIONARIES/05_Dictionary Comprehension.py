# Normal way
squares = {}
for i in range(1, 6):
    squares[i] = i ** 2

# Dictionary comprehension ✅
squares = {i: i ** 2 for i in range(1, 6)}
print(squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {i: i**2 for i in range(1, 11) if i % 2 == 0}
print(even_squares)    # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}