def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

arrays = [
    [5, 3, 8, 6, 7],
    [9, 1, 4, 2, 10],
    [12, 45, 23, 8, 1, 0]
]

for arr in arrays:
    print("Original array:", arr)
    sorted_array = bubblesort(arr.copy())
    print("Sorted array:", sorted_array, "\n")