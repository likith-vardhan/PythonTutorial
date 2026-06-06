# Local Scope
# Variables created inside a function only exist inside it:

def my_function():
    x = 10          # local variable — only exists inside function
    print(x)

my_function()       # 10
print(x)            # ❌ NameError! x doesn't exist outside

# Global Scope
# Variables created outside all functions:


x = 100             # global variable

def my_function():
    print(x)        # ✅ can READ global variable

my_function()       # 100
print(x)            # 100


# The global keyword

count = 0

def increment():
    global count        # tell Python: use the GLOBAL count
    count += 1

increment()
increment()
increment()
print(count)            # 3


'''
LEGB Rule — How Python finds variables
Python searches in this order:
L — Local (inside current function)
E — Enclosing (outer function, for nested functions)
G — Global (module level)
B — Built-in (Python's built-in names like print, len)

'''

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)      # local — finds local first

    inner()
    print(x)          # enclosing

outer()
print(x)              # global


