# 🔹 What is an Instance Method?

# 👉 A method that works with object data (instance variables)
# 👉 It always uses self

class Student:
    
    def __init__(self, name, marks):
        # Instance variables
        self.name = name
        self.marks = marks

    # ✅ Instance Method
    def display(self):
        # Accessing instance variables using self
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Likith", 85)
s2 = Student("Rahul", 90)

s1.display()
s2.display()



'''
class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def update_marks(self, new_marks):
        # Modify instance variable
        self.marks = new_marks

    def display(self):
        print(self.name, self.marks)


s1 = Student("Likith", 85)

s1.display()        # 85
s1.update_marks(95)
s1.display()        # 95
'''

'''


class BankAccount:
    
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)


acc1 = BankAccount(1000)
acc1.deposit(500)
acc1.show_balance()



'''