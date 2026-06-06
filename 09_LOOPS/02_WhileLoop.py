count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1        # ← CRITICAL: update the variable!

print("Done!")
# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
# Done!


password = ""

while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Wrong! Try again.")

print("Access granted! ✅")