# Array of integer numbers
arr = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

smallest_value = 0.0
largest_value = 0.0
smallest_pos = (0, 0)
largest_pos = (0, 0)

# Find smallest and largest values
for row_index, row in enumerate(arr):
    for col_index, value in enumerate(row):
        if value < smallest_value:
            smallest_value = value
            smallest_pos = (row_index, col_index)
        if value > largest_value:
            largest_value = value
            largest_pos = (row_index, col_index)

print(f"Smallest value: {smallest_value} at position {smallest_pos}")
print(f"Largest value: {largest_value} at position {largest_pos}")
