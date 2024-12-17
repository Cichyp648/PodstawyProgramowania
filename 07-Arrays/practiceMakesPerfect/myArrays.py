def second_largest(arr):
    if len(arr) < 2:
        return None
    unique_sorted_arr = sorted(set(arr), reverse=True)
    return unique_sorted_arr[1]

def range_difference(arr):
    return max(arr) - min(arr)

def median(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        return sorted_arr[mid]

def min_max(arr):
    return [min(arr), max(arr)]

def array_to_string(arr):
    result = ""
    for num in arr:
        result += str(num) + "-"
    return result[:-1] # Remove last '-'