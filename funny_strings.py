import random
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



def randomize(text):
    chars = []
    for idx, char in enumerate(text):
        if random.randint(0, 1):
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return ''.join(chars)







def numberize(text):
    pass


