import random
change_size = 'tutaj co drugi znak ma być zapisany wielką literą'
randomowy = 'ldjfsg lkhkhj uiuytfs'
to_numbers = 'lkjshooeeeiiii!!alkslhka'
powstale = []
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
    pass

def numberize(text):
    pass


