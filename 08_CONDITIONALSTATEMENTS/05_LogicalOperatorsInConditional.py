age = 20
has_id = True

# Using 'and' — cleaner than nested if
if age >= 18 and has_id:
    print("Entry allowed ✅")
else:
    print("Entry denied ❌")


# Using 'or'
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend! 🎉")
else:
    print("Back to work 😔")


# Using 'not'
is_raining = False
if not is_raining:
    print("Let's go for a walk! 🚶")