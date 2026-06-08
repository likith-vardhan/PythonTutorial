# 🔵 2. Class Method
# 👉 Definition:

# A method that works with class-level data, not object data.

# 👉 Key Point:
# Uses @classmethod decorator
# Takes cls as first parameter
# Can access class variables


class Student:
    school = "ABC School"   # class variable

    @classmethod
    def change_school(cls, name):
        cls.school = name

Student.change_school("XYZ School")
print(Student.school)

# 🧠 Important:
# Affects all objects
# Used for shared data