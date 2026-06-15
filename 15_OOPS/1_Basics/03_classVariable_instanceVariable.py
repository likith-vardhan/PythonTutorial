# ==========================================
# CLASS VARIABLES vs INSTANCE VARIABLES
# ==========================================

class Student:
    
    # ✅ CLASS VARIABLE
    # Shared by ALL objects of this class
    school_name = "ABC School"
    
    def __init__(self, name, age):
        # ✅ INSTANCE VARIABLES
        # Each object gets its OWN copy
        self.name = name
        self.age = age


# ==========================================
# CREATING OBJECTS
# ==========================================

s1 = Student("Likith", 21)
s2 = Student("Rahul", 22)

# Both objects share the same class variable initially
print("Initial values:")
print(s1.name, s1.age, s1.school_name)
print(s2.name, s2.age, s2.school_name)


# ==========================================
# MODIFYING CLASS VARIABLE
# ==========================================

# Change class variable using class name
Student.school_name = "XYZ School"

print("\nAfter changing class variable:")
print(s1.name, s1.school_name)  # updated
print(s2.name, s2.school_name)  # updated


# ==========================================
# MODIFYING INSTANCE VARIABLE
# ==========================================

# Change only s1's age
s1.age = 25

print("\nAfter modifying instance variable:")
print(s1.name, s1.age)  # changed
print(s2.name, s2.age)  # unchanged


# ==========================================
# INSTANCE OVERRIDING CLASS VARIABLE
# ==========================================

# ⚠️ This creates a NEW instance variable for s1
# It DOES NOT change the class variable
s1.school_name = "My Private School"

print("\nAfter overriding class variable in s1:")
print("s1 school:", s1.school_name)  # uses instance value
print("s2 school:", s2.school_name)  # still uses class value


# ==========================================
# INTERNAL MEMORY CHECK (__dict__)
# ==========================================

print("\nInspecting internal storage:")

print("s1 __dict__:", s1.__dict__)
# {'name': 'Likith', 'age': 25, 'school_name': 'My Private School'}

print("s2 __dict__:", s2.__dict__)
# {'name': 'Rahul', 'age': 22}

print("Class __dict__ contains school_name:", Student.__dict__['school_name'])
# 'XYZ School'


# ==========================================
# ATTRIBUTE LOOKUP RULE (VERY IMPORTANT)
# ==========================================

# Python follows this order:
# 1. Check inside OBJECT (instance)
# 2. If not found → check CLASS

# So:
# s1.school_name → found in s1 → "My Private School"
# s2.school_name → not in s2 → goes to class → "XYZ School"


# ==========================================
# FINAL SUMMARY (MENTAL MODEL)
# ==========================================

# Class Variable:
# - Shared across all objects
# - Defined outside methods
# - Changed using ClassName.variable

# Instance Variable:
# - Unique for each object
# - Defined using self inside __init__
# - Changed using object.variable

# Key Rule:
# Instance variable OVERRIDES class variable for that object