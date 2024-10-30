###
# BMI Calculator
#
height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')

###
# The program simulates five dice rolls.
#
import random
print("Dice rolling simulator")
for i in range(5):
    dice_roll = random.randint(1,6)
    print(dice_roll, end=" ")

# A program that calculates the sum of three numbers.
number1 = 71
number2 = 14
number3 = 12
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 2: ', number3)
print('The result of summation: ', result)

# Swapping two varaibles
x = 7
y = 34
z = 0
print("Before swapping: x=", x, "y=", y)
z = x
x = y
y = z
print("After swapping: x=", x, "y=", y)

# Km/h to m/s conversion
speed_kmh = 70
speed_ms = (speed_kmh*1000)/3600
print(speed_kmh, "km/h = ", speed_ms, "m/s")

#Diagonal lenght of a rectangle
import math
a = 5
b = 8
diagonal = math.sqrt(a**2+b**2)
print(diagonal)

# Distance to horizon based on observer height
h = 1.8
d = 3.57 * math.sqrt(h)
print('Distance on sea level: ', d)
h += 20
d = 3.57 * math.sqrt(h)
print('Distance on 20m above sea level: ', d)

###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south/total*100)

###
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print('Average grade is: ', average)

###
# Printing student's personal data
#
name = "Paweł"
age = 20
height = 182
print(f"My name is {name}.")
print(f'I am {age} years old, and my height is {height} cm.')
print(f'In 6 years I will be {age+6} years old')

###
# A program that calculates and prints
# the income of a family per person.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income}, and income per person is {income_per_person}')

###
# A program that writes an expression and it's value
a = 3
b = 5
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')

# A program that reads your first and last name from the keyboard
# Then prints your full name
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')

###
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side ** 3
cube_surface_area = (cube_side ** 2)* 6
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')

###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
cuboid_volume = a*b*c
cuboid_surface_area = a*b*2 + c*b*2 + a*c*2 
print(f'The volume of that cuboid is equal to {cuboid_volume}')
print(f'The surface area of that cuboid is equal to {cuboid_surface_area}')


###
# VAT calculator
amount = int(input('Amount to calculate VAT from: '))
vat = 0.23 * amount
print(f'VAT = {vat:.2f}')

###
# Discount calculator
price_old = int(input('Enter price before the discount: '))
discount = int(input('Enter discount %: '))
price_new = (price_old - price_old * discount / 100)
difference = price_old - price_new
print(f'Discounted price: {price_new:.2f}')
print(f'Price difference: {difference:.2f}')

###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Paweł'   # replace Anna with your name
surname = 'Cichy' # replace May with your surname
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {characters_in_name + len(surname) + 1}') # with a space between name and surname

###
# A program that prints your initials
#
name = 'Paweł'
surname = 'Cichy'
print(name[0],surname[0])

###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
abbr = university[0] + university[7] + university[21]
print(abbr)

###
# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[22:32]}')
print(f'Initials: {employee[4]+employee[9]}')

###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
formatted = phone[0:3] + '-' + phone[3:6] + '-' + phone[6:9]
print(formatted)


###
# A program to print numerical representations of characters.
#
print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'1 {ord('1')}')
print(f'= {ord('=')}')
print(f'+ {ord('+')}')
print(f'€ {ord('€')}')


###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Paweł' 
for x in name:
    print(f'The letter {x} has a code {ord(x)}')

###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = last_letter_code - first_letter_code - 1
print(f'Between {first} and {last} is {number_of_letters} letters')


###
# Character code conversion
#
codes = 67, 111, 111, 108, 33
for code in codes:
    print(chr(code), end="")

###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Capital letters: ', movie.upper())

# print title in small letters
print('Small letters: ', movie.casefold())

# print how many times the vowel "e" appears in the title
print('Letters "e": ', movie.count('e'))

# print where in the text is the word "Lord"
print('"Lord" location: ', movie.find('Lord'))

# print where in the text is the word "dragon"
print('"Dragon" location: ', movie.find('dragon'))


###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
age = int(input('Enter age: '))
no_tax = age <= 26
print(f'Exemption from paying taxes: {no_tax}')


###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')


###
# A program that checks whether the number entered
# from the keyboard is even.
#
number = int(input('Enter number: '))
even = number % 2 == 0
print(f'Number is even: {even}')

###
#Program to test if a tree can be cut
circumference = int(input('Tree circumference: '))
diameter = circumference / math.pi
canCut = diameter >= 50
print(f'The tree can be cut: {canCut}')


###
# Vehicle registration numbers in Krakow start
# with the letters KR or KK. Write a program that checks
# whether the vehicle registration number entered
# from the keyboard means a vehicle from Krakow.
# Print True whether a car is from Krakow or False otherwise.
#
car_number = input('Enter car registration number: ')
is_krakow = car_number[0:2] == "KR" or car_number[0:2] =="KK"
print(f'Car is from Krakow: {is_krakow}')

###
# Check if speed is between 40 and 140 km/h

speed = int(input("Input car speed in km/s: "))
check = speed >= 40 and speed <= 140
print(f'Speed is within 40 and 140 km/h: {check}')


###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
rollSum = 0
for i in range(3):
    roll = random.randint(1,6)
    print(f'Roll no. {i}: {roll}')
    rollSum += roll
print(f'Sum of rolls: {rollSum}')

###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
computer = random.randint(1,6)
you = int(input('Your guess: '))
isCorrect = you == computer
print(f'You won: {isCorrect}')