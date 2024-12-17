import myText

text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", myText.word_count(text))
print("Words from the longest:")
longest_words = myText.words_by_length(text)
for word in longest_words:
    print(word, end=", ")
print()

print("Words ordered alphabetically:")
alphabetical_words = myText.words_alphabetically(text)
for word in alphabetical_words:
    print(word, end=", ")