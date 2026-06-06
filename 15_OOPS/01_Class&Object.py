'''
🔷 What is a Class?

A class is a blueprint or template for creating objects. 
It defines what data (attributes) and behaviors (methods) an object will have.

'''

'''
🔷 What is an Object?

An object is a real instance created from a class. 
It occupies memory and has its own specific data.

'''

# 🔷 WHY do we use Classes and Objects?

# ❌ Without OOP - messy, hard to scale
car1_brand = "Toyota"
car1_speed = 0

car2_brand = "BMW"
car2_speed = 0

def accelerate_car1():
    car1_speed += 10

def accelerate_car2():
    car2_speed += 10

# Imagine managing 100 cars like this... nightmare!


# ✅ With OOP - clean, scalable, reusable

# Define a class (blueprint)
class Dog:
    # This is a class body
    pass   # 'pass' means empty for now

# Create objects (instances) from the class
dog1 = Dog()
dog2 = Dog()

print(type(dog1))   # <class '__main__.Dog'>
print(dog1)         # <__main__.Dog object at 0x...> (memory address)
print(dog1 is dog2) # False — they are DIFFERENT objects in memory






















