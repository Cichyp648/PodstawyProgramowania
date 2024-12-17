arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

# Finding numbers that are in arr1 but not in arr2
result = []
for num in arr1:
    if num not in arr2:
        result.append(num)

print("Numbers in the first array that are not in the second array:")
for num in result:
    print(num, end=" ")
