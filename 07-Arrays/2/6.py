# Program to Modify Main Diagonal of a Square Matrix
matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# Replace main diagonal with 1
for i in range(len(matrix)):
    matrix[i][i] = 1

# Print the modified matrix
print("Modified Matrix:")
for row in matrix:
    print(row)
