def is_palindrome(word):
    if len(word) == 0:
        return True
    elif len(word) == 1:
        return True

    if word[0] == word[-1] and is_palindrome(word[1:-1]):
        return True

    return False


def palindrome(word, idx):
    if len(word) == 0:
        return f"{word} is a palindrome"
    if len(word) == 1:
        return f"{word} is a palindrome"

    is_not_palindrome = "not" in palindrome(word[1:-1], idx)

    if word[0] == word[-1] and not is_not_palindrome:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
