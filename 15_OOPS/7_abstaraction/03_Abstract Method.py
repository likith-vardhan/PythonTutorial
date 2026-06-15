from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5


class Rectangle(Shape):
    def area(self):
        return 10 * 5


c = Circle()
r = Rectangle()

print(c.area())
print(r.area())




# ----------------------------------------------------

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


methods = [CreditCard(), UPI()]

for m in methods:
    m.pay(1000)



# -----------------------------------------------------------------------------

# 9. Abstract Class with Constructor


from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass


class Engineer(Person):
    def work(self):
        print(self.name, "is coding")

p = Engineer("Likith")
p.work()    

# ------------------------------------------------------------------------------

# 10. Multiple Abstract Methods


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")



        # ------------------------------------------------------


        from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fuel_type(self):
        pass


class PetrolCar(Vehicle):
    def fuel_type(self):
        print("Uses Petrol")


class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Uses Electricity")


vehicles = [PetrolCar(), ElectricCar()]

for v in vehicles:
    v.fuel_type()  

    #  real example

    