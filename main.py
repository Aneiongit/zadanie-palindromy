def palindrome(word):
    if str(word) == str(word)[::-1]:
        print(True)
    else:
        print(False