import LetterOccurencesModule

text = input('Enter your text: ')
letter = input('Letter to count in text: ')

occurences = LetterOccurencesModule.LetterCounter(text, letter)

print(f'There are {occurences} letters {letter} in given text')