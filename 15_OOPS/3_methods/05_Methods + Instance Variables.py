# Now we’ll understand:
# 👉 how methods use data from the object

class Student:
    
    def set_data(self, name, age):
        # Assign values to instance variables
        self.name = name
        self.age = age

    def display(self):
        # Access instance variables using self
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student()

s1.set_data("Likith", 21)   # set values
s1.display()                # use values


'''

🧠 Key understanding
self.name → belongs to that specific object
Each object stores its own data
'''