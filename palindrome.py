def is_palindrome(word):

    letters = list(word)
    is_palindrome = "Palindrome"

    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            is_palindrome = "Not a Palindrome"
            break

    return is_palindrome


word = 'aba'
print(is_palindrome(word))    








