class Grandparent:
    def house(self):
        print("Owns house")

class Parent(Grandparent):
    def car(self):
        print("Owns car")

class Child(Parent):
    def bike(self):
        print("Owns bike")