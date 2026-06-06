# 
def outer():
    x = 10

    def inner():
        x = x + 1  # ERROR

    inner()


    # 💥 Why?

# Python thinks x is local to inner(), but it's used before assignment.

def outer():
    x = 10

    def inner():
        nonlocal x
        x = x + 1
        print(x)

    inner()

outer()

# # 🧠 Key Understanding:
# nonlocal = modify variable from enclosing scope
# Without it → Python creates a new local variable
# # 



# 🔁 5. Returning Inner Functions (VERY IMPORTANT)

# This is where things become powerful.

def outer(msg):
    def inner():
        print(msg)
    return inner

f = outer("Hello")
f()
# 🧠 What’s happening?
# outer() finishes
# But inner() still remembers msg

# 👉 This leads to closures (next topic)



# 🔄 6. Inner Functions as Dynamic Behavior

# You can create different behaviors dynamically

def operation(op):
    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    if op == "add":
        return add
    else:
        return mul

f = operation("add")
print(f(2, 3))  # 5
# 🧠 Insight:
# You're returning different inner functions
# This is how frameworks build dynamic logic


# 🧪 7. Inner Functions + Parameters

def outer(a):
    def inner(b):
        return a + b
    return inner

f = outer(10)
print(f(5))






