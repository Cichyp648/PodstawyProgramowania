arr = [8, 2, 5, 1, 9]
print('Original array:', arr)

for elem in range(len(arr)):
    arr[elem] = arr[elem] ** 2

print('Power of 2:', arr)