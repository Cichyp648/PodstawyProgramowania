###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last: ', arr[len(arr)-1])
print('Last but one: ', arr[len(arr)-2])
print('Sum of frst and last: ', arr[1] + arr[len(arr)-1])
print('Middle value: ', arr[len(arr)//2])
for i in range(len(arr)):
    print(arr[i], end = ' ')