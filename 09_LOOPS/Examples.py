n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum of 1 to {n} = {total}")
# Enter n: 10 → Sum of 1 to 10 = 55

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")

    # pattern



# Right-angled triangle pattern
rows = 5

for i in range(1, rows + 1):
    print("* " * i)

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *


# Number pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *