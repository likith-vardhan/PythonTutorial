matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access single element — [row][column]
print(matrix[0][0])    # 1 — row 0, col 0
print(matrix[1][2])    # 6 — row 1, col 2
print(matrix[2][1])    # 8 — row 2, col 1

# Loop through nested list
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9