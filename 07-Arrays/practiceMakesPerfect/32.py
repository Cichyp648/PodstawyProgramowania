arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Print array before swap
print("Before swap:")
for row in arr:
    print(row)

# Swap the first and last rows
arr[0], arr[-1] = arr[-1], arr[0]

# Print array after swap
print("\nAfter swap:")
for row in arr:
    print(row)
