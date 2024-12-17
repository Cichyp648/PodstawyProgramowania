arr = [2, 3, 2, 5, 8, 1, 9, 8]

# Finding unique elements
unique_elements = []
for num in arr:
    if arr.count(num) == 1:
        unique_elements.append(num)

print("Array:", arr)
print("Unique elements:", end=" ")
for num in unique_elements:
    print(num, end=" ")