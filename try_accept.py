import random

try:
    lower_bound = int(input('Podaj dół zakresu: '))
    upper_bound = int(input('Podaj górę zakresu: '))
    target = random.randint(lower_bound, upper_bound)

    count = 0

    while target != guess:
        count +=1
        guess = int(input('Podaj liczbę: '))
        if guess < target:
            print('Za mało!')
        elif guess > target:
            print('Za dużo!')

    print('Gratlacje! Ilośc ruchów: ', count)
exept ValueError as err:
    print('Oczekiwano liczby. Nie można kontynuować.')
    print('Zwrócony błąd: ', err)