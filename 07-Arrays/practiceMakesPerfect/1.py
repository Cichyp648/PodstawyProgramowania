# Array of integers
arr = [34, 7, 19, 4, 21, 8]

# Initialize variables
count_even = 0
i = 0

# While loop to check for even values
while i < len(arr):
    if arr[i] % 2 == 0:  # Check if even
        count_even += 1
    i += 1

# Print result
print("Number of even values in the array:", count_even)
