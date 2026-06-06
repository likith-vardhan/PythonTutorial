# A function that remembers variables from its outer scope even after that outer function has finished execution
# 

'''

🔑 2. The 3 Conditions for a Closure

For a closure to exist:

There must be a nested function
The inner function must use a variable from outer function
The outer function must return the inner function


'''
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(3))  # 8