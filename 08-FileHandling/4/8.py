import re

with open('files.txt', 'r') as file:
    data = file.read()

pattern = r'\..{4}'
matches = re.findall(pattern, data)

for line in matches:
    print(line)