# Loop through columns 1 to 7
for i in range(1, 8):
    # Loop through numbers in each column
    for j in range(i, 50, 7):
        # Print each number in the row
        print(j, end=' ')
    # Move to the next line after each row
    print()
