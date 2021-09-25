def palindromes(text):
    text = str(text.lower())
    results = []
    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                results.append(chunk)
    if len(results) > 0:
        pali = max(results, key=len)
        a = text.find(pali)
        b = text.find(pali) + len(pali) - 1
        print(a, b)
    else:
        print(-1, -1)


palindromes("kajak")