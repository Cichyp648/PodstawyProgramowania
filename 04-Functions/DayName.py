# Function that returns the full name of a day of the week based on its number
def day_name(day_number):
    match day_number:
        case 1:
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thursday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'

for i in range(1,8):
    name = day_name(i)
    print(f'Day no {i} is {name}')