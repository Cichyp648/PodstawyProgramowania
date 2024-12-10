# Calculates a sum of digits in given number
# True for only even digits, false for odd

def SumEven(number):
    sum, buffer = 0, 0
    for digit in number:
        buffer = int(digit)
        if buffer % 2 == 0:
            sum += buffer
    return sum

def SumOdd(NumberString):
    sum, buffer = 0, 0
    for digit in number:
        buffer = int(digit)
        if buffer % 2 != 0:
            sum += buffer
    return sum

number = '3124'
#number = input('Number: ')
OnlyEven = True
#OnlyEven = input('True for even, False for odd digits: ') == 'True'

if OnlyEven == True:
    sum = SumEven(number)
else:
    sum = SumOdd(number)

print(f'Sum: {sum}')