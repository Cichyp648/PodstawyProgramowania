old = int(input("Old price: "))
new = int(input("New price: "))
decrease = old/new*100

if decrease >= 10:
    print("Buy the product!!")
    print(f'Product price reduced by {decrease}')