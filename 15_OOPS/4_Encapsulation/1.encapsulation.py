# Step 1: Creating a Simple Class

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("John")

print(p1.name)


# self.name

# is an attribute.

# Currently anyone can change it:

p1.name = "Mike"


'''
What Is Encapsulation Here?

The data:
and behavior:

are bundled together inside a class.

This itself is the basic idea of encapsulation.

'''

# --------------------------------------------------------------------

# Access Modifiers in Python

# Unlike languages such as Java or C++, Python does not have strict access modifiers.

# Instead, Python uses naming conventions.

# There are three levels:


# | Type      | Syntax   |
# | --------- | -------- |
# | Public    | `name`   |
# | Protected | `_name`  |
# | Private   | `__name` |


# public

class Student:
    def __init__(self):
        self.name = "Alice"


s = Student()

print(s.name)

s.name = "Bob"
print(s.name)

# Public attributes are completely open.

# When to Use Public?

# Use public when:

# Data is safe to access
# No validation is needed
# You don't mind users changing it


# 2. Protected Members

# Protected members start with a single underscore

# _name

class Employee:
    def __init__(self):
        self._salary = 50000

e = Employee()

print(e._salary)

'''

Output: 50000


It still works.

So why call it protected?

Because it is a convention.

It tells other programmers:

"This is intended for internal use.

Don't access it unless necessary."

'''

# Protected Example with Inheritance

class Parent:
    def __init__(self):
        self._message = "Hello"

class Child(Parent):
    def show(self):
        print(self._message)

c = Child()
c.show()

# Protected members are commonly used by child classes.


# 3. Private Members

# Private members start with double underscores.

# __name

class BankAccount:
    def __init__(self):
        self.__balance = 1000

account = BankAccount()

print(account.__balance)

# AttributeError

# You cannot access it directly.



# Why Private Members?

# Suppose balance should only change through deposit or withdrawal.


class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)


acc = BankAccount()

acc.deposit(500)

acc.show_balance()

# The balance is protected from direct modification



'''

How Private Actually Works

Python uses something called Name Mangling.

When you write:

self.__balance

Python internally changes it to:

self._BankAccount__balance

Example:

class BankAccount:
    def __init__(self):
        self.__balance = 1000

Usage:

acc = BankAccount()

print(acc._BankAccount__balance)

Output:

1000

So Python's private is not absolute security.

It is designed to prevent accidental access.

Name Mangling Demonstration
class Demo:
    def __init__(self):
        self.__secret = "Python"

Check attributes:

d = Demo()

print(dir(d))

You will see something like:

_Demo__secret

This is name mangling.


'''



# ---------------------------------------------------------------

'''

Example: Encapsulation with Methods

Without encapsulation:

class BankAccount:
    def __init__(self):
        self.balance = 1000

acc = BankAccount()

acc.balance = -5000   # Invalid
print(acc.balance)

Output:

-5000

Problem:
Anyone can set an invalid balance.



'''

# Encapsulation Using Methods

class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


acc = BankAccount()

acc.deposit(500)
acc.withdraw(200)

print(acc.get_balance())





























