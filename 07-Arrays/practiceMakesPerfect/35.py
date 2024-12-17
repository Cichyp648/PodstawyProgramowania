def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    
    # New transposed matrix
    transposed = [[0] * rows for _ in range(cols)]
    
    # Fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = m[i][j]
    
    return transposed

def print_2d_array(array):
    for row in array:
        print(row)

matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]]
]

for idx, matrix in enumerate(matrices, 1):
    print(f"Matrix {idx}:")
    print_2d_array(matrix)
    
    transposed_matrix = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    print_2d_array(transposed_matrix)
    print()  # Empty line for better separation
