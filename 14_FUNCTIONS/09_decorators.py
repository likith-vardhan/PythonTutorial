'''
A decorator is:

A function that modifies or extends another function’s behavior without changing its code


'''

def decorator(func):
    def wrapper():
        print("i am about to execute a function.......")
        func()
        print("i have executed this function..........")
    return wrapper

    def say_hello():
        print("hello!")

f=decorator(say_hello)
f()

'''

say_hello ───────┐
                 ↓
          decorator(func)
                 ↓
          creates wrapper
                 ↓
   wrapper remembers say_hello (closure)
                 ↓
              return wrapper
                 ↓
                f
                 ↓
               f()
                 ↓
     wrapper() executes
         ↓       ↓
   print     say_hello()
                 ↓
             "Hello!"

'''
def decorator(func):
    def wrapper():
        print("I am about to execute a function.......")
        func()
        print("I have executed this function..........")
    return wrapper

@decorator
def say_hello():
    print("hello!")

say_hello()

# f=decorator(say_hello)
# f()

# decorators using arguments

def greet_decorator(name):
    def decorator(func):
        def wrapper():
            print(f"Hello {name}, before function execution")
            func()
            print(f"Goodbye {name}, after function execution")
        return wrapper
    return decorator

@greet_decorator("Likith")
def say_hello():
    print("Inside function")

say_hello()






