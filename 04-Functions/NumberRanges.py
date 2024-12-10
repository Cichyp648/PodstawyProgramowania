import NumberRangesModule

RangeA = int(input('First number: '))
RangeB = int(input('Second number: '))
CheckNumber = int(input('Number to check if its in range: '))

IsInRange = NumberRangesModule.IsInRange(RangeA, RangeB, CheckNumber)

print(f'Number {CheckNumber} is in range <{RangeA},{RangeB}>: {IsInRange}')