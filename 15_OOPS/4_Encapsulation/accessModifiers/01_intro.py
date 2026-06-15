# 1. Access in the same class

class Student:
    def __init__(self):
        self.name = "Alice"   # public data

    def show(self):
        print(self.name)      # accessing in same class

s = Student()
s.show()
# alice
# The method show() accesses the public attribute name inside the same class.

# 2. Access by object

class Student:
    def __init__(self):
        self.name = "Alice"

s = Student()

# Accessing public data through object
print(s.name)


# 3. Access from subclass

class Student:
    def __init__(self):
        self.name = "Alice"

class GraduateStudent(Student):
    def display(self):
        print(self.name)   # accessing inherited public attribute

g = GraduateStudent()
g.display()


# 4. Access by subclass object

class Student:
    def __init__(self):
        self.name = "Alice"

class GraduateStudent(Student):
    pass

g = GraduateStudent()

# Accessing through subclass object
print(g.name)

# The object of the subclass can directly access the inherited public attribute.



class Parent:
    def __init__(self):
        self.data = "Public Data"

    def same_class_access(self):
        print("Same class:", self.data)

class Child(Parent):
    def subclass_access(self):
        print("Subclass:", self.data)

# Parent object
p = Parent()
p.same_class_access()        # same class
print("By object:", p.data)  # by object

# Child object
c = Child()
c.subclass_access()          # from subclass
print("Subclass object:", c.data)  # by subclass object


# --------------------------------------------------------------------------------------------------------------------------------------



# In Python, protected is only a convention, not a strict access restriction like in C++.

# A protected attribute is written with a single underscore (_) before its name.

class Parent:
    def __init__(self):
        self._data = 100   # protected attribute

class Child(Parent):
    def show(self):
        print(self._data)  # Accessible in derived class

c = Child()
c.show()


# Accessing from outside the class

# Although _data is considered protected, Python does not prevent access:

class Parent:
    def __init__(self):
        self._data = 100

obj = Parent()

print(obj._data)   # Works, but not recommendedte