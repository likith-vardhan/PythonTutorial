# 🔬 3. LEGB Rule (Scope Resolution)

'''
When Python sees a variable name, it searches for it in this order:

L → E → G → B


'''

# local

def outer():
    x = 10

    def inner():
        y = 20      # Local to inner
        print(y)

    inner()

outer()
# Here y is found in the Local scope of inner(). 20


# 2. Enclosing Scope (E)
# An inner function can access variables from its outer function.

def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()

'''
Python looks for x:

Local? ❌
Enclosing (outer) ? ✅

So it prints 10.

'''
# global:Variables defined outside all functions

x = 100

def outer():

    def inner():
        print(x)

    inner()

outer()

'''
Search order:

Local? ❌
Enclosing? ❌
Global? ✅

'''

# 4. Built-in Scope (B)

# Python's built-in names.

def outer():

    def inner():
        print(len("hello"))

    inner()

outer()

# complete example

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()



# if local doesnt exist

x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

outer()

# if enclosing doesnt exist

x = "global"

def outer():

    def inner():
        print(x)

    inner()

outer()


 
# global Keyword

# Used when you want to modify a global variable.

x = 10

def outer():

    def inner():
        global x
        x = 50

    inner()

outer()

print(x)

# 50

# Without global, Python would create a local variable.


# nonlocal Keyword (Very Important for Inner Functions)

# Used to modify a variable from the enclosing scope.

def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()

# 20

# Without nonlocal:

def outer():
    x = 10

    def inner():
        x = 20

    inner()
    print(x)

outer()
# Because a new local x is created inside inner().

# interview


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    return inner

counter = outer()

counter()
counter()
counter()

'''
count belongs to outer()
inner() accesses it through the Enclosing scope
nonlocal allows modification
This is the foundation of closures

'''
# ---------------------------------------------------------------------

'''

inner() looks for a variable in:

1. Local      (inside inner)
2. Enclosing  (inside outer)
3. Global     (module level)
4. Built-in   (Python predefined names)

L → E → G → B

'''