amount = int(input('Number of products: '))
price = int(input('Price: '))
total = 0

if amount == 1:
    total = price
else:
    total = price + (price-1)*0,75

print(f'Total price: {total}')