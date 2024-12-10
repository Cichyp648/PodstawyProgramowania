def AtLeastOneNegative(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))

print(f'At least one negative number: {AtLeastOneNegative(a, b, c)}')