# Array of values
arr = [15, 8, 31, 47, 2, 19]

# Initialize sum
total_sum = 0

# Calculate sum of the array
for num in arr:
    total_sum += num

# Calculate arithmetic mean
mean = total_sum / len(arr)

print("Array:", arr)
print("Arithmetic mean:", mean)