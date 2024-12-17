arr = [15, 8, 31, 47, 2, 19]

total_sum = 0
i = 0

while i < len(arr):
    total_sum += arr[i]
    i += 1

mean = total_sum / len(arr)

print("Array:", arr)
print("Arithmetic mean:", mean)