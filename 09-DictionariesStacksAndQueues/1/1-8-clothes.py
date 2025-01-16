# Initial price list
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}


def before_discount():
    print("Products and Prices Before Discount:")
    for product, price in price_list.items():
        print(f"{product}: ${price:.2f}")


def before_discount_total():
    total_before_discount = sum(price_list.values())
    print(f"\nTotal value of products before discount: ${total_before_discount:.2f}")


def apply_discount():
    for product in price_list:
        price_list[product] = round(price_list[product] * 0.9, 2)


def after_discount():
    print("\nProducts and Prices After 10% Discount:")
    for product, price in price_list.items():
        print(f"{product}: ${price:.2f}")


def after_discount_total():
    total_after_discount = sum(price_list.values())
    print(f"\nTotal value of products after discount: ${total_after_discount:.2f}")



before_discount()
before_discount_total()
apply_discount()
after_discount()
after_discount_total()
