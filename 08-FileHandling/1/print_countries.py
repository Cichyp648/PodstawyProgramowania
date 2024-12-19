###
# Reads from file, line by line
#

with open('countries.txt', 'r') as file:
    counter = 1
    for line in file:
        print(counter, line, end="")
        counter += 1