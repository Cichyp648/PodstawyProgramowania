def generator(x):
    output = ''
    for i in range(1, x+1):
        output += str(i)
    return output

length = int(input('Number length: '))
output = generator(length)
print(output)