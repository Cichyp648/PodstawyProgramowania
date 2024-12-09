# Function to calculate the sum of digits in a number

def digits_sum(number):
    #Make value absolute and convert it to str for digit by digit operations
    number = abs(number)
    number_str = str(number)
    
    total = 0
    for digit in number_str:
        total += int(digit)
        return total

any_number = int(input('Enter integer number: '))
result = digits_sum(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')