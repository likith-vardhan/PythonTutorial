# 🔹 What is a Class Method?

# 👉 A method that works with class-level data (shared data)
# 👉 Uses cls instead of self
# 👉 Defined using @classmethod


class Student:
    
    school_name = "ABC School"   # Class variable
    
    def __init__(self, name):
        self.name = name

    # ✅ Class Method
    @classmethod
    def change_school(cls, new_name):
        # 'cls' refers to the class itself
        cls.school_name = new_name


s1 = Student("Likith")
s2 = Student("Rahul")

print("Before change:")
print(s1.school_name)
print(s2.school_name)

# Change class variable using class method
Student.change_school("XYZ School")

print("\nAfter change:")
print(s1.school_name)
print(s2.school_name)



class Employee:
    
    company = "TechCorp"
    
    def __init__(self, name):
        self.name = name

    @classmethod
    def update_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Likith")
e2 = Employee("Rahul")

Employee.update_company("AI Solutions")

print(e1.company)  # AI Solutions
print(e2.company)  # AI Solutions