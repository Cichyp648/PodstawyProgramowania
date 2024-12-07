###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed > speed_limit:
    print(f'Your speed is {...}km/h')
    print('Warning: speed limit exceeded!!')
    
###
# Credit card payment 
#
account_balance = 500
total_payment = int(input('Payment: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')
    
    
###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input('Correctly completed tasks: '))
test_passed = False

if total_tasks - tasks_ok  >= total_tasks / 2:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
    

###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{...} is even')
else:
    print(f'{...} is odd')  
    
    
###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:
    total_salary = basic_salary + basic_salary * bonus
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')


###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Invalid input')
    
    
###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E):')
distance = int(input('Enter distance in km'))

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6

total_consumption = distance / 100 * fuel_consumption
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {fuel_consumption} liters')


###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
operator = input('Enter the operator: ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
    
# print result
print(f'{number1} {operator} {number2} = {result}')


###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month <= 7 and month >= 9:
    quarter = 3
elif month <= 4 and month >= 6:
    quarter = 2
elif month <= 1 and month >= 3:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')


###
# Checking login and password
#
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and entered_password == password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')
    
    
###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age >= 65:
    print('Discount is available')
else:
    print('Discount is unavailable')
    
    
###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
    
    
###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12)'))

if month==1 or month==3 or month ==  5 or month == 7 or month == 9 or month == 11:
    days = 31 ## months with 31 days
elif month == 2 :
    days = 28
else:
    days = 31

print(f'{month} has {days} days')


###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month==1 or month==3 or month ==  5 or month == 7 or month == 9 or month == 11:
    if day >=1 and day <= 31:
        day_ok = True
elif month == 2:
    if day >=1 and day <= 28:
        day_ok = True
else:
    if day >= 1 and day <= 30:
        day_ok = True

message = f'Day {day} for the month {month}'
if day_ok:
    print('{message} is correct')
else:
    print('{message} is incorrect')
    
    
###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + ' '

print(university) # original university name
print(university_expanded) # expanded university name



###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char = char(ord(char) + 1)
    encrypted_text += char

print(plain_text)
print(encrypted_text)


###
# Calculates the sum of integer numbers in the range <1,5>
#
sum = 0

for i in range(5,10):
    sum += i

print(f'Sum is {sum}')


###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1,10):
    if i%2 != 0:
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is {sum}')



###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
for i in range(1, 10):
    print(f'1/{i} = {1/i}')
    

###
# A simple number guessing game
# Randomly chosen number to be guessed from 1 to 100
import random
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")


###
# Sums numbers entered by user
#
total_sum = 0
iteration = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    iteration += 1
    
print(f"The total sum of the numbers is: {total_sum}")
print(f"Aritmethic mean: {total_sum/iteration}")


###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
i = 1
# Calculate the sum of even numbers
while i < N + 1:
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")