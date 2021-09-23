def palindrome(word):
    word = word.lower()
    return word == word.lower()[::-1]


x = palindrome('Anna')
print(x)