# Display text from file and count number of words

with open('pets.txt', 'r') as file:
    content = file.read()

contentLines = content.splitlines()
for line in contentLines:
    lineLength = len(line.split())
    print(lineLength ,line)

