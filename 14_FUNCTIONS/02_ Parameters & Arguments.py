# Parameter = variable name in the function definition
# Argument = actual value you pass when calling


def greet(name):          # 'name' is the PARAMETER
    print(f"Hello, {name}!")

greet("Ravi")             # "Ravi" is the ARGUMENT
greet("Priya")
# Output:
# Hello, Ravi!
# Hello, Priya!


# Type 1: Positional Arguments
# Order matters — values are matched by position:

def describe(name, age, city):
    print(f"{name} is {age} years old from {city}")

describe("Ravi", 22, "Bengaluru")    # ✅ correct order
describe(22, "Ravi", "Bengaluru")    # ❌ wrong — 22 goes to name

# Type 2: Keyword Arguments
# Order doesn't matter — you name each argument:

def describe(name, age, city):
    print(f"{name} is {age} years old from {city}")

describe(age=22, city="Bengaluru", name="Ravi")   # ✅ any order!
describe(name="Priya", age=21, city="Mumbai")      # ✅


# Type 3: Default Arguments
# Provide a fallback value if argument is not passed:

def greet(name, message="Hello"):    # message has a default
    print(f"{message}, {name}!")

greet("Ravi")                  # Hello, Ravi!      — uses default
greet("Priya", "Good morning") # Good morning, Priya! — overrides default
greet("Arjun", message="Hi")   # Hi, Arjun!


# ⚠️ Rule: Default parameters must always come after non-default ones!

# def greet(message="Hello", name):   # ❌ SyntaxError!
# def greet(name, message="Hello"):   # ✅ correct



# Type 4: *args — Variable Positional Arguments
# When you don't know how many arguments will be passed:

def add_all(*args):
    print(args)           # It's a TUPLE of all passed values
    return sum(args)

print(add_all(1, 2, 3))          # 6
print(add_all(10, 20, 30, 40))   # 100
print(add_all(5))                # 5

def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")

greet_all("Ravi", "Priya", "Arjun", "Sneha")
# Hello, Ravi!
# Hello, Priya!
# Hello, Arjun!
# Hello, Sneha!


# Type 5: **kwargs — Variable Keyword Arguments
# When you don't know what keyword arguments will be passed:

def display_info(**kwargs):
    print(kwargs)          # It's a DICT of all passed key=value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Ravi", age=22, city="Bengaluru")
# {'name': 'Ravi', 'age': 22, 'city': 'Bengaluru'}
# name: Ravi
# age: 22
# city: Bengaluru



# combining all 

# Order must always be:
# regular → *args → keyword defaults → **kwargs

def mega_function(name, age, *hobbies, country="India", **extra):
    print(f"Name: {name}, Age: {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Country: {country}")
    print(f"Extra: {extra}")

mega_function("Ravi", 22, "cricket", "coding", "chess",
              country="India", job="developer", level="senior")
# Name: Ravi, Age: 22
# Hobbies: ('cricket', 'coding', 'chess')
# Country: India
# Extra: {'job': 'developer', 'level': 'senior'}