# 🔷 Think Like This (Real-Life Analogy)

# Imagine:

# 👨‍💼 All employees in a company have:
# name
# salary

# 👉 These are COMMON (shared by everyone)

# 👨‍💻 But Developers also have:
# programming_language
# 👨‍💼 Managers also have:
# team_size

# 👉 These are NOT common (specific to each role)

# Parent class (COMMON data)

class Product:
    def __init__(self, name, price):
        print("Product constructor called")
        self.name = name
        self.price = price

    def show_details(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")


# Child class 1 (Mobile)
class Mobile(Product):
    def __init__(self, name, price, brand, ram):
        print("Mobile constructor called")

        # Call parent constructor (COMMON)
        super().__init__(name, price)

        # Child-specific data
        self.brand = brand
        self.ram = ram

    def show_details(self):
        super().show_details()
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}")


# Child class 2 (Laptop)
class Laptop(Product):
    def __init__(self, name, price, brand, processor):
        print("Laptop constructor called")

        # Call parent constructor
        super().__init__(name, price)

        self.brand = brand
        self.processor = processor

    def show_details(self):
        super().show_details()
        print(f"Brand: {self.brand}")
        print(f"Processor: {self.processor}")


# Creating objects
m1 = Mobile("iPhone 14", 70000, "Apple", "6GB")
print("-----")
l1 = Laptop("Dell XPS", 120000, "Dell", "i7")

print("\nMobile Details:")
m1.show_details()

print("\nLaptop Details:")
l1.show_details()
