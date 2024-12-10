def validate(password):
    if len(password) < 6:
        return False
    
    LetterList = set(password)
    if len(LetterList) != len(password):
        return False

    return True

print(validate("ax15"))
print(validate("book123"))
print(validate("A2water3"))
print(validate("qwerty"))
print(validate(""))