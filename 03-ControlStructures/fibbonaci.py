a = 0
b = 1
for _ in range(20):
    print(a, end=' ')
    a = a + b
    b = a - b
