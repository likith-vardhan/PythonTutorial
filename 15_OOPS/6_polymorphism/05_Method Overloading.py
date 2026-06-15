# Python does NOT support true method overloading.

class Test:
    def add(self, a):
        print(a)

    def add(self, a, b):
        print(a + b)


# 👉 Second method overrides first


# alternative

class Test:
    def add(self, a=None, b=None):
        if a and b:
            print(a + b)
        else:
            print(a)

# super()

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")