question1 = input('Are you interested in computer science? (y/n): ') == 'y'
question2 = input('Do you like playing computer games? (y/n): ') == 'y'
question3 = input('Do you have an Instagram account? (y/n): ') == 'y'

print('SURVEY RESULTS')
print(f'Interested in computer science: {"Yes" if question1 else "No"}')
print(f'Playing computer games: {"Yes" if question2 else "No"}')
print(f'Has an Instagram account: {"Yes" if question3 else "No"}')
