amount = int(input('Enter the amount in PLN: '))

five_zloty = amount // 5
amount %= 5

two_zloty = amount // 2
amount %= 2

one_zloty = amount

print(f'The amount of PLN {amount + five_zloty * 5 + two_zloty * 2} in coins:')
print(f'5 PLN coins: {five_zloty}')
print(f'2 PLN coins: {two_zloty}')
print(f'1 PLN coins: {one_zloty}')