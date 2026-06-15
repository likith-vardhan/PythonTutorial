class Employee:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

e = Employee()
print(e.get_salary())



# Setter

# Used to modify a private attribute with validation.
# 

class Employee:
    def __init__(self):
        self.__salary = 50000

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

e.set_salary(60000)

# Problem with Getters/Setters

# Accessing data looks like method calls:


