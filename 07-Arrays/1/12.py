# Monthly expenses and their corresponding expense categories are included in the arrays below.
# Write a program that calculates which expense category was the most expensive.

categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

MaxPos, MaxValue = 0, 0

for i in range(len(expenses)):
    if expenses[i] > MaxValue:
        MaxValue = expenses[i]
        MaxPos = i

print(f'The most expensive is {categories[MaxPos]} with {expenses[MaxPos]} spent')