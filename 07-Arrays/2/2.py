### Tic-Tac-Toe board program

# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

# Print the Tic-Tac-Toe board
print("Tic-Tac-Toe Board:")
for row in tic_tac_toe_board:
   for cell in row:
      print(cell, end=" ")
   print()
