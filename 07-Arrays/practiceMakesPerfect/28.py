# Calculate the sum of the last column
arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

last_column_sum = sum(row[-1] for row in arr)
print(f"Sum of the last column: {last_column_sum}")
