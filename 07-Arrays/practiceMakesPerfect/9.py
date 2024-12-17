def compare(array1, array2):
    # Check if both arrays have the same length
    if len(array1) != len(array2):
        return False
    
    # Check if elements at corresponding positions are the same
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

array1_1 = ["water", "book", "sky"]
array2_1 = ["water", "book", "sky"]
print(compare(array1_1, array2_1))

array1_2 = [True, False]
array2_2 = [True, False, True]
print(compare(array1_2, array2_2))

array1_3 = [5, 3, 1]
array2_3 = [5, 3, 1]
print(compare(array1_3, array2_3))

array1_4 = [3, 2, 1]
array2_4 = [3, 2]
print(compare(array1_4, array2_4))
