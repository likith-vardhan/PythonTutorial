# What is a Function?
# A function is a named, reusable block of code that performs a specific task.

# Without functions:
# Calculating area 3 times — repetitive!

area1 = 5 * 3
area2 = 10 * 4
area3 = 7 * 6

# With functions:

def calculate_area(length, width):
    return length * width

area1 = calculate_area(5, 3)
area2 = calculate_area(10, 4)
area3 = calculate_area(7, 6)


# PART 1: Defining & Calling Functions
# Basic Structure

def function_name(parameters):
    """Docstring — describes what function does"""
    # code block
    return value

# ==================================================


# Define
def greet():
    print("Hello, World!")

# Call
greet()        # Hello, World!
greet()        # Hello, World! — reuse as many times!
greet()        # Hello, World!

# 💡 def tells Python: "I'm defining a reusable block of code."
# The function does nothing until you call it.