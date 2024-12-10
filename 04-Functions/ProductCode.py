def f(product_code):
    # 3 first digits and their sum
    d1, d2, d3, d4 = int(product_code[0]), int(product_code[1]), int(product_code[2]), int(product_code[3])
    sum = d1 + d2 + d3
    
    if d4 == sum % 7:
        return True
    else:
        return False

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
