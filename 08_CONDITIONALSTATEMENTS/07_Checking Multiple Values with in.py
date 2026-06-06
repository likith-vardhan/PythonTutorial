day = "Monday"

# Without 'in' — messy
if day == "Monday" or day == "Tuesday" or day == "Wednesday":
    print("Weekday")

# With 'in' — clean ✅
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Weekday")
else:
    print("Weekend")