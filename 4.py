def largestPalindrome():
    # Find all palindromes
    palindromes = []
    for n in reversed(range(1000000)):
        stringN = str(n)
        count = 0
        for i in range(len(stringN)/2):
            if stringN[i] == stringN[len(stringN)-1-i]:
                count += 1
        if count == len(stringN)/2:
            palindromes.append(n)
    # Find which of those palindromes are the product of 2 three-digit numbers
    threeDigits = []
    for i in reversed(range(500, 999)):
        for j in reversed(range(500, 999)):
            if i*j in palindromes:
                print i*j
                threeDigits.append(i*j)
    # Find the largest of those palindromes
    maximum = 0
    for i in threeDigits:
        if i > maximum:
            maximum = i
    return maximum

print largestPalindrome()
