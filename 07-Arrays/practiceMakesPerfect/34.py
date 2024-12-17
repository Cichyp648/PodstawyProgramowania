def identity_matrix(n):
    # Initialize a zero matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Set the diagonal to 1
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix

def print_2d_array(arr):
    for row in arr:
        for item in row:
            print(item, end=" ")
        print()


sizes = [3, 5, 8]

for size in sizes:
    print(f"Identity Matrix {size}x{size}:")
    identity_mat = identity_matrix(size)
    print_2d_array(identity_mat)
    print() 
