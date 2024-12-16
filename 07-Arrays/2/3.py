### Monthly expenses calculation program

# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculate total expenses per category and per week
total_food = sum(week[0] for week in monthly_expenses)
total_transport = sum(week[1] for week in monthly_expenses)
total_utilities = sum(week[2] for week in monthly_expenses)

total_week_1 = sum(monthly_expenses[0])
total_week_2 = sum(monthly_expenses[1])
total_week_3 = sum(monthly_expenses[2])
total_week_4 = sum(monthly_expenses[3])

total_expenses = total_food + total_transport + total_utilities

# Print expenses
print('\nMONTHLY EXPENSES')
print('----------------')
print(f'Food: {total_food}')
print(f'Transport: {total_transport}')
print(f'Utilities: {total_utilities}')
print(f'Week 1: {total_week_1}')
print(f'Week 2: {total_week_2}')
print(f'Week 3: {total_week_3}')
print(f'Week 4: {total_week_4}')
print('---------------')
print(f'TOTAL: {total_expenses}')
