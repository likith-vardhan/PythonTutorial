# A method that works with object (instance) data.

# 👉 Key Point:
# Takes self as the first parameter
# Can access and modify instance variables

class Student:
    def __init__(self, name):
        self.name = name   # instance variable

    def display(self):    # instance method
        print("Name:", self.name)

s1 = Student("Likith")
s1.display()


# 🧠 Important:
# Each object has its own data
# Instance methods operate on that data

