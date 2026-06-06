name = input("Enter your name: ")
city = input("Enter your city: ")
print(f"Welcome, {name} from {city}!")


# 

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")


# 

# Get two numbers and do multiple operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Sum:      {a + b}")
print(f"Diff:     {a - b}")
print(f"Product:  {a * b}")
print(f"Division: {a / b:.2f}")   # :.2f = 2 decimal places
print(f"Is sum even? {(a + b) % 2 == 0}")

# 