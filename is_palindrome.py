
def is_palindrome(text):
    """Cheks if text is palindrome.

    Args:
        text: string to be checked
    Returns:
        True if text is a palindrome, False if not """
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text) -i-1]:
            return False
    return True

print(is_palindrome('kajak'))



