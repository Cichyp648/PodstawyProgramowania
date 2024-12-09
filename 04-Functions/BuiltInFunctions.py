###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter a letter: ")
print(f"Letter read from the keyboard: {letter}")

string_number = int("20303")
print(f"Number representing the string '20303': {string_number}")

binary_string = bin(304)[2:]
print(f"Binary string representing decimal number 304: {binary_string}")

hexadecimal_string = hex(304)
print(f"Hexadecimal string representing decimal number 304: {hexadecimal_string}")

unicode_code_of_euro = ord('€')
print(f"Integer representing the Unicode code of the € sign: {unicode_code_of_euro}")

absolute_value = abs(-17)
print(f"Absolute value of -17: {absolute_value}")
