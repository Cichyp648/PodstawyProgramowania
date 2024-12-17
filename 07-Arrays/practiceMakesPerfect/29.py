# A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. Create a program and the function. 
# Then create a two-dimensional array with dimensions of 3 by 5. print the created array.

def create_2d_arr(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

arr = create_2d_arr(3, 5)

for row in arr:
    print(row)