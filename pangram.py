import string

print(string.ascii_lowercase)

def pangram(text):
    text = text.lower()
    for letter in string.ascii_lowercase:
        if letter not in text:
            return False
    return True

check = 'some random text with not all ascii characters'
check2 = 'kjash'

print(pangram(check))
print(pangram(check2))


def is_pangram(text):
    found_letters = {}
    for char in text.lower():
        if char.isalpha():
            found_letters[char] = 0
    if len(found_letters) == len(string.ascii_lowercase):
        return True
    return False