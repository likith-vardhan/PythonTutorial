names = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

print("Names:", names)
print("Sorted:", sorted(names))


# Find average of scores:
pythonscores = [85, 92, 78, 96, 88, 74, 90]

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

print(f"Total:   {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest:  {lowest}")

# Remove duplicates while preserving order:
pythonnumbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

seen = []
for num in numbers:
    if num not in seen:
        seen.append(num)

print(seen)    # [3, 1, 4, 5, 9, 2, 6]