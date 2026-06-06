num = int(input("Enter a number: "))

if num > 0:
    print("Positive ➕")
elif num < 0:
    print("Negative ➖")
else:
    print("Zero 0️⃣")

    correct_username = "admin"
correct_password = "python123"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Login successful! Welcome 👋")
elif username == correct_username:
    print("Wrong password ❌")
else:
    print("Username not found ❌")

    year = int(input("Enter a year: "))

# A year is a leap year if:
# divisible by 4 AND (not divisible by 100 OR divisible by 400)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year 🗓️")
else:
    print(f"{year} is NOT a Leap Year")





