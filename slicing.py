numbers = '123,21,37,39088755,986854'

def split(text, sep):
    list = []
    elements = ''
    for char in text:
        if char != sep:
                elements += char
        else:
            list.append(''.join(elements))
            elements = ''
    list.append(''.join(elements))
    return list

print(split(numbers, ','))


def split2(text, sep):
    list = []
    start = 0
    for current, char in enumerate(text):
        if char == sep:
            list.append(text[start:current])
            start = current + 1
        list.append(text[start:])
        return list
print(split2(numbers, ','))