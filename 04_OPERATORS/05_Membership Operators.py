name = "Bengaluru"

print("Benga" in name)       # True  — "Benga" exists inside "Bengaluru"
print("Mumbai" in name)      # False — "Mumbai" not in "Bengaluru"
print("Delhi" not in name)   # True  — "Delhi" is indeed not there



price = 500
discount = 50
final = price - discount
print("Final price:", final)   # Final price: 450



marks = 85
total = 100

percentage = (marks / total) * 100
print(f"Percentage: {percentage}%")    # Percentage: 85.0%
print(f"Passed: {percentage >= 35}")   # Passed: True


# Python follows BODMAS / PEMDAS
result = 2 + 3 * 4       # 3*4 first, then +2
print(result)             # 14, NOT 20!

result = (2 + 3) * 4     # brackets first
print(result)             # 20

result = 2 ** 3 ** 2      # right to left for **
print(result)             # 2**9 = 512, NOT 8**2 = 64!

# Always use brackets when in doubt
result = (2 ** 3) ** 2
print(result)             # 64
