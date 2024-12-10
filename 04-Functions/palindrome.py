def IsPalindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

print(IsPalindrome('radar'))
print(IsPalindrome('12-11-21'))
print(IsPalindrome('book'))
