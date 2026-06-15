# what is  inheritance in python?

# Inheritance is an Object-Oriented Programming (OOP) concept
#  where one class (child) acquires properties and behaviors (methods) of another class (parent)


# 🔹 Why use inheritance?
# Code reuse
# Reduce redundancy
# Improve maintainability
# Enable hierarchical design
# Supports polymorphism

class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def display(self):
        print("This is child class")

obj = Child()
obj.show()     # inherited
obj.display()  # own method