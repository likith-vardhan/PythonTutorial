# Normal way
age = 20
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Shorthand (ternary) way
status = "Adult" if age >= 18 else "Minor"
print(status)    # Adult