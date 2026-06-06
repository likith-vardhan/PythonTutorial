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