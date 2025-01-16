translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}


def translate_word(word):
    return translations.get(word.lower(), "Translation unavailable")


word = input("Enter an English word: ").strip()
translation = translate_word(word)
print(f"The Polish translation is: {translation}")
