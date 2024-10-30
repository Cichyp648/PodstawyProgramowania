###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

#Read user input, parse to float
celcius = float(input('Temp in C: '))
#Convert the units
fahrenheit = (celcius * 9 / 5) + 32
kelvin = celcius + 273.15
#Output results
print(f'F {fahrenheit}')
print(f'K {kelvin}')