def LetterCounter(text, SelectedLetter):
    counter = 0
    for char in text:
        if char == SelectedLetter:
            counter += 1
    return counter