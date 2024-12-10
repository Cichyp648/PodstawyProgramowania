# Minumim number of coins
# Accepted: #1, 2, 5

def LargestCoin():
    if PriceBuffer - 5 >= 0:
        return 5
    elif PriceBuffer - 2 >= 0:
        return 2
    elif PriceBuffer - 1 >= 0:
        return 1

price = 23
#price = int(input('Enter the price: '))
PriceBuffer = price
CoinAmount = 0

while PriceBuffer != 0:
    if PriceBuffer in [1, 2, 5]:
        CoinAmount += 1
        PriceBuffer = 0
    else:
        PriceBuffer -= LargestCoin()
        CoinAmount += 1

print(f'Minimum amount of coins: {CoinAmount}')