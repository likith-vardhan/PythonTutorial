# Higher Order Function

# 🧠 1. Core Idea (Understand This First)

# A Higher-Order Function is any function that:

# 👉 Takes a function as input
# 👉 OR returns a function

# 🧪 1. Functions as Arguments

def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

print(apply_function(square, 5))  # 25


'''

▶️ Step 1: Function Definitions
1. def square(x):
   Python creates a function object named square
   It stores it in memory

2. def apply_function(func, value):
   Python creates another function object apply_function

👉 Nothing runs yet — only definitions

▶️ Step 2: Function Call Begins

apply_function(square, 5)

🧠 What happens:
square (function itself, not result) is passed as func
5 is passed as value

So internally:

func = square
value = 5

▶️ Step 3: Inside apply_function
return func(value)

Now replace:

return square(5)

▶️ Step 4: Call square(5)
def square(x):
    return x * x
x = 5
returns → 5 * 5 = 25

▶️ Step 5: Return Back
square(5) → returns 25
apply_function returns 25
▶️ Step 6: Print
print(25)

👉 Output:

25

'''





# 🔁 5. Returning Functions

def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
print(double(5))  # 10

# 🔬 Step 1: Function Definition Phase
# Python creates a function object named multiplier
# double = multiplier(2)
# Inside multiplier:
# n = 2

# 🧩 Step 3: Inner Function Creation

'''

multiplier(2)
     ↓
n = 2
     ↓
create multiply(x)
     ↓
attach memory: n = 2
     ↓
return multiply
     ↓
double = multiply (with memory)
     ↓
double(5)
     ↓
multiply(5)
     ↓
5 * 2 = 10


'''