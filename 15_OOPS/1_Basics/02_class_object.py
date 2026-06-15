# Demonstration of Class Attributes vs Instance Attributes

class SampleClass:
    # Class attributes (shared by all instances)
    attribute1 = 10
    attribute2 = 20


# Creating objects (instances)
obj1 = SampleClass()
obj2 = SampleClass()
obj3 = SampleClass()


# ⚠️ This creates an INSTANCE attribute for obj1
# It does NOT change the class attribute
obj1.attribute1 = 100

# At this point:
# obj1.attribute1 → 100 (instance attribute)
# obj2.attribute1 → 10 (class attribute)
# obj3.attribute1 → 10 (class attribute)


# ⚠️ Now we change the CLASS attribute
SampleClass.attribute1 = 1

# Now:
# obj2.attribute1 → 1 (updated class attribute)
# obj3.attribute1 → 1 (updated class attribute)
# obj1.attribute1 → still 100 (because it has its own instance copy)


# Printing values
print("obj1.attribute1:", obj1.attribute1)  # 100
print("obj2.attribute1:", obj2.attribute1)  # 1
print("obj3.attribute1:", obj3.attribute1)  # 1


# 🔍 Important concept:
# Python checks attributes in this order:
# 1. Instance (object) namespace
# 2. Class namespace

# Since obj1 already has its own 'attribute1',
# it does NOT look at the class attribute anymore.


'''
🧠 Why obj1 prints 100?

Because Python follows this lookup order:

Check inside the object (instance)
If not found → check class

So for obj1:

It finds attribute1 = 100 inside itself ✅
It never goes to the class

'''