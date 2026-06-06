# break-Exit the loop immediately

for i in range(1, 10):
    if i == 5:
        break           # Stop the loop when i is 5
    print(i)

# Output: 1 2 3 4
# 5 is never printed — loop exits before that

# continue- Skip this iteration, keep going

for i in range(1, 8):
    if i == 4:
        continue        # Skip 4, keep going
    print(i)

# Output: 1 2 3 5 6 7
# 4 is skipped but loop continues

# pass- Do nothing (placeholder)

for i in range(5):
    if i == 3:
        pass            # Do nothing, just move on
    print(i)

# Output: 0 1 2 3 4
# pass literally does nothing — used as a placeholder


# else-with loops
# A loop can have an else block — it runs only if the loop completed without hitting break:

# Searching for a number
for i in range(1, 6):
    if i == 7:
        print("Found 7!")
        break
else:
    print("7 not found in range")   # Runs because break was never hit

# Output: 7 not found in range

