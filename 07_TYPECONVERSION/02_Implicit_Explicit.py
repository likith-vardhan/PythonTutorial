# explicit

x = int("42")        # You explicitly asked for conversion
y = float(10)        # 10 → 10.0


# implicit

result = 10 + 3.5    # int + float → Python auto-converts to float
print(result)        # 13.5
print(type(result))  # <class 'float'>


#  
age = int(input("Enter age: "))
# What if user types "hello" instead of a number?
# → ValueError: invalid literal for int() with base 10: 'hello'

