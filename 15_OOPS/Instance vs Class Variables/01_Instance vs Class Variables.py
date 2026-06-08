# 🔷 What are Attributes?
# Attributes are variables that belong to a class or object.

# There are two types of attributes:

# 1️⃣ Instance Variables
# - Belong to: Each specific object
# - Defined in: Inside __init__ using self
# - Shared? ❌ No — each object has its own copy

# 2️⃣ Class Variables
# - Belong to: The class itself
# - Defined in: Inside class, outside __init__
# - Shared? ✅ Yes — shared by ALL objects

# instance variables

class Employee:
    def __init__(self, name, salary):
        # Instance variables — different for each employee
        self.name = name
        self.salary = salary

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 70000)

print(emp1.name)    # Alice
print(emp2.name)    # Bob
print(emp1.salary)  # 50000
print(emp2.salary)  # 70000

# Changing one object's attribute does NOT affect others
emp1.salary = 60000
print(emp1.salary)  # 60000
print(emp2.salary)  # 70000 — unchanged!

# class variables

class Employee:
    company_name = "TechCorp"    # Class variable — shared by ALL employees
    employee_count = 0           # Class variable — tracks total employees

    def __init__(self, name, salary):
        self.name = name             # Instance variable
        self.salary = salary         # Instance variable
        Employee.employee_count += 1 # Updating class variable

    def show_info(self):
        print(f"{self.name} works at {Employee.company_name}")
        print(f"Salary: {self.salary}")


emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 70000)
emp3 = Employee("Carol", 60000)

emp1.show_info()   # Alice works at TechCorp
emp2.show_info()   # Bob works at TechCorp

# Class variable is same for all
print(Employee.company_name)     # TechCorp
print(emp1.company_name)         # TechCorp (accessible via object too)
print(emp2.company_name)         # TechCorp

print(f"Total Employees: {Employee.employee_count}")  # 3

# Changing class variable via class name — affects ALL
Employee.company_name = "NewTechCorp"
print(emp1.company_name)   # NewTechCorp
print(emp2.company_name)   # NewTechCorp


# ⚠️ The Tricky Part — When Object Modifies Class Variable

class Demo:
    shared = "I am shared"

d1 = Demo()
d2 = Demo()

print(d1.shared)   # I am shared
print(d2.shared)   # I am shared

# ⚠️ What happens here?
d1.shared = "I am d1's own"   # This CREATES a new instance variable for d1!
                               # It does NOT modify the class variable

print(d1.shared)   # I am d1's own   ← d1 now has its OWN instance variable
print(d2.shared)   # I am shared     ← d2 still uses the class variable
print(Demo.shared) # I am shared     ← class variable unchanged!

# The CORRECT way to modify class variable:
Demo.shared = "Updated for everyone"
print(d1.shared)   # I am d1's own  ← d1 uses its own instance variable (shadow)
print(d2.shared)   # Updated for everyone
print(Demo.shared) # Updated for everyone


# Key Insight: When you do obj.class_var = value, Python creates a new instance variable that shadows the class variable.
#  It does NOT change the class variable.

# 🔷 How Python Looks Up Attributes (Search Order)

# Python looks for an attribute in this order:
# 1. The object's own __dict__ (instance variables)
# 2. The class's __dict__ (class variables)
# 3. Parent class(es) — we'll cover this in Inheritance

# This is called the Attribute Lookup Chain.

class Car:
    wheels = 4   # class variable

    def __init__(self, brand):
        self.brand = brand   # instance variable

my_car = Car("Toyota")

# Python looks in my_car.__dict__ first
print(my_car.__dict__)   # {'brand': 'Toyota'}  ← only instance variables!
print(Car.__dict__)       # {'wheels': 4, '__init__': ..., ...}

print(my_car.brand)    # Found in instance dict ✅
print(my_car.wheels)   # NOT in instance dict → found in class dict ✅
