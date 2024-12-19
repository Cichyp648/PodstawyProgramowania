# Write a program that displays the first five lines from the it_company.csv file 
# and then prints 'Press Enter key...' in the next line and waits for the Enter key to be pressed. 
# The program repeats printing the next five lines from the file, waiting for the Enter key to be pressed each time.

with open('it_company.csv', 'r') as file:
    content = file.read()

content = content.splitlines()
counter = 0

for line in content:
    print(line)
    counter += 1
    if counter == 5:
        input('Press Enter to continue...')
        print()
        counter = 0