import re

text = input('Enter text to check: ')
pattern = r'[aeiou]'
counter = len(re.findall(pattern, text))

print(counter)