def printer(n):
    return '*/' * (n - 1) + '*'

n = int(input('Number of *: '))
generated = printer(n)
print(generated)