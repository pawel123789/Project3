import funny_strings

def bubblesize(text):
    """Returns bubbelized string"""
    chars = []
    target = ''
    text = text.lower()
    for idx, char in enumerate(text):
        if idx % 2 == 1:
            target += char.upper()
        else:
            idx % 2 == 0
            target += char.lower()
    return ''.join(chars)

print(funny_strings.bubblesize('Salamandra'))