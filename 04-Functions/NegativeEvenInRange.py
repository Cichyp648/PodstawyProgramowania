def Counter(bot, top):
    count = 0

    for num in range(bot, top+1):
        if num < 0 and num % 2 == 0:  # Check if the number is negative and even
            count += 1
    return count

RangeA = int(input('Lowest number in range: '))
RangeB = int(input('Highest number in range: '))

amount = Counter(RangeA, RangeB)
print(f'There are {amount} negative even numbers in that range')