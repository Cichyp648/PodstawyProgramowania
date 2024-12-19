import re

username = input('Enter username: ')
password = input('Enter password: ')

username_pattern = r'[a-z]{6,}'
password_pattern = r'[a-zA-Z0-9_]{8,}'

# Check if username and password match the patterns
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

if username_match and password_match:
    print('Username and password match the criteria')
else:
    print('Username and/or password doesn\'t match the criteria')
