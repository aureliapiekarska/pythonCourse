import random
r_1 = int(input('podaj liczbe rund'))
n = random.randint(1, 100)
win = n
guess = int(input('Wpisz liczbe 1 do 100'))
while n != "guess":
    print
    if guess < win:
        print('Zimno')
        guess = int(input('Wpisz ponownie liczbe od 1 do 100: '))
    elif guess > win:
        print('Zimno')
        guess = int(input('Wpisz ponownie liczbe od 1 do 100 '))
    elif guess == win - 10:
        print('Cieplo')
    elif guess == win + 10:
        print('Cieplo')
    else:
        print('zgadles')
        break
    print
