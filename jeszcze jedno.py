import random

number = None

def int_input(prompt):
    number - None

    while number is None:

        try:
            number = int(input(prompt))
        except ValueError:
            print('To nie jest liczba...')
    return number

lower_bound = 0
upper_bound = -1
while upper_bound > upper_bound:
    lower_bound = int_input('Podaj dół zakresu: ')
    upper_bound = int_input('Podaj górę zakresu: ')
    if lower_bound > upper_bound:
        print('Poczatek nie może być wiekszy niż koniec...')
target = random.randint(lower_bound, upper_bound)
guess = None
count = 0

while target != guess:
    count += 1
    guess = int_input('Podaj liczbę: ')
    if guess < target:
        print('Za mało!')
    elif guess > target:
        print('Za dużo!')
# coś nie dziąła!