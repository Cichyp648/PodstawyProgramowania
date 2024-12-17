# Function to check if a number occurs in an array
def occurs(number, array):
    for value in array:
        if value == number:
            return True
    return False

arr = [15, 38, 7, 23, 14]
number = int(input("Enter a number: "))

print("Array:", end=" ")
for num in arr:
    print(num, end=" ")

if occurs(number, arr):
    print(f"\nResult: number {number} appears in the array")
else:
    print(f"\nResult: number {number} does not appear in the array")