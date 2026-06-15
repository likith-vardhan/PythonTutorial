class Demo:
    
    # This is a METHOD (function inside class)
    def say_hello(self):
        print("Hello!")
    

obj = Demo()        # create object
obj.say_hello()     # call method



# 🔍 Important Concepts (very important)
# 1. Why self is there?

'''
def say_hello(self):
self refers to the current object
Python automatically passes it when you call:
obj.say_hello()

Internally, Python does:

Demo.say_hello(obj)


'''

class Car:
    
    def start(self):
        print("Car started")

c1 = Car()
c1.start()