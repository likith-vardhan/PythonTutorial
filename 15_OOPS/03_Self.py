# self is the reference to the current object calling the method. 
# It's how Python knows which object's data to use.

class Student:
    def __init__(self, name):
        self.name = name   # THIS student's name

    def greet(self):
        print(f"Hi, I am {self.name}")  # THIS student's name

s1 = Student("Alice")
s2 = Student("Bob")

# Internally Python translates:
# s1.greet()  →  Student.greet(s1)
# s2.greet()  →  Student.greet(s2)

s1.greet()   # Hi, I am Alice
s2.greet()   # Hi, I am Bob



# Key Rule: self is always the first parameter of any instance method.
# Python passes it automatically — you never pass it manually.

