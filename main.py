def palindromes(text):
    text = str(text.lower())
    palindrome = ''
    for i in range(len(text)):
        for j in range(len(text), i, -1):
            if len(palindrome) >= j - i:
                break
            elif text[i:j] == text[i:j][::-1]:
                palindrome = text[i:j]
    if len(palindrome) > 1:
        a = text.find(palindrome)
        b = text.find(palindrome) + len(palindrome) - 1
        print(a, b)
    else:
        print(-1, -1)


palindromes("kajak")