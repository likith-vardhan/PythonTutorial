# 🔹 What is __init__?

# It is a special method that runs automatically when an object is created.

class Student:
    
    def __init__(self, name, age):
        # Automatically called when object is created
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Likith", 21)   # __init__ runs automatically
s2 = Student("Rahul", 22)

s1.display()
s2.display()