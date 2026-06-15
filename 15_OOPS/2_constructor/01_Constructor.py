# 🔥 1. What is a Constructor?

# A constructor is a special method that is automatically called when an object is created.

# __init__()

class Student:
    def __init__(self):
        print("Constructor is called")

s1 = Student() 
# Constructor is called

# ✔ Automatically runs when object is created
# ✔ Used to initialize object data

# 🧠 2. Why Do We Need Constructors?

# Without constructors:

# You must manually assign values
# Code becomes repetitive and error-prone

# With constructors:

# Initialize values instantly
# Cleaner, reusable, structured code

# Default Constructor :No parameters except self


class Car:
    def __init__(self):
        self.brand = "Tesla"
        self.price = 50000

    def show(self):
        print(self.brand, self.price)

c1 = Car()
c1.show()

# Parameterized Constructor

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show(self):
        print(self.brand, self.price)

c1 = Car("BMW", 80000)
c2 = Car("Audi", 70000)

c1.show()
c2.show()


# self

# ⚙️ 4. Understanding self

# This is VERY IMPORTANT

# 👉 self refers to the current object

class Demo:
    def __init__(self, value):
        self.value = value

d1 = Demo(10)
d2 = Demo(20)

print(d1.value)  # 10
print(d2.value)  # 20

# ✔ Each object has its own copy of data


# 🧪 5. Constructor Flow (Internally)

# When you write:

# obj = MyClass()

# Python internally does:

# Calls __new__() → creates object
# Calls __init__() → initializes object


# 🧬 6. __new__() vs __init__()
# 🔹 __new__() → creates object
# 🔹 __init__() → initializes object
class Demo:
    def __new__(cls):
        print("1. __new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("2. __init__ called")

d = Demo()

# Output:
# 1. __new__ called
# 2. __init__ called


# 🧱 7. Constructor with Default Values
class Employee:
    def __init__(self, name="Unknown", salary=0):
        self.name = name
        self.salary = salary

e1 = Employee()
e2 = Employee("Likith", 50000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)






































# 🔁 8. Constructor Overloading (Important Concept)

# ❌ Python does NOT support traditional overloading

# ✔ But you can simulate it:

# Method 1: Default arguments

class Demo:
    def __init__(self, a=None):
        if a is None:
            print("No value")
        else:
            print("Value:", a)

d1 = Demo()
d2 = Demo(10)

# Method 2: *args
class Demo:
    def __init__(self, *args):
        print("Arguments:", args)

Demo()
Demo(1)
Demo(1, 2, 3)





















# 🧬 9. Constructor in Inheritance
# 🔹 Parent constructor is NOT automatically called

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        print("Child constructor")

c = Child()

# Output:
# Child constructor


# ✅ Calling Parent Constructor

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

c = Child()

# Output:
# Parent constructor
# Child constructor



# 🔄 10. Constructor Chaining

# Calling one constructor from another

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")

c = C()

# Output:
# A
# B
# C




# 
























class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


acc1 = BankAccount("Likith", 10000)

acc1.show()
acc1.deposit(5000)
acc1.withdraw(3000)
acc1.show()