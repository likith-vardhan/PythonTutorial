class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"❌ Insufficient funds! Available: ₹{self.balance}")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

    def get_balance(self):
        print(f"💰 {self.owner}'s balance: ₹{self.balance}")


# Creating two completely independent accounts
account1 = BankAccount("Rahul", 5000)
account2 = BankAccount("Priya")   # default balance = 0

account1.deposit(2000)     # ✅ Deposited ₹2000. New balance: ₹7000
account1.withdraw(1000)    # ✅ Withdrew ₹1000. Remaining balance: ₹6000
account1.withdraw(10000)   # ❌ Insufficient funds! Available: ₹6000

account2.deposit(500)      # ✅ Deposited ₹500. New balance: ₹500
account1.get_balance()     # 💰 Rahul's balance: ₹6000
account2.get_balance()     # 💰 Priya's balance: ₹500

# account1 and account2 are completely INDEPENDENT
# Changing one does NOT affect the other







# ------------------------------------------------------------

# MISTAKE 1: Forgetting 'self' in method definition
class Cat:
    def meow():        # ❌ Missing self!
        print("Meow")

c = Cat()
c.meow()   # TypeError: meow() takes 0 positional arguments but 1 was given
            # Python tries to pass 'c' as self automatically!

# FIX:
class Cat:
    def meow(self):   # ✅ Always include self
        print("Meow")

# -------------------------------------------------------

# MISTAKE 2: Calling __init__ manually
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Buddy")
d.__init__("Max")   # ❌ Don't do this! Creates bugs.
                    # __init__ is called automatically

# -------------------------------------------------------

# MISTAKE 3: Confusing class and object
class Car:
    def drive(self):
        print("Driving!")

Car.drive()   # ❌ TypeError — you need an object, not the class itself

my_car = Car()
my_car.drive()   # ✅ Correct

# -------------------------------------------------------

# MISTAKE 4: Not using self to store attributes
class Person:
    def __init__(self, name):
        name = name    # ❌ This is a LOCAL variable, lost after __init__ ends!
        # self.name = name   ← This is what you SHOULD do

p = Person("Alice")
# print(p.name)   # AttributeError: 'Person' object has no attribute 'name'