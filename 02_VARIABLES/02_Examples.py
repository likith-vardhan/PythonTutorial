# easy
name = "Ravi"
age = 22
gpa = 8.7
is_student = True

print(name)        # Ravi
print(age)         # 22
print(gpa)         # 8.7
print(is_student)  # True


# medium-Using variables inside print:

name = "Priya"
age = 20
city = "Mumbai"

print("Name:", name)
print("Age:", age)
print("City:", city)

# Even cleaner with f-strings (preview!):
print(f"My name is {name}, I am {age} years old.")
# Output: My name is Priya, I am 20 years old.

# Tricky — Variable reassignment & multiple assignment:

# Reassignment
x = 10
x = x + 5    # Take what's in x (10), add 5, put it back
print(x)     # Output: 15

# Multiple variables in one line
a, b, c = 1, 2, 3
print(a, b, c)   # Output: 1 2 3

# Same value to multiple variables
p = q = r = 0
print(p, q, r)   # Output: 0 0 0
