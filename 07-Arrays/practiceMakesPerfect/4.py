arr = [-15, 8, -31, 47, -2, 19]

max_value = arr[0]
min_value = arr[0]

for num in arr:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Array:", arr)
print("Maximum number:", max_value)
print("Minimum number:", min_value)
