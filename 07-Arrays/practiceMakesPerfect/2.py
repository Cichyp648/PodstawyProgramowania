arr = [15, 8, 31, 47, 2, 19]

print("Existed array:", end=" ")
for value in arr:
    print(value, end=" ")

# Print the array in reverse order
print("\nReverse array:", end=" ")
for i in range(len(arr) - 1, -1, -1):  # Iterate in reverse
    print(arr[i], end=" ")
