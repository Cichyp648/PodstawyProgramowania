def is_subset(arr1, arr2):
    return set(arr1).issubset(arr2)

arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]

# Check if arr1 is a subset of arr2
result = is_subset(arr1, arr2)

print("Array1:", arr1)
print("Array2:", arr2)
print("Array1 is a subset of Array2:", result)
