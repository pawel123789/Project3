numbers = '123,21,37,39088755,986854'

def split(text, sep):
    list = []
    elements = ''
    for char in text:
        if char != sep:
                elements += char
        else:
            list.append(elements)
            elements = ''
    list.append(elements)
    return list

print(split(numbers, ','))



