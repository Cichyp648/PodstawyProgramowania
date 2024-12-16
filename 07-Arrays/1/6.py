###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]

print(f'Weekday 1 is {weekday(1)}')
print(f'Weekday 4 is {weekday(4)}')
print(f'Weekday 7 is {weekday(7)}')