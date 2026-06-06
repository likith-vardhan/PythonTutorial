# Returning a single value

def square(n):
    return n ** 2

result = square(5)
print(result)          # 25
print(square(10))      # 100
print(square(3) + 1)   # 10 — use return value directly in expressions


# Returning multiple values (as a tuple)

def min_max(numbers):
    return min(numbers), max(numbers)    # returns a tuple

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(low)     # 1
print(high)    # 9

# Or capture as tuple
result = min_max([3, 1, 4, 1, 5, 9])
print(result)          # (1, 9)
print(result[0])       # 1


# Early return — exit function immediately

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"    # exits here
    return a / b                           # only runs if b != 0

print(divide(10, 2))    # 5.0
print(divide(10, 0))    # Cannot divide by zero!


# Functions without return

def say_hi():
    print("Hi!")

result = say_hi()    # Hi! — prints, but...
print(result)        # None — no return value means None