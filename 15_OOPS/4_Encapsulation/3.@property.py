'''

Problem with Getters/Setters

Accessing data looks like method calls:

e.set_salary(60000)
print(e.get_salary())

Python provides a cleaner way.


'''

# @property

# Turns a method into a read-only attribute.

class Employee:
    def __init__(self):
        self.__salary = 50000

    @property
    def salary(self):
        return self.__salary

e = Employee()
print(e.salary)


# @property + Setter

class Employee:
    def __init__(self):
        self.__salary = 50000

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value

e.salary = 70000
print(e.salary)

'''
Interview Answer

Getter: Method used to access private data.

Setter: Method used to modify private data with validation.

@property: Pythonic way to implement getters and setters while allowing attribute-like access.

'''