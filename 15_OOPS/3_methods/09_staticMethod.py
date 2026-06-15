# )
# 🔹 What is a Static Method?

# 👉 A method that does NOT use self or cls
# 👉 Works like a normal function, but kept inside the class
# 👉 Used for utility / helper logic

class Student:
    
    def __init__(self, marks):
        self.marks = marks

    # ✅ Static Method
    @staticmethod
    def is_pass(marks):
        # No self, no cls
        # Just logic
        return marks >= 40

s1 = Student(85)
s2 = Student(30)

print(Student.is_pass(s1.marks))  # True
print(Student.is_pass(s2.marks))  # False



'''
🔍 Key Observation
Static method does not care about object or class
It only uses the data you pass

'''