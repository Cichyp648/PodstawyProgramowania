# Program to separate even and odd numbers
arr = [7, 9, 2, 4, 5, 6]

evens = [num for num in arr if num % 2 == 0]
odds = [num for num in arr if num % 2 != 0]

sorted_arr = evens + odds

print("Original array:", arr)
print("Evens first:", sorted_arr)
