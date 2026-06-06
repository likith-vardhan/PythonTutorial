age = int(input("Enter your age: "))
# User types: 22
# input() gives "22" (string)
# int() converts to 22 (integer)

print(age + 1)       # 23 ✅
print(type(age))     # <class 'int'>


# float

price = float(input("Enter price: "))
# User types: 99.99

print(price * 2)     # 199.98 ✅
print(type(price))   # <class 'float'>

# string

age = 22
message = "I am " + str(age) + " years old"
print(message)       # I am 22 years old ✅

# Converting numbers to string for manipulation
number = 12345
text = str(number)
print(text[0])       # "1" — first digit!
print(len(text))     # 5  — number of digits!


# boolean

# These are FALSY — become False
print(bool(0))        # False
print(bool(""))       # False — empty string
print(bool(None))     # False

# These are TRUTHY — become True
print(bool(1))        # True
print(bool(-5))       # True — any non-zero number
print(bool("hello"))  # True — any non-empty string
print(bool(42))       # True


