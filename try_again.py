number = None

while number is None:

    try:
        number = int(input('Podaj liczbę: '))
    except ValueError:
        print('To nie jest liczba...')
print('Podałeś: ', number)