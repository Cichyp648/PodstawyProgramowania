def word_count(text):
    return len(text.split())

def words_by_length(text):
    return sorted(text.split(), key=len, reverse=True)

def words_alphabetically(text):
    return sorted(text.split())