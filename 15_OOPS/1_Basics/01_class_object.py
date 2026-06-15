# ---------------------------------------------
# Example: Class Attributes vs Object Attributes
# ---------------------------------------------

class SampleClass:
    # Class attributes (shared by all objects)
    attribute1 = 20
    attribute2 = 90


# ---------------------------------------------
# Creating Objects (Instances of the class)
# ---------------------------------------------

obj1 = SampleClass()
obj2 = SampleClass()
obj3 = SampleClass()


# ---------------------------------------------
# Accessing Class Attributes using Objects
# ---------------------------------------------
# Even though attributes belong to the class,
# objects can access them

print("Initial values:")
print(obj1.attribute1)  # 20
print(obj1.attribute2)  # 90


# ---------------------------------------------
# All objects share same class attributes
# ---------------------------------------------

print("\nValues from all objects (before change):")
print(obj1.attribute1)
print(obj2.attribute1)
print(obj3.attribute1)

print(obj1.attribute2)
print(obj2.attribute2)
print(obj3.attribute2)


# ---------------------------------------------
# Modifying attribute via one object
# ---------------------------------------------
# This DOES NOT change the class attribute.
# Instead, it creates a NEW attribute for obj1 only
# (called instance attribute)

obj1.attribute1 = 100


# ---------------------------------------------
# After modification
# ---------------------------------------------

print("\nAfter modifying obj1.attribute1:")

print("obj1.attribute1:", obj1.attribute1)  # 100 (instance attribute)
print("obj2.attribute1:", obj2.attribute1)  # 20 (still class attribute)
print("obj3.attribute1:", obj3.attribute1)  # 20

print("\nAccessing class attribute directly:")
# we cannot change class attributes using objects.
print("SampleClass.attribute1:", SampleClass.attribute1)  # 20